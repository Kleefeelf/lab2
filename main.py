from CounterBarManager import CounterBarManager
from items.furniture import Chair, CounterBar
from items.device import POS, Dishwasher
from items.tableware import Glass, Plate
from items.country import Country

if __name__ == "__main__":
    bar = CounterBarManager()
    bar.buyEquip([
        Chair("Zruchno", "Krislo", Country.China, 150, "Derevo", 250, 50, 25, "Zaokruglena"),
        Dishwasher(50, 50, "Mitu posud", "Dish200", "Dishwasher", Country.Ukraine , 1500, "Zalizo", 25),
        Glass(10, "Prozoriy","Gravirovka", "Ukrainski chashki", "Chashka", Country.USA, 150, "Glass", 150)
    ])

    print(bar)
    print(bar.searchByItemMaterial)
    print(bar.sortByPrice)
    print(bar.sortByWeight)