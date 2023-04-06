import os
import subprocess
from parse_json import parse_json
from output_json import output_json
from timeit import default_timer as timer

map_file = "json_files/solved_map_details.json"
agent_file = "json_files/solved_agent_details.json"
map_dicts, scene_names, starts_goals = parse_json(map_file, agent_file)

# scene files directory
scene_dir = "scenes/"
if not os.path.exists(scene_dir):
    os.mkdir(scene_dir)

# planner output directory
planner_dir = "planner_outputs/"
if not os.path.exists(planner_dir):
    os.mkdir(planner_dir)

# current working directory
cwd = os.getcwd() + "/"
# map directory
map_dir = cwd + "mapf-map/"


def write_to_scene(scene_file: str, map_dict: dict, starts_goals: dict):
    starts = starts_goals["starts"]
    goals = starts_goals["goals"]
    bucket = 1
    tab = "\t"
    optimal_length = 1.0
    with open(scene_file, "w+") as file:
        file.writelines(["version 1\n"])
        for start, goal in zip(starts, goals):
            # bucket number
            line = str(bucket) + tab
            # map name
            line += map_dict["name"] + tab
            # map width
            line += str(map_dict["dim"][0]) + tab
            # map height
            line += str(map_dict["dim"][1]) + tab
            # start-x, start-y
            line += str(start[0]) + tab + str(start[1]) + tab
            # goal-x, goal-y
            line += str(goal[0]) + tab + str(goal[1]) + tab
            # optimal length
            line += str(optimal_length) + "\n"

            file.writelines([line])


# main loop
planners = ["ecbs", "eecbs", "pbs"]
subprocess_timeout = 300
planner_timeout = 300
suboptimality = 1.2
for idx in range(0,len(map_dicts)):
    print(str(idx) + '/' + str(len(map_dicts)))
    map_dict = map_dicts[idx]
    scene_name = scene_names[idx]
    scene_file = scene_dir + scene_names[idx]

    # create scene file
    write_to_scene(scene_file, map_dict, starts_goals[idx])

    # dict to pass to output script
    output_dict = dict()
    min_time = planner_timeout
    best_solver = "EECBS" 
    # call planners
    for planner in planners:
        # global path required since output folder is outside planning directory
        planner_file = cwd + planner_dir + planner
        planner_exec = "eecbs" if (planner == "eecbs" or planner == "ecbs") else planner
        planner_call = []
        # executable name
        planner_call.append("./" + planner_exec)
        # map name
        planner_call.extend(["-m", map_dir + map_dict["name"]])
        # scene name
        planner_call.extend(["-a", cwd + scene_file])
        # output csv
        planner_call.extend(["-o", planner_file + ".csv"])
        # output paths
        planner_call.extend(["--outputPaths=" + planner_file + ".txt"])
        # number of agents
        planner_call.extend(["-k", str(map_dict["num_agents"])])
        # timeout
        planner_call.extend(["-t", str(planner_timeout)])

        if planner == "eecbs" or planner == "ecbs":
            planner_call.extend(["--suboptimality=" + str(suboptimality)])
            planner_cwd = cwd + "EECBS/"
        else:
            planner_cwd = cwd + "PBS/"

        if planner == "ecbs":
            # change high level search for ECBS
            planner_call.extend(["--highLevelSolver=" + "A*eps"])
        try:
            process = subprocess.run(
                planner_call, cwd=planner_cwd, timeout=subprocess_timeout, stdout=subprocess.PIPE
            )
            planner_success = process.returncode
        except subprocess.TimeoutExpired: 
            print("caught subprocess timeout error")
            planner_success = -1

        if(planner_success == 1):
            planner_output = (process.stdout).decode()
            # print(planner_output)
            planner_output = planner_output.split(':')[1]
            planner_output = planner_output.split(',')
            time_taken = float(planner_output[2])
            cost = float(planner_output[1])
            output_dict[planner.upper()] = time_taken
            output_dict[planner + "_cost"] = cost
            # check best solver
            if(time_taken < min_time): # TODO: Add a cost criteria for best solver
                best_solver = planner.upper()
                min_time = time_taken
        else:
            output_dict[planner.upper()] = -1
            output_dict[planner + "_cost"] = -1

    map_name = map_dict["filename"]
    output_dict["SOLVER"] = best_solver
    # call output script
    output_json(map_name, output_dict)
    # break
