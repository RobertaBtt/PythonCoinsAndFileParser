import json
from typing import List


class Beacon:

    @staticmethod
    def deserialize_json(file_path: str) -> List[str]:
        json_elements = []
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    line = line[line.index("{"):line.index("}")+1]
                    json_elements.append(json.loads(line))
                except Exception as e:
                    pass

        return json_elements


    @staticmethod
    def group_by_beacon(json_list: List[str], antenna_ids: List[int]) -> json:
        groups = {}
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
