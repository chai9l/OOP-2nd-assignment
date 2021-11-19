import functools
import sys
import json
import csv

from myCall import *
from myelevator import myElevator
from myBuilding import *


class ElevatorAlgo:

    def load_buildings(self, file_name) -> myBuilding:
        global b
        try:
            with open(file_name, 'r') as j_file:
                json_arr = json.load(j_file)

            b = myBuilding(json_arr.get("_minFloor"), json_arr.get("_maxFloor"))
            for v in json_arr["_elevators"]:
                el = myElevator(v['_id'], v['_speed'], v['_closeTime'], v['_openTime'], v['_startTime'], v['_stopTime'],
                                v['_minFloor'], v['_maxFloor'])
                b.elevators.append(el)

        except IOError:
            print("Error")

        return b

    def load_calls(self, file_name) -> []:
        ret = []
        try:
            with open(file_name, 'r') as csv_reader:
                calls = list(csv.reader(csv_reader))
                for i in calls:
                    call = myCall(i[1], i[2], i[3], i[5])
                    ret.append(call)
                return ret

        except IOError:
            return "Error"

    def load_calls_like_file(self, file_name) -> []:
        ret = []
        try:
            with open(file_name, 'r') as csv_reader:
                calls = list(csv.reader(csv_reader))
                for i in calls:
                    ret.append(i)
                return ret

        except IOError:
            return "Error"

    def write_output(self, file_name, call):
        with open(file_name, 'r+') as csv_reader:
            calls = list(csv.reader(csv_reader))


    def allocate_elevators(self, b: json, call_file: str, out_put: str):
        algo = ElevatorAlgo()
        building = algo.load_buildings(b)
        elev = building.elevators
        calls = algo.load_calls(call_file)
        output = algo.load_calls_like_file(call_file)

        for c in calls:
            time = 100000000
            i = -1
            for e in elev:
                this_time = e.calc_time_all_calls(c)
                if (this_time < time):
                    time = this_time
                    i = e.id
            elev[i].call_list.append(c)
            c.allocated_to = i

        i = 0
        for x in output:
            x[5] = calls[i].allocated_to
            i += 1
        with open(out_put, 'w', newline="") as f:
            for x in output:
                writer = csv.writer(f)
                writer.writerow(x)
        print("------")
        print("Finished the Program")
        print("------")






algo = ElevatorAlgo()
algo.allocate_elevators('Ex1_Buildings/B5.json', 'Ex1_Calls/Calls_d.csv', 'Ex1_Calls/out_put_a.csv')
# algo.allocate_elevators(sys.argv[2], sys.argv[3], sys.argv[4])
# Ex1_Buildings/B3.json Ex1_Calls/Calls_b.csv Ex1_Calls/out_put_a.csv


