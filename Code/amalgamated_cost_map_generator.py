import pandas as pd
import numpy as np
import os

base_dir = '/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Data'
data_dir=os.path.join(base_dir, "amalgamated_cost_map.csv")



#applies cost function on static features: y=0.4(road_network) + 0.4 (important_cells) + 0.2(slope)
def static_cost_calculation(road_network, important_cells, slope):
    static_cost_map = (0.4*road_network) + (0.4*important_cells) + (0.2*slope)
    return static_cost_map



#applies priority function on dynamic features: y = 0.6(survivors) + 0.2(findings) 0.2(report_information)
def cell_priority_calculation(survivors, findings, report_information):
    cell_priority = (0.65*survivors) + (0.20*findings) + (0.15*report_information)
    return cell_priority



#function takes in static and dynamic features. applies static cost calculation, cell priority: priority*static_cost
def cost_amalgamation():
    static_cost= static_cost_calculation(road_network, important_cells, slope)
    cell_priority=cell_priority_calculation(survivors, findings, report_information)
    amalgamated_cost=cell_priority/static_cost
    return amalgamated_cost





#defining paths to datasets
road_network_path=os.path.join(base_dir, "road_network.csv")
important_cells_path=os.path.join(base_dir, "geographical_features.csv")
slope_path=os.path.join(base_dir, "slope.csv")
survivor_path=os.path.join(base_dir, "survivor.csv") 
findings_path=os.path.join(base_dir, "findings.csv")
report_info_path=os.path.join(base_dir, "slope.csv")



# importing datasets
road_network = np.genfromtxt(road_network_path, delimiter=',')
important_cells = np.genfromtxt(important_cells_path, delimiter=',')
slope = np.genfromtxt(slope_path, delimiter=',')
survivors = np.genfromtxt(survivor_path, delimiter=',')
findings = np.genfromtxt(findings_path, delimiter=',')
report_information = np.genfromtxt(report_info_path, delimiter=',')
cost=cost_amalgamation()


np.savetxt(data_dir, cost, delimiter=',')
print("Your data has been saved successfully.")