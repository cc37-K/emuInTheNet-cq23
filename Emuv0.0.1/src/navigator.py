import sys
import numpy as np
from object_types import ObjectTypes
import math

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
        your_pos = self.game.objects[self.game.tank_id]["position"]
        enemy_pos = self.game.objects[self.game.enemy_tank_id]["position"]
        rad = (your_pos[1] - enemy_pos[1])/(your_pos[0] - enemy_pos[0])
        angle = np.rad2deg(rad)
        return angle + 90

    def get_enemy(self):
        return self.game.objects[self.game.enemy_tank_id]

    def post_move(self):
        current_dist = self.cal_dist()
        if current_dist > 100:
            print(f"path:{current_dist}", file=sys.stderr)
            if self.path_call_counter == 0:
                self.path_call_counter = 2
                return {
                    "path": self.get_enemy()["position"]
                }
            else:
                self.path_call_counter -= 1
        else:
            print(f"move_angle:{self.cal_angle()}\n move_dist:{current_dist}", file=sys.stderr)
            return {
                "move": self.cal_angle()
            }