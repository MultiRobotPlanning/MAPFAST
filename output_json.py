import json
# x = {}
with open("sample.json", "r") as f:
  data = json.load(f)
# returns JSON object as 
# a dictionary

print(data)

map_name = "new_brc202d-even-4_1_40_agents.yaml"
best_solver = "EECBS"
eecbs_time = 1.2
eecbs_cost = 2.1
ecbs_time = 14.4
ecbs_cost = 41.2
pbs_time = 4.2
pbs_cost = 12.2
# a Python object (dict):
# x = {
#   map_name: {"SOLVER": best_solver, "eecbs_time": eecbs_time, "eecbs_cost": eecbs_cost, "ecbs_time": ecbs_time, "ecbs_cost": ecbs_cost, "pbs_time": pbs_time, "pbs_cost": pbs_cost}
# }
data[map_name] = {"SOLVER": best_solver, "eecbs_time": eecbs_time, "eecbs_cost": eecbs_cost, "ecbs_time": ecbs_time, "ecbs_cost": ecbs_cost, "pbs_time": pbs_time, "pbs_cost": pbs_cost}

# convert into JSON:
json_object  = json.dumps(data)

# the result is a JSON string:
# print(json_object ) 

with open("sample.json", "w") as outfile:
    outfile.write(json_object)