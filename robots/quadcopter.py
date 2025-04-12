import pybullet as p
import pybullet_data
import time

# Connect to PyBullet
physicsClient = p.connect(p.GUI)

# Setup environment
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

# Load plane and rocket
plane_id = p.loadURDF("plane.urdf")
robotId = p.loadURDF("r2d2.urdf", [0, 0, 1])

# Simulate thrust
for step in range(30000):
    if step <3000:
        p.setJointMotorControlArray(
                robotId,
                jointIndices=[1,2, ],  # Assuming these are the wheel joints
                controlMode=p.VELOCITY_CONTROL,
                targetVelocities=[50,50]  # Turn by making one wheel slower
            ) #move robot
    else:
        p.setJointMotorControlArray(
            robotId,
            jointIndices=[0, 1,2, 3,4,5,6,7],  # Assuming these are the wheel joints
            controlMode=p.VELOCITY_CONTROL,
            targetVelocities=[5,5,5,5,5,5,5,5]  # Turn by making one wheel slower
        ) #move robot

    p.stepSimulation()
    time.sleep(1/2400)

p.disconnect()

