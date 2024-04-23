import pandas as pd
import numpy as np
import os

base_dir = '/home/keithmartin/Documents/masters_in_AI/Semester_3/Thesis/Code/thesis_project/New_Everything/Data1'
data_dir = 'static_cost_map.csv'



#applies cost function on static features: y=0.4(road_network) + 0.4 (important_cells) + 0.2(slope)
def static_cost_calculation(road_network, important_cells, slope):
    static_cost_map = (0.4*road_network) + (0.4*important_cells) + (0.2*slope)
    return static_cost_map




#defining paths to datasets
road_network_path=os.path.join(base_dir, "road_network.csv")
important_cells_path=os.path.join(base_dir, "geographical_features.csv")
slope_path=os.path.join(base_dir, "slope.csv")



# importing datasets
road_network = np.genfromtxt(road_network_path, delimiter=',')
important_cells = np.genfromtxt(important_cells_path, delimiter=',')
slope = np.genfromtxt(slope_path, delimiter=',')
static_cost=static_cost_calculation(road_network, important_cells, slope)


np.savetxt(data_dir, static_cost, delimiter=',')
print("Your data has been saved successfully.")