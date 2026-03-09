#Name: Duy Bao Khang Nguyen
#StudentID: 185000239
#Date: 30/1/2026 @6PM
import matplotlib.pyplot as plt
import math
import astropy.coordinates

def spherical_to_components(magnitude, bearing, trajectory):
    """Takes a 3D vector, and returns a tuple of the x, y, and z components"""
    return astropy.coordinates.spherical_to_cartesian(magnitude, math.radians(trajectory), math.radians(bearing))

def components_to_spherical(x, y, z):
    """Takes the x, y, and z components of a 3D vector, and returns a tuple of magnitude, bearing, and trajectory"""
    magnitude, trajectory, bearing = astropy.coordinates.cartesian_to_spherical(x, y, z)
    return magnitude, math.degrees(bearing.to_value()), math.degrees(trajectory.to_value())

def distance(x1, y1, z1, x2, y2, z2):
    """Takes the x, y, and z coordinates of two objects, and returns the distance between the two."""
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

class Asteroid:
    def __init__(self):
        #Define a list to store values for xpos, ypos,zpos,speed,time and distance for each updated iteration
        self.xpos = []
        self.ypos = []
        self.zpos = []
        self.speed = []
        self.time = []
        self.distance = []
    def runsim(self,starting_xposition,starting_yposition,starting_zposition,starting_xvelocity, starting_yvelocity, starting_zvelocity,timeinterval):
        #current position of x,y,z are at the beginning (starting point)
        #current velocity for x,y,z are the same (at the start)
        #time = 0
        current_x = starting_xposition
        current_y = starting_yposition
        current_z = starting_zposition
        current_xveloc = starting_xvelocity
        current_yveloc = starting_yvelocity
        current_zveloc = starting_zvelocity
        current_time = 0

        #Initial Distance
        initial_distance = distance(starting_xposition,starting_yposition,starting_zposition,0,0,0)

        print("Starting Simulation...")
        running_status = True
        while running_status:
            #append x,y,z position value to x,y,z position list (for each update)
            self.xpos.append(current_x)
            self.ypos.append(current_y)
            self.zpos.append(current_z)
            self.time.append(current_time)

            #calculate the latest distance
            current_distance = distance(current_x,current_y,current_z,0,0,0)
            self.distance.append(current_distance)

            #calculate latest speed ([0] at the end is to retrieve the magnitude)
            total_speed = components_to_spherical(current_xveloc,current_yveloc,current_zveloc)[0]
            self.speed.append(total_speed)

            #Condition Check
            if current_distance < 6400:
                print("Impact")
                running_status = False
            elif current_distance >= 2*initial_distance:
                print("Flyaway")
                running_status = False
            elif current_time > 300000:
                print("Time Out!")
                running_status = False


            #X,Y,Z Position
            new_x = current_x + current_xveloc*timeinterval
            new_y = current_y + current_yveloc*timeinterval
            new_z = current_z + current_zveloc*timeinterval
    
            #X,Y,Z Velocity
            new_xveloc = current_xveloc -1434921106/(current_distance**3)*current_x
            new_yveloc = current_yveloc -1434921106/(current_distance**3)*current_y
            new_zveloc = current_zveloc -1434921106/(current_distance**3)*current_z
        
    
            #Update variables' values
            current_x = new_x
            current_y = new_y
            current_z = new_z
            current_xveloc = new_xveloc
            current_yveloc = new_yveloc
            current_zveloc = new_zveloc
            current_time += timeinterval
    
    #Plot
    def plot(self):
        # 1. X-Position vs Time 
        plt.plot(self.time, self.xpos)
        plt.title("X-Position vs Time")
        plt.xlabel("Time (hours)")
        plt.ylabel("X Position (km)")
        plt.show()

        # 2. X-Position vs Y-Position 
        plt.plot(self.xpos, self.ypos)
        plt.title("X Position vs. Y Position")
        plt.xlabel("x (Distance) (km)")
        plt.ylabel("y (Distance) (km)")
        plt.axis('square') 
        plt.show()

        # 3. Distance vs Time 
        plt.plot(self.time, self.distance)
        plt.title("Distance vs Time")
        plt.xlabel("Time (hours)")
        plt.ylabel("Distance (km)")
        plt.show()

        # 4. Speed vs Time
        plt.plot(self.time, self.speed)
        plt.title("Speed vs Time")
        plt.xlabel("Time (hours)")
        plt.ylabel("Speed (km/h)")
        plt.show()

        # 5. 3D Plot
        ax = plt.axes(projection='3d')
        plt.title("3D Path of Asteroid")
        ax.set_xlabel("x (km)")
        ax.set_ylabel("y (km)")
        ax.set_zlabel("z (km)")
        
        # Plot trajectory
        ax.plot(self.xpos, self.ypos, self.zpos)
        # Plot Earth at origin
        ax.plot([0], [0], [0], 'ro')     
        plt.show()
#Run simulation and display result  
sim = Asteroid()
sim.runsim(500000,500000,0,0,10,10,1)
sim.plot()
