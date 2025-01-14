from unittest.mock import NonCallableMagicMock


class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not item in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            if getattr(item, 'category') == category:
                items_list.append(item)
        return items_list
    
    def swap_items(self, vendor1, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor1.inventory:
            return False
        self.remove(my_item)
        vendor1.add(my_item)
        vendor1.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, vendor1):
        if len(self.inventory) == 0 or len(vendor1.inventory) == 0:
            return False
        return self.swap_items(vendor1, self.inventory[0], vendor1.inventory[0])
        
    def get_best_by_category(self, category):
        best_item_by_category = 0
        best_item = None
        for item in self.inventory:
            if item.category == category:
                if item.condition > best_item_by_category:
                    best_item_by_category = item.condition
                    best_item = item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best == None or their_best == None:
            return False
        self.swap_items(other, my_best, their_best)
        return True