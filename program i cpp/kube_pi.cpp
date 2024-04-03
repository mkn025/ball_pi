#include <iostream>
#include <SDL.h>
#include <SDL_mixer.h>
#include <cmath>

const int SCREEN_WIDTH = 1280;
const int SCREEN_HEIGHT = 720;
const int BALL_SIZE = 50;
const int GROUND_HEIGHT = 100;
const int FPS = 60;

SDL_Window* window = nullptr;
SDL_Renderer* renderer = nullptr;
Mix_Music* music = nullptr;

struct Cube {
    float x;
    float y;
    float speed;
    float mass;
};

bool initialize() {
    if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_AUDIO) != 0) {
        std::cerr << "SDL initialization failed: " << SDL_GetError() << std::endl;
        return false;
    }

    window = SDL_CreateWindow("Colliding Balls", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
    if (!window) {
        std::cerr << "Window creation failed: " << SDL_GetError() << std::endl;
        return false;
    }

    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    if (!renderer) {
        std::cerr << "Renderer creation failed: " << SDL_GetError() << std::endl;
        return false;
    }

    if (Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 2048) < 0) {
        std::cerr << "SDL_mixer could not initialize! SDL_mixer Error: " << Mix_GetError() << std::endl;
        return false;
    }

    return true;
}

void close() {
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    Mix_FreeMusic(music);
    Mix_Quit();
    SDL_Quit();
}

void drawRect(SDL_Renderer* renderer, int x, int y, int width, int height, SDL_Color color) {
    SDL_Rect rect = { x, y, width, height };
    SDL_SetRenderDrawColor(renderer, color.r, color.g, color.b, 255);
    SDL_RenderFillRect(renderer, &rect);
}

void drawScene(Cube& bigCube, Cube& smallCube, int numCollisions) {
    SDL_SetRenderDrawColor(renderer, 30, 30, 30, 255);
    SDL_RenderClear(renderer);

    drawRect(renderer, 0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT, { 125, 177, 244 });
    drawRect(renderer, bigCube.x, bigCube.y, BALL_SIZE, BALL_SIZE, { 95, 137, 140 });
    drawRect(renderer, smallCube.x, smallCube.y, BALL_SIZE / 5, BALL_SIZE / 5, { 95, 137, 140 });

    SDL_RenderPresent(renderer);
}

void playSound() {
    Mix_PlayChannel(-1, music, 0);
}

void handleCollision(Cube& bigCube, Cube& smallCube, int& numCollisions) {
    if ((smallCube.x + BALL_SIZE / 5) < bigCube.x || smallCube.x > (bigCube.x + BALL_SIZE)) {
        return; // No collision
    }

    numCollisions++;

    float v1 = ((bigCube.mass - smallCube.mass) * bigCube.speed + 2 * smallCube.mass * smallCube.speed) / (bigCube.mass + smallCube.mass);
    float v2 = ((smallCube.mass - bigCube.mass) * smallCube.speed + 2 * bigCube.mass * bigCube.speed) / (bigCube.mass + smallCube.mass);

    bigCube.speed = v1;
    smallCube.speed = v2;

    playSound();
}

int main(int argc, char* argv[]) {
    if (!initialize()) {
        std::cerr << "Initialization failed!" << std::endl;
        return 1;
    }

    Cube bigCube = { 220, SCREEN_HEIGHT - GROUND_HEIGHT - BALL_SIZE, -0.9, 100 };
    Cube smallCube = { 70, SCREEN_HEIGHT - GROUND_HEIGHT - BALL_SIZE / 5, 0, 1 };
    int numCollisions = 0;

    music = Mix_LoadMUS("klikkelyd.wav");
    if (!music) {
        std::cerr << "Failed to load sound file: " << Mix_GetError() << std::endl;
    }

    bool running = true;
    Uint32 startTime = SDL_GetTicks();
    Uint32 elapsedTime = 0;

    while (running) {
        SDL_Event event;
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            }
        }

        const Uint8* keystates = SDL_GetKeyboardState(NULL);
        if (keystates[SDL_SCANCODE_ESCAPE]) {
            running = false;
        }

        if (elapsedTime == 0 && bigCube.speed != 0) {
            handleCollision(bigCube, smallCube, numCollisions);
        }

        bigCube.x += bigCube.speed;
        smallCube.x += smallCube.speed;

        if (bigCube.x > SCREEN_WIDTH) {
            running = false;
        }

        drawScene(bigCube, smallCube, numCollisions);

        SDL_Delay(1000 / FPS);
        elapsedTime = SDL_GetTicks() - startTime;
    }

    close();
    return 0;
}
