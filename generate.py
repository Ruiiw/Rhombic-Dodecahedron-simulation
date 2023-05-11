import pyrosim.pyrosim as pyrosim

def Generate_Body():
    pyrosim.Start_URDF("body4.urdf")
    pyrosim.Send_RD(name="Central", pos=[0, 0, 0], size = [1, 1, 1], rpy = [0, 0, 0.62])
    pyrosim.Send_Joint(name = "Central_FrontOne" , parent= "Central" , child = "FrontOne" , type = "fixed", position = [0, 4.086, 0])
    pyrosim.Send_RD(name="FrontOne", pos=[0, 0, 0], size = [1, 1, 1], rpy = [0, 0, 0.62])
    pyrosim.End()
       
Generate_Body()