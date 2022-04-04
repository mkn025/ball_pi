from fractions import Fraction

class Block:
  # Creating a class since that helps keep track of attributes
  def __init__(self, mass, velocity, position):
    self.mass = mass
    self.velocity = velocity
    self.position = position

# Set initial conditions: the object on the left is at rest at x = 5 and has
# unit mass. The one on the right starts off at x = 10, with velocity =
# -5 units/s and has mass equal to 100^n, where n is user-specified.
# The number of collisions should be floor(Pi*10^n). e.g. n = 2 => 314,
# n = 3 => 3141, and so on

small = Block(1, 0, Fraction(32/10))
large = Block(100**int(input("Which power of 100 is the second mass? ")),
             -7, Fraction(75,10))

# By "collision", we mean that either the position of both the objects is the
# same (both collide against each other) or the position of the small block is
# 0 (collision against wall)

def updateVelocities(collisions):
  if(small.position == large.position != 0):
    # Both blocks collide against each other
    collisions += 1
    temp = small.velocity

    small.velocity = Fraction(((2*large.mass*large.velocity)+
    (small.mass*small.velocity)-(large.mass*small.velocity)),
    (small.mass + large.mass))

    large.velocity = Fraction(((2*small.mass*temp)+(large.mass*large.velocity)
    -(small.mass*large.velocity)),(small.mass + large.mass))

  elif(small.position == 0 != large.position):
    # The small block gets "reflected" off the wall
    collisions += 1
    small.velocity = -small.velocity

  elif(small.position == large.position == 0):
    # The rare instance in which both blocks move towards the wall and
    # collide with the wall and against each other simultaneously
    collisions += 2
    small.velocity, large.velocity = -small.velocity, -large.velocity
  else:
    pass

  return collisions

# Given the current positions and velocities, find the time to next collision
# This takes care of all different scenarios  
def timeToNextCollision():
  if(large.velocity >= small.velocity >= 0):
    # Both blocks move towards right, but the large block is faster and the
    # small block can't catch up
    return float("inf")

  elif(small.velocity >= 0 >= large.velocity):
    # Both blocks are either moving towards each other, or one of the is at
    # rest and the other is moving towards it. The wall is obviously ignored
    # The condition small.velocity == 0 == large.velocity will also be ignored
    # since if that's true, only the first if statement would be executed.
    return Fraction(large.position - small.position,
                    small.velocity - large.velocity)

  elif((large.velocity >= 0 and small.velocity < 0) or
       (small.velocity <= large.velocity < 0)):
    # Both blocks move towards left, but the large block can't catch up with
    # the small block before the latter runs into the wall
    return Fraction(-small.position, small.velocity)

  elif(small.position == 0):
    # Special case for when the small block is currently at the wall
    if(large.velocity >= abs(small.velocity)):
      # Small block can no longer catch up with large block
      return float("inf")
    else:
      # Large block is either moving towards left or too slow moving towards
      # the right. In either case, they will collide
      return large.position/(abs(small.velocity) - large.velocity)
  else:
    # Both blocks move towards left, but large block is faster. If the
    # distance between blocks is small enough compared to that between the wall
    # and the small block, they will collide. Otherwise the small block will
    # reach the wall before the large block has a chance to catch up
    return min(Fraction(-small.position, small.velocity),
               Fraction(large.position - small.position), 
                       (small.velocity - large.velocity))

collisionCount = 0

while True:
  t = timeToNextCollision()
  if(t == float("inf")):
    # No more collisions
    break
  # Update the distances to what they'll be during the next collision
  small.position += small.velocity*t
  large.position += large.velocity*t
  # Update collision count AND velocities to post-collision values
  collisionCount = updateVelocities(collisionCount)

print(collisionCount)