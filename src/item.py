class Item:
    def __init__(self, item, item_description):
        self.item = item
        self.item_description = item_description

    def on_get(self):
        print(f'{self.item} added to inventory. View inventory with by pressing [i]')

    def on_remove(self):
        print(f'{self.item} removed from inventory.')