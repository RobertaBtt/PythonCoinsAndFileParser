from beacon import beacon
from pathlib import Path
import os
import bisect
from operator import itemgetter
import json
from typing import List
import pathlib

if __name__ == '__main__':
    groups = {}
    path = pathlib.Path().absolute().parent

    file_path = str(path) + "/input.json"
    json_list = beacon.Beacon().deserialize_json(file_path)
    groups={}
    antennaIds = [201, 202, 203, 204, 205, 206]

    def beacon_generator(json_list, antenna_ids):

        for beacon in json_list:
            key = str(beacon["BeaconId"]) + ", " + str(beacon["timestamp"])
            if key not in groups:

                # Re-initialize the values to the default
                values = [-135] * len(antenna_ids)

                # Change just the one with that antenna ID
                values[antenna_ids.index(beacon["ant_id"])] = beacon["dbm_ant"]

                # Assign to the current key
                groups[key] = values
            else:
                # Recover the status of the list of the current antenna
                values = groups[key]

                # replace just the current antenna ID
                values[antenna_ids.index(beacon["ant_id"])] = beacon["dbm_ant"]

                groups[key] = values

        return groups




groups=beacon_generator(json_list, antennaIds)
json_dictionary={}
json_list = []

for beacon, values_list in groups.items():
    beacon_dict = {}
    beacon_dict['beacon'] = beacon
    beacon_dict['vector'] = values_list
    print(beacon_dict)
    #json_list.append(beacon_dict)

#print(json.dumps(json_list))
