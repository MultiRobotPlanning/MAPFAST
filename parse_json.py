import os
import json

def parse_json(map_file : str, agent_file : str):
    # read map json
    if os.path.exists(map_file):
        map_details = json.load(open(map_file))
    else:
        raise FileNotFoundError(map_file + ' not found!')
    # read agent json
    if os.path.exists(agent_file):
        agent_details = json.load(open(agent_file))
    else:
        raise FileNotFoundError(agent_file + ' not found!')
    
    prefix = "new_"
    map_ext = ".map"
    scene_ext = ".scen"
    map_dicts = []
    scene_names = []
    starts_goals = []

    for key, val in map_details.items():
        # remove "new_" prefix
        if key.startswith(prefix):
            key = key[len(prefix):]

        assert ("-random" in key or "-even" in key), "random/even not in key"

        if "-random" in key:
            partition = key.partition("-random")
            map_name = partition[0]
            scene_num = partition[2].partition("_")
            scene_name = partition[0] + partition[1] + scene_num[0]

        elif "-even" in key:
            partition = key.partition("-even")
            map_name = partition[0]
            scene_num = partition[2].partition("_")
            scene_name = partition[0] + partition[1] + scene_num[0]

        map_name += map_ext
        map = dict()
        map["name"] = map_name
        map["dim"] = val["mp_dim"]
        map["num_agents"] = val["no_agents"]
        map_dicts.append(map)

        scene_name += scene_ext
        scene_names.append(scene_name)

    for val in agent_details.values():
        starts_goals.append(val.copy())
    
    return map_dicts, scene_names, starts_goals