# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room, inventory):
          self.name = name
          self.current_room = starting_room
          self.inventory = []

    def take(self, item):
        for i in self.current_room.items_in_room:
            if item.lower() == i.name.lower():
                self.inventory.append(i)
                self.current_room.items_in_room.remove(i)
                i.on_take()  
            else:
                print('Unable to add item to inventory')
               
    def drop(self, item):
        for i in self.inventory:
            if item.lower() == i.name.lower():
                self.inventory.remove(i)
                i.on_drop()
                print(f'{item} has been removed from inventory!')
            else:
                print()

    def getInventory(self):
            if len(self.inventory) == 0:
                return "You are carrying nothing"
            output = "You are carrying a "
            if len(self.inventory) == 1:
                output += self.inventory[0].name
                return output
            else: 
                for i in self.inventory:
                    if i == self.inventory[-1]:
                        output += "and a " + i.name
                        if len(self.inventory) == 2:

                            output = output.replace(",","")
                        return output 
                    output += i.name + ", "