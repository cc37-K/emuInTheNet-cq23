import sys
import math
from object_types import ObjectTypes

class Navigator:
    def __init__(self, game):
        self.game = game
        self.boundaries = []
        self.walls = set()
        self.powerups = set()
        self.path_call_counter = 0

    def cal_dist(self):
        your_pos = self.game.objects[self.game.tank_id]["position"]
        enemy_pos = self.game.objects[self.game.enemy_tank_id]["position"]
        return math.sqrt((your_pos[0] - enemy_pos[0]) ** 2 + (your_pos[1] - enemy_pos[1]) ** 2)

    def cal_angle(self):
        enemy_position = self.get_enemy()["position"]
        current_position = self.game.get_my_tank()["position"]
        angle = 0
        if enemy_position[0] - current_position[0] != 0:  # Avoid division by zero
            angle = math.atan2((enemy_position[1] - current_position[1]),
                               (enemy_position[0] - current_position[0])) * 180 / math.pi

        dodge_angle = (angle + 90) % 360
        return dodge_angle

    def get_enemy(self):
        return self.game.objects[self.game.enemy_tank_id]

    def detect_boundary(self):
        closing_boundaries = []

        for game_object in self.game.objects.values():
            if game_object["type"] == ObjectTypes.CLOSING_BOUNDARY.value:
                closing_boundaries.append(game_object['position'])

        y_lower_bound = closing_boundaries[0][1][1]
        y_upper_bound = closing_boundaries[0][0][1]
        x_lower_bound = closing_boundaries[0][1][0]
        x_upper_bound = closing_boundaries[0][2][0]

        return [y_lower_bound, y_upper_bound,
                x_lower_bound, x_upper_bound]

    def get_move(self):
        current_dist = self.cal_dist()

        safe_distance = 100

        action = {}
        if current_dist <= safe_distance:  # case distance is close enough that need to rotate
            angle = self.cal_angle()
            action = {
                "move": angle
            }
        else:
            if self.path_call_counter != 0:
                self.path_call_counter -= 1
            else:
                self.path_call_counter = 2
                action = {
                    "path": self.get_enemy()["position"]
                }
        return action
