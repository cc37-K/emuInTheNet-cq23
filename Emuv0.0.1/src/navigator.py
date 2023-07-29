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
        return math.sqrt((your_pos[0] - enemy_pos[0]) ** 2 + (your_pos[1] - enemy_pos[1]) ** 2)

    def cal_angle(self):
        enemy_position = self.get_enemy()["position"]
        current_position = self.game.get_my_tank()["position"]
        angle = math.atan2((enemy_position[1] - current_position[1]),
                           (enemy_position[0] - current_position[0])) * 180 / math.pi
        dodge_angle = angle + 90
        return dodge_angle

    def get_enemy(self):
        return self.game.objects[self.game.enemy_tank_id]

    def post_move(self):
        current_dist = self.cal_dist()
        print(f"path:{current_dist}", file=sys.stderr)

        if current_dist <= 200:  # case distance is close enough that need to rotate
            print(f"move_angle:{self.cal_angle()}\n move_dist:{current_dist}", file=sys.stderr)
            return {
                "move": self.cal_angle()
            }
        else:
            if self.path_call_counter != 0:
                self.path_call_counter -= 1
            if self.path_call_counter == 0:
                self.path_call_counter = 2
                return {
                    "path": self.get_enemy()["position"]
                }
