import json
import os


# def output_json(map_name: str, best_solver: str, eecbs_time: float, eecbs_cost: float, ecbs_time: float, ecbs_cost: float, pbs_time: float, pbs_cost: float):
def output_json(map_name: str, output_dict : dict):
    data = {}
    if not os.path.exists("sample.json"):
        json_object = json.dumps(data)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

    with open("sample.json", "r") as f:
        data = json.load(f)
    # returns JSON object as
    # a dictionary

    # print(data)

    # map_name = "new_brc202d-even-4_1_40_agents.yaml"
    # best_solver = "EECBS"
    # eecbs_time = 1.2
    # eecbs_cost = 2.1
    # ecbs_time = 14.4
    # ecbs_cost = 41.2
    # pbs_time = 4.2
    # pbs_cost = 12.2
    # a Python object (dict):
    # x = {
    #   map_name: {"SOLVER": best_solver, "eecbs_time": eecbs_time, "eecbs_cost": eecbs_cost, "ecbs_time": ecbs_time, "ecbs_cost": ecbs_cost, "pbs_time": pbs_time, "pbs_cost": pbs_cost}
    # }

    data[map_name] = output_dict.copy()

    # data[map_name] = {
    #     "SOLVER": best_solver,
    #     "EECBS": eecbs_time,
    #     "eecbs_cost": eecbs_cost,
    #     "ECBS": ecbs_time,
    #     "ecbs_cost": ecbs_cost,
    #     "PBS": pbs_time,
    #     "pbs_cost": pbs_cost,
    # }

    # convert into JSON:
    json_object = json.dumps(data)

    # the result is a JSON string:
    # print(json_object )

    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

    return
