import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadURDF("body4.urdf")
# pyrosim.Start_URDF("box.urdf")
# pyrosim.Send_Cube(name="box", pos=[0.5, -0.5, 0.5] , size=[1, 1, 1])
# pyrosim.End()
# p.loadURDF("box.urdf")
for i in range(10000):
    p.stepSimulation()
    time.sleep(1/60)
p.disconnect()