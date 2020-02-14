# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomName, description, items):
        self.roomName = roomName
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items_in_room = items