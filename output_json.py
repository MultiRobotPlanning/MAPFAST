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

    data[map_name] = output_dict.copy()

    # convert into JSON:
    json_object = json.dumps(data)

    # the result is a JSON string:
    # print(json_object )

    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

    return
