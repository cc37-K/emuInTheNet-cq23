import sys
import numpy as np
from object_types import ObjectTypes
import math
import random

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
        # print(your_pos,file=sys.stderr)
        # print(enemy_pos,file=sys.stderr)
        return math.sqrt((your_pos[0] - enemy_pos[0])**2 + (your_pos[1] - enemy_pos[1])**2)

    def cal_angle(self):
        enemy_position = self.get_enemy()["position"]
        current_position = self.game.get_my_tank()["position"]
        x1 = current_position[0]
        y1 = current_position[1]
        x2 = enemy_position[0]
        y2 = enemy_position[1]
        dy = y2 - y1
        dx = x2 - x1
        angle = math.degrees(math.atan2(dy, dx))
        angle = angle if angle >= 0 else angle + 360  # Convert to range 0 to 360
        return angle


    def get_enemy(self):
        return self.game.objects[self.game.enemy_tank_id]

    def post_move(self):
        current_dist = self.cal_dist()
        if current_dist <= 140: # case distance is close enough that need to roatae
            print(f"move_angle:{self.cal_angle()}\n move_dist:{current_dist}", file=sys.stderr)
            return {
                "move": self.cal_angle()
            }
        print(f"path:{current_dist}", file=sys.stderr)
        if self.path_call_counter != 0:
            self.path_call_counter -= 1
        if self.path_call_counter == 0:
            self.path_call_counter = 2
            return {
                "path": self.get_enemy()["position"]
            }
