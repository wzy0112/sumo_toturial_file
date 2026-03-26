import json
import optparse
import sys
import time
import traci
from sumolib import checkBinary
import os

# 检查 SUMO_HOME 环境变量
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

# 是否使用 GUI
if_show_gui = True

# 选择 sumo 或 sumo-gui
if not if_show_gui:
    sumoBinary = checkBinary('sumo')
else:
    sumoBinary = checkBinary('sumo-gui')

# sumocfg 文件路径（注意双反斜杠）
sumocfgfile = "C:\\sumo-1.3.1\\file\\traci\\exa.sumocfg"

# 启动仿真
traci.start([sumoBinary, "-c", sumocfgfile])

# 仿真循环
for step in range(0, 200):
    time.sleep(1)
    traci.simulationStep(step + 1)

    simulation_current_time = traci.simulation.getTime()
    print("仿真时间是：", simulation_current_time)

    # 获取所有车辆 ID
    all_vehicle_id = traci.vehicle.getIDList()

    # 获取所有车辆位置
    all_vehicle_position = [
        (i, traci.vehicle.getPosition(i)) for i in all_vehicle_id
    ]

    print(all_vehicle_position)

# 关闭仿真
traci.close()