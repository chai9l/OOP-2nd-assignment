
from myCall import *


class myElevator:

    def __init__(self, id: int, speed: float, close_time: float, open_time: float, start_time: float, stop_time: float,
                 minfloor: int, maxfloor: int):
        self.id = int(id)
        self.speed = float(speed)
        self.close_time = float(close_time)
        self.open_time = float(open_time)
        self.start_time = float(start_time)
        self.stop_time = float(stop_time)
        self.min_floor = int(minfloor)
        self.max_floor = int(maxfloor)
        self.call_list = []  # going to hold myCall list


    def is_inrange(self, current, one, two):
        if one < two:
            return one <= current <= two
        else:
            return two <= current <= one

    def calc_time_all_calls(self,call): # calculating the entire path of the elevator with the new call we might want to add
        # timescale = 1/self.speed;
        time = 0
        pos = 0.0
        door_timer = 0
        elev_state = 0  # elev_state = 0 LEVEL, 1 = UP, -1 = DOWN
        active_calls = []
        j = 0
        stop_request = False
        self.call_list.append(call) # adding the call to the list so we can run the simulation on it
        call.state = -1 # state = -1 is GOING2SRC , state = 1 is GOINGTODEST , state = 0 , ARIIVEDATDEST
        while call.state != 0:
            # moving from elevator call list to a simulation list
            if len(self.call_list) > j:
                if self.call_list[j].time_received <= time:
                    self.call_list[j].state = -1
                    active_calls.append(self.call_list[j])
                    j += 1
            # checking all of the active calls to see if we need to remove one that is done
            for c in active_calls:
                if c.state == -1 and self.is_inrange(pos, c.src, c.src + self.speed*elev_state):
                    c.state = 1
                    stop_request = True
                    pos = c.src

                if c.state == 1 and self.is_inrange(pos, c.dest, c.dest + self.speed*elev_state):
                    c.state = 0
                    stop_request = True
                    pos = c.dest
                    active_calls.remove(c)
            # handle elevator
            if elev_state == 0: # checking the first direction that the elevator is going
                if len(active_calls) > 0:
                    if pos < active_calls[0].src:
                        elev_state = 1
                    if pos > active_calls[0].src:
                        elev_state = -1

            if stop_request == False: # stop_reuqest when elevator is moving we want to change position
                if elev_state == 1:
                    pos += self.speed

                if elev_state == -1:
                    pos -= self.speed
            else:                       # else we want the elevator to stop moving so we open a new timer for the door to calc the time of the doors opening and closing
                door_timer += 1
                if door_timer >= self.open_time + self.close_time:
                    stop_request = False
                    door_timer = 0
                    if len(active_calls) != 0:  # we want to check if we need to keep going the same direction or oppiste direction
                        if elev_state == 1:
                            elev_state = -1
                            for c in active_calls:
                                if (c.state == -1 and pos < c.src) or (c.state == 1 and pos < c.dest):
                                    elev_state = 1
                        if elev_state == -1:
                            elev_state = 1
                            for c in active_calls:
                                if (c.state == -1 and pos > c.src) or (c.state == 1 and pos > c.dest):
                                    elev_state = -1
                        if elev_state == 0:
                            if pos < active_calls[0].dest:
                                elev_state = 1
                            if pos > active_calls[0].dest:
                                elev_state = -1

                    else:
                        elev_state = 0
            time += 1

        self.call_list.remove(call) # removing the call that we simulated on
        return time - call.time_received # returning the time it took to calc the entire path - the call arrival time gives us the time of the path it took the elevator to reach the dest of the given call

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int):
        self.id = id

    def get_speed(self) -> float:
        return self.speed

    def set_speed(self, speed: float):
        self.speed = speed

    def get_close_time(self) -> float:
        return self.close_time

    def set_close_time(self, close_time: float):
        self.close_time = close_time

    def get_open_time(self) -> float:
        return self.open_time

    def set_open_time(self, open_time: float):
        self.open_time = open_time

    def get_start_time(self) -> float:
        return self.start_time

    def set_start_time(self, start_time: float):
        self.start_time = start_time

    def get_stop_time(self) -> float:
        return self.stop_time

    def set_stop_time(self, stop_time: float):
        self.stop_time = stop_time

    def __getitem__(self, item):
        return item

    def __str__(self):
        return f"Elevetor : Id: {self.id}, Speed: {self.speed}, CloseTime: {self.close_time}, OpenTime: {self.open_time}, StarTime: {self.start_time},StopTime: {self.stop_time}"

    def __repr__(self):
        return f"Elevetor : Id: {self.id}, Speed: {self.speed}, CloseTime: {self.close_time}, OpenTime: {self.open_time}, StarTime: {self.start_time},StopTime: {self.stop_time} "
