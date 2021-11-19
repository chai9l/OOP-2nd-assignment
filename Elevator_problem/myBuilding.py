from myelevator import myElevator


class myBuilding:

    def __init__(self, min_floor: int, max_floor: int):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elevators = []

    def __add__(self, other):
        self.elevators.append(other)

    def add_elevator(self, other: myElevator):
        self.elevators.append(other)

    def get_min_floor(self) -> int:
        return self.min_floor

    def set_min_floor(self, min_floor: int):
        self.min_floor = min_floor

    def get_max_floor(self) -> int:
        return self.max_floor

    def set_max_floor(self, max_floor: int):
        self.max_floor = max_floor

    def get_elevators(self) -> []:
        return self.elevators

    def __getitem__(self, item):
        return item

    def __iter__(self):
        return self.elevators



