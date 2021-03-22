from items.furniture import Chair, CounterBar
from items.device import POS, Dishwasher
from items.tableware import Glass, Plate

class CounterBarManager:
    def __init__(self):
        self.items = []
    
    def buyEquip(self, item):
        self.items.append(item)
    
    def sortByWeight(self):
        bought_items = []
        self.items.sort(key=lambda item: item.weight, reverse=False)
        print(self.items)
        return bought_items

    def sortByPrice(self):
        bougth_items = []
        self.items.sort(key=lambda item: item.price, reverse=False)
        bougth_items = self.items
        return bougth_items

    def searchByItemMaterial(self, material = Glass):
        bought_items = []
        for item in self.items:
            if item.material == material:
                bought_items.append(item)
        self.items = bought_items
        return bought_items
