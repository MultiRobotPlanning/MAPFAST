import os
import json

yaml_file = "sample.json"
map_file = "json_files/solved_map_details.json"
agent_file = "json_files/solved_agent_details.json"

yaml_file_out = "json_files/solved_yaml_details_run1.json"
map_file_out = "json_files/solved_map_details_run1.json"
agent_file_out = "json_files/solved_agent_details_run1.json"

yaml_details = json.load(open(yaml_file))
map_details = json.load(open(map_file))
agent_details = json.load(open(agent_file))

prefix = "new_"

yaml_details_out = yaml_details.copy()
map_details_out = map_details.copy()
agent_details_out = agent_details.copy()

for key, val in map_details.items():
    new_name = key
    if key.startswith(prefix):
        add_prefix = True
        new_name = key[len(prefix):]
    if new_name not in yaml_details_out.keys():
        map_details_out.pop(key)
        agent_details_out.pop(key)
        continue
    run_details = yaml_details_out[new_name]
    if (run_details["ECBS"] == -1 and run_details["EECBS"] == -1 and run_details["PBS"] == -1):
        yaml_details_out.pop(new_name)
        map_details_out.pop(key)
        agent_details_out.pop(key)    
        continue
    yaml_details_out[key] = yaml_details_out.pop(new_name)
    # yaml_details_out[key]["LNS2"] = -1
    yaml_details_out[key].pop("ecbs_cost")
    yaml_details_out[key].pop("eecbs_cost")
    yaml_details_out[key].pop("pbs_cost")


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
