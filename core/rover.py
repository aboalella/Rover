class Rover:

    def __init__(self):
        self.current_state = "0:0:N"

    def __move_r(self, current_state: str):
        next_direction = ""
        direction = current_state[4]
        if direction == "N":
            next_direction = "E"
        if direction == "E":
            next_direction = "S"
        if direction == "S":
            next_direction = "W"
        if direction == "W":
            next_direction = "N"
        other_points = current_state[0:4]
        return other_points + next_direction

    def __move_l(self, current_state):
        next_direction = ""
        direction = current_state[4]
        if direction == "N":
            next_direction = "W"
        if direction == "W":
            next_direction = "S"
        if direction == "S":
            next_direction = "E"
        if direction == "E":
            next_direction = "N"
        other_points = current_state[0:4]
        return other_points + next_direction

    def __move_m(self, current_state):
        x_axis = int(current_state[0])
        y_axis = int(current_state[2])
        direction = current_state[4]
        if direction in ["N", "S"]:
            y_axis = y_axis + 1
        if direction in ["E", "W"]:
            x_axis = x_axis + 1
        return f"{x_axis}:{y_axis}:{direction}"

    def rover_move(self, movements: str):
        next_state = ""
        for move in movements:
            if move == "R":
                next_state = self.__move_r(self.current_state)
            if move == "L":
                next_state = self.__move_l(self.current_state)
            if move == "M":
                next_state = self.__move_m(self.current_state)
            self.current_state = next_state
        return self.current_state
