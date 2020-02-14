# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room, inventory):
          self.name = name
          self.current_room = starting_room
          self.items_inventory = inventory

    def get_item(self, item):
        for i in self.current_room.items_in:
            print('Picking up item', item)

            if item == i.item:
                self.items_inventory.append(i)
                self.current_room.items_in.remove(i)
                i.on_get()  
            else:
                print('Unable to add item to inventory')
               
    def remove_item(self, item):
        for f in self.items_inventory:
            if (item == f.item):
                self.items_inventory.remove(f)
                f.on_remove()
                print(f'{item} has been removed from inventory!')
            else:
                print('Unable to remove item')