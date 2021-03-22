from items.item import Item

class Furniture(Item):
    def __init__(self, item_type, country_manufacturer, price, material, weight, height, width, form):
        self.height = height
        self.width = width
        self.form = form
        super.__init__(self, item_type, country_manufacturer, price, material, weight)

class Chair(Furniture):
    def __init__(self, comfort, item_type, country_manufacturer, price, material, weight, height, width, form):
        self.comfort = comfort
        super().__init__(item_type, country_manufacturer, price, material, weight, height, width, form)

class CounterBar(Furniture):
    def __init__(self, decoration, item_type, country_manufacturer, price, material, weight, height, width, form):
        self.decoration = decoration
        super.__init__(self, item_type, country_manufacturer, price, material, weight, height, width, form)         