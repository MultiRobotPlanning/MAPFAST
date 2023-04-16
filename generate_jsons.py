import os
import json

yaml_file1 = "sample1.json"
yaml_file2 = "sample2.json"
yaml_file3 = "sample3.json"
map_file = "json_files/solved_map_details.json"
agent_file = "json_files/solved_agent_details.json"

yaml_file_out = "json_files/solved_yaml_details_run3.json"
map_file_out = "json_files/solved_map_details_run3.json"
agent_file_out = "json_files/solved_agent_details_run3.json"

yaml_details1 = json.load(open(yaml_file1))
yaml_details2 = json.load(open(yaml_file2))
yaml_details3 = json.load(open(yaml_file3))
map_details = json.load(open(map_file))
agent_details = json.load(open(agent_file))

prefix = "new_"

# yaml_details_out = yaml_details2.copy()
yaml_details_out = {}
map_details_out = map_details.copy()
agent_details_out = agent_details.copy()

for key, val in map_details.items():
    new_name = key
    if key.startswith(prefix):
        add_prefix = True
        new_name = key[len(prefix):]
    if (new_name not in yaml_details1.keys()) and (key not in yaml_details2.keys()) and (key not in yaml_details3.keys()):
        map_details_out.pop(key)
        agent_details_out.pop(key)
        continue
    run_details1 = yaml_details1[new_name]
    run_details2 = yaml_details2[key]
    run_details3 = yaml_details3[key]
    # if (run_details1["ECBS"] == -1 and run_details1["EECBS"] == -1 and run_details1["PBS"] == -1 and run_details2["ECBS"] == -1 and run_details2["EECBS"] == -1 and run_details2["LNS"] == -1 and run_details3["ECBS"] == -1 and run_details3["EECBS"] == -1):
    if (run_details1["PBS"] == -1 and run_details2["LNS"] == -1 and run_details3["ECBS"] == -1 and run_details3["EECBS"] == -1):
        # yaml_details_out.pop(new_name)
        map_details_out.pop(key)
        agent_details_out.pop(key)    
        continue
    run_details = {}
    # run_details["ECBS1_2"] = run_details1["ECBS"]
    # run_details["ECBS1_2_cost"] = run_details1["ecbs_cost"]
    # run_details["EECBS1_2"] = run_details1["EECBS"]
    # run_details["EECBS1_2_cost"] = run_details1["eecbs_cost"]
    run_details["PBS"] = run_details1["PBS"]
    run_details["PBS_cost"] = run_details1["pbs_cost"]
    # run_details["ECBS1_1"] = run_details2["ECBS"]
    # run_details["ECBS1_1_cost"] = run_details2["ecbs_cost"]
    # run_details["EECBS1_1"] = run_details2["EECBS"]
    # run_details["EECBS1_1_cost"] = run_details2["eecbs_cost"]
    run_details["LNS"] = run_details2["LNS"]
    run_details["LNS_cost"] = run_details2["lns_cost"]
    run_details["ECBS1_02"] = run_details3["ECBS"]
    run_details["ECBS1_02_cost"] = run_details3["ecbs_cost"]
    run_details["EECBS1_02"] = run_details3["EECBS"]
    run_details["EECBS1_02_cost"] = run_details3["eecbs_cost"]

    # costs = {}
    least_cost = float('inf')
    for planner, cost in run_details.items():
        if (planner[-(len("_cost")):] != "_cost"):
            continue
        if (cost != -1) and cost <= least_cost:
            if (cost == least_cost):
                if (run_details[planner[:-(len("_cost"))]] < run_details[best_planner]):
                    best_planner = planner[:-(len("_cost"))]
                continue
            least_cost = cost
            best_planner = planner[:-(len("_cost"))]
            # costs[planner[:-(len("_cost"))]] = cost
    # run_details["SOLVER"] = min(costs, key=costs.get)
    run_details["SOLVER"] = best_planner

    yaml_details_out[key] = run_details
    # yaml_details_out[key] = yaml_details_out.pop(new_name)
    # yaml_details_out[key]["LNS2"] = -1
    # yaml_details_out[key].pop("ecbs_cost")
    # yaml_details_out[key].pop("eecbs_cost")
    # yaml_details_out[key].pop("pbs_cost")
    


print(len(yaml_details_out))
print(len(map_details_out))
print(len(agent_details_out))

yaml_details_object = json.dumps(yaml_details_out)
with open(yaml_file_out, "w") as outfile:
    outfile.write(yaml_details_object)

map_details_object = json.dumps(map_details_out)
with open(map_file_out, "w") as outfile:
    outfile.write(map_details_object)

agent_details_object = json.dumps(agent_details_out)
with open(agent_file_out, "w") as outfile:
    outfile.write(agent_details_object)
