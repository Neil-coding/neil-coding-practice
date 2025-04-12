import pybullet as p
import pybullet_data
import time 

# Connect to the simulation GUI
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load the plane
plane = p.loadURDF('plane.urdf')

# Set gravity
p.setGravity(0, 0, -9.8)

# Load R2D2 robots at different positions
rbs = []
wls = []
for i in range(1, 5):
    for j in range(1, 5):
        rbs.append(p.loadURDF('r2d2.urdf', [i, j, 1]))
        wls.append(p.loadURDF('walls.urdf', [i+10, j, 1]))
        wls.append(p.loadURDF('walls.urdf', [i+10, j+10, 1]))
        wls.append(p.loadURDF('walls.urdf', [i-10, j, 1]))
            
# Apply a forward force to each robot
for i in range(10000):
    for each in rbs:
        # Get the base link index for the R2D2 robot
        base_link_index = 0  # the main body of the robot
        # Apply an external force along the x-axis (forward direction)
        force = [0, 0, 500]  # Adjust the '100' for different force magnitude
        position = p.getBasePositionAndOrientation(each)[0]  # Get position of the base
        
        # Apply force at the center of mass (position of the base)
        p.applyExternalForce(each, base_link_index, force, position, p.WORLD_FRAME)


        
    # Step the simulation
    p.stepSimulation()
    time.sleep(1 / 240)
