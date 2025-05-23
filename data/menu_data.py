from src.restaurant.menu import Menu

def get_default_menus():
    return {
    1: Menu(1, 'Brunch', '11:00', '16:00', {
        'pancakes': 7.50,
        'waffles': 9.00,
        'burger': 11.00,
        'home fries': 4.50,
        'coffee': 1.50,
        'espresso': 3.00,
        'tea': 1.00,
        'mimosa': 10.50,
        'orange juice': 3.50
    }),
    2: Menu(2, 'Early bird', '15:00', '18:00', {
        'salumeria plate': 8.00,
        'salad and breadsticks (serves 2, no refills)': 14.00,
        'pizza with quattro formaggi': 9.00,
        'duck ragu': 17.50,
        'mushroom ravioli (vegan)': 13.50,
        'coffee': 1.50,
        'espresso': 3.00,
    }),
    3: Menu(3, 'Dinner', '17:00', '23:00', {
        'crostini with eggplant caponata': 13.00,
        'caesar salad': 16.00,
        'pizza with quattro formaggi': 11.00,
        'duck ragu': 19.50,
        'mushroom ravioli (vegan)': 13.50,
        'coffee': 2.00,
        'espresso': 3.00,
    }),
    4: Menu(4, 'Kids', '11:00', '21:00', {
        'chicken nuggets': 6.50,
        'fusilli with wild mushrooms': 12.00,
        'apple juice': 3.00,
    }),
}
