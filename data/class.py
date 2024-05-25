class Room:
    def __init__(self, chairs):
        self.tables = 2
        self.board = 1
        self.chairs = chairs

    def withroom(self):
        return "we are in room"
apponix=Room(10)
print(apponix.chairs)
