class myCall:

    def __init__(self, time_received: float, src: int, dest: int,allocated_to: int):
        self.src = int(src)
        self.dest = int(dest)
        self.time_received = float(time_received)
        self.allocated_to = int(allocated_to)
        self.state = -1

    def calc_length(self):
        return abs(self.src - self.dest)

    def get_src(self) -> int:
        return self.src

    def get_dest(self) -> int:
        return self.dest

    def get_time_received(self) -> float:
        return self.time_received

    def get_allocated_to(self) -> int:
        return self.allocated_to

    def set_src(self, src: int):
        self.src = src

    def set_dest(self, dest: int):
        self.dest = dest

    def set_time_received(self, time_received: float):
        self.time_received = time_received

    def set_allocated_to(self, pos: int):
        self.allocated_to = pos

    def __str__(self):
        return f"{self.time_received}, {self.src}, {self.dest},-1,{self.allocated_to}"

    def __repr__(self):
        return f"{self.time_received}, {self.src}, {self.dest},-1,{self.allocated_to}"

    def __getitem__(self, item):
        return item
