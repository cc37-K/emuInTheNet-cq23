class Wall:
    def __init__(game_type,position,destructable=0):
        self.destructable = destructable
        self.position = position
        if self.destructable == 0:
            self.game_type = 3
        else:
            self.game_type = 4
        
