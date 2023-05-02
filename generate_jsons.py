import os
import json

yaml_file1 = "sample.json"
yaml_file2 = "json_files/solved_yaml_details_run3.json"
map_file = "json_files/solved_map_details.json"
agent_file = "json_files/solved_agent_details.json"

yaml_file_out = "json_files/solved_yaml_details_run5.json"
map_file_out = "json_files/solved_map_details_run5.json"
agent_file_out = "json_files/solved_agent_details_run5.json"

yaml_details1 = json.load(open(yaml_file1))
yaml_details2 = json.load(open(yaml_file2))
map_details = json.load(open(map_file))
agent_details = json.load(open(agent_file))

# prefix = "new_"

# yaml_details_out = yaml_details2.copy()
yaml_details_out = {}
map_details_out = map_details.copy()
agent_details_out = agent_details.copy()

for key, val in map_details.items():
    if (key not in yaml_details1.keys()) and (key not in yaml_details2.keys()):
        map_details_out.pop(key)
        agent_details_out.pop(key)
        continue
    run_details1 = {} if (yaml_details1.get(key,-1) == -1) else yaml_details1[key]
    run_details2 = {} if (yaml_details2.get(key,-1) == -1) else yaml_details2[key]
    run_details = {}
    
    run_details["BCP"] = run_details1.get("BCP",-1)
    run_details["BCP_cost"] = run_details1.get("BCP_cost",-1)
    run_details["CBSH"] = run_details1.get("CBSH",-1)
    run_details["CBSH_cost"] = run_details1.get("cbsh_cost",-1)
    run_details["PBS"] = run_details2.get("PBS",-1)
    run_details["PBS_cost"] = run_details2.get("PBS_cost",-1)
    run_details["LNS"] = run_details2.get("LNS",-1)
    run_details["LNS_cost"] = run_details2.get("LNS_cost",-1)
    run_details["ECBS1_02"] = run_details2.get("ECBS1_02",-1)
    run_details["ECBS1_02_cost"] = run_details2.get("ECBS1_02_cost",-1)
    run_details["EECBS1_02"] = run_details2.get("EECBS1_02",-1)
    run_details["EECBS1_02_cost"] = run_details2.get("EECBS1_02_cost",-1)

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
