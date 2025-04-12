import pybullet as p
import time
import pybullet_data

# Initialize the physics client and load URDFs
physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally add search path
p.setGravity(0, 0, -10)  # Set gravity

# Load the plane and the R2-D2 robot
planeId = p.loadURDF("plane.urdf")
startPos = [0, 0, 1]
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
boxId = p.loadURDF("r2d2.urdf", startPos, startOrientation)

# Initializing robot's control variables
speed = 0.1  # Control speed (movement increment per step)

# Simulation loop
while True:
    p.stepSimulation()
    time.sleep(1. / 240.)

    # Get keyboard events
    keyboardEvents = p.getKeyboardEvents()

    # Check for arrow key presses
    for key, state in keyboardEvents.items():
        if state & p.KEY_WAS_TRIGGERED:  # 'W' key pressed (move forward)
            p.applyExternalForce(boxId, -1, forceObj=[0, 0, speed], posObj=[0, 0, 0], flags=p.WORLD_FRAME)
        elif state & p.KEY_WAS_TRIGGERED:  # 'S' key pressed (move backward)
            p.applyExternalForce(boxId, -1, forceObj=[0, 0, -speed], posObj=[0, 0, 0], flags=p.WORLD_FRAME)
        elif state & p.KEY_WAS_TRIGGERED:  # 'A' key pressed (move left)
            p.applyExternalForce(boxId, -1, forceObj=[-speed, 0, 0], posObj=[0, 0, 0], flags=p.WORLD_FRAME)
        elif state & p.KEY_WAS_TRIGGERED:  # 'D' key pressed (move right)
            p.applyExternalForce(boxId, -1, forceObj=[speed, 0, 0], posObj=[0, 0, 0], flags=p.WORLD_FRAME)

    # Get and print the current position and orientation of the R2-D2 robot
    cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
    print("Position:", cubePos, "Orientation:", cubeOrn)

    # Disconnect on a specific condition (like user pressing the 'Q' key)
    if 65307 in keyboardEvents:  # ESC key to exit the simulation
        break

# Disconnect from the simulation
p.disconnect()
