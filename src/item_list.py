class ItemList(list):
    """
    Class for list of library items.
    Methods:
        add_item(Item): adds library item to list
        remove_item(Item): removes library item from list
        get_item(title): returns item object from item title
        is_available(title): verify whether item is available for loan
        checkout(Item): check item out to library user
        return(title): return item to library from use
        number_of_items(): number of items in list
        fines_owed(): total fines owed on items in list
    """

    def add_item(self, item):
        """Input: item object. No return. Adds a library item to the list."""
        pass

    def remove_item(self, item):
        """Input: item object. No return. Removes a library item from the list."""
        pass

    def get_item_from_title(self, title):
        """Input: string of item title. Return: item object."""
        pass

    def get_item_from_id(self, item_id):
        """Input: item object address. Return: item object."""
        pass

    def get_item(self, item_id):
        """Input: string of item title OR item object id. Return: item object.
        Uses get_item_from_title if input is string and get_item_from_id if input is int."""

    def is_available(self, title):
        """Input: string of item title. Return boolean: is item with title available for loan?"""
        pass

    def return_item(self, title):
        """Input: string of item title. Return float: final fine owed on item.
        Check item back into library from user: remove item from item list, get final fine due on item, and tell
        item to clear checkout date."""
        pass

    def checkout(self, item):
        """Input: item object. No return.
        Check out library item to user: add item to item list, tell item to set checkout date"""
        pass

    def number_of_items(self):
        """Returns number of items in list (no parameters taken)."""
        pass

    def fines_owed(self):
        """Return float: total fines owed over all items in list. No parameters taken."""
