from items.item import Item

class Device(Item):
    def __init__(self, device_purpose, name, item_type, country_manufacturer, price, material, weight):
        self.device_purpose = device_purpose
        self.name = name
        super.__init__(self, item_type, country_manufacturer, price, material, weight)

class Dishwasher(Device):
    def __init__(self, capacity, noise_level, device_purpose, name, item_type, country_manufacturer, price, material, weight):
        self.capacity = capacity
        self.noise_level = noise_level
        super.__init__(device_purpose, name, item_type, country_manufacturer, price, material, weight)

class POS(Device):
    def __init__(self, os_type, display_type, ram, device_purpose, name, item_type, country_manufacturer, price, material, weight):
        self.os_type = os_type
        self.display_type = display_type
        self.ram = ram
        super.__init__(device_purpose, name, item_type, country_manufacturer, price, material, weight)