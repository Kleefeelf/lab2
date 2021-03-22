from items.item import Item

class Tableware(Item):
    def __init__(self, design, brand,  item_type, country_manufacturer, price, material, weight):
        self.design = design
        self.brand = brand
        super.__init__(self, item_type, country_manufacturer, price, material, weight)

class Glass(Tableware):
    def __init__(self, volume, opacity, design, brand,  item_type, country_manufacturer, price, material, weight):
        self.volume = volume
        self.opacity = opacity
        super.__init__(self,  item_type, design, brand, country_manufacturer, price, material, weight)

class Plate(Tableware):
    def __init__(self, diameter, depth, design, brand,  item_type, country_manufacturer, price, material, weight):
        self.diameter = diameter
        self.depth  = depth
        super.__init__(self, design, brand,  item_type, country_manufacturer, price, material, weight)