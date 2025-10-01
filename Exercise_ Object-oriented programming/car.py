"""Car simulation module with 2D movement and heading tracking."""

from math import cos, radians, sin

class Car:
    """A 2D car that can turn and drive, tracking position and heading."""
    
    def __init__(self, x = 0.0, y = 0.0, heading = 0.0):
        """Initialize car with position and heading.
        
        Args:
            x (float): Initial x coordinate (default: 0.0)
            y (float): Initial y coordinate (default: 0.0)
            heading (float): Initial heading in degrees (default: 0.0)
            
        Side effects:
            Sets the x, y, and heading attributes.
        """
        self.x = x
        self.y = y
        self.heading = heading
        
    def turn(self, angle):
        """Turn the car by the given angle in degrees.
        
        Args:
            angle (float): Angle to turn in degrees
        
        Side effects:
            Updates the heading attribute, keeping it in the range [0, 360).
        """
        self.heading = (self.heading + angle) % 360
    
    def drive(self, distance):
        """Drive forward by the given distance.
        
        Args:
            distance (float): Distance to drive forward
        
        Side effects:
            Updates the x and y attributes based on the heading and distance.
        """
        self.x += distance * sin(radians(self.heading))
        self.y -= distance * cos(radians(self.heading))

def sanity_check():
    """Test the Car class functionality.
    
    Returns:
        None: Prints location and heading to console
        
    Side effects:
        Prints the final location and heading of the car to the console.
    """
    c1 = Car()
    c1.turn(90)
    c1.drive(10)
    c1.turn(30)
    c1.drive(20)
    
    print(f"Location: {c1.x}, {c1.y})")
    print(f"Heading: {c1.heading}")
    
    return c1

if __name__ == "__main__":
    sanity_check()

