import math

class Shooter:
    def __init__(self, game):
        self.game = game

    # Calculate angle and shoot to the location
    def aimed_shoot(self):
        current_position = self.game.objects[self.game.tank_id]["position"]
        enemy_position = self.game.objects[self.game.enemy_tank_id]["position"]
        angle = 0
        if enemy_position[0] - current_position[0] != 0:  # Avoid division by zero
            angle = math.atan2((enemy_position[1] - current_position[1]),(enemy_position[0] - current_position[0]))*180/math.pi
            angle = angle % 360
        return {
            "shoot": angle
        }
