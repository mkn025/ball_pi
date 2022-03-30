import os


# run powershell command
def run_command(command):
    return os.popen(command).read()

for n in range(10):
    run_command("C:/Users/marti/AppData/Local/Microsoft/WindowsApps/python3.9.exe c:/Users/marti/Documents/GitHub/ball_pi/test3.py")



# sorts a txt file 
def sort_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    lines.sort()
    with open(file_name, 'w') as f:
        f.writelines(lines)

# delete duplicate lines in a txt file
def delete_duplicate_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    lines = list(dict.fromkeys(lines))
    with open(file_name, 'w') as f:
        f.writelines(lines)




sort_file("c:/Users/marti/Documents/GitHub/ball_pi/test.txt")
delete_duplicate_lines("c:/Users/marti/Documents/GitHub/ball_pi/test.txt")
