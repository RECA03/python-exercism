"""Functions to manage a users shopping cart items."""


#from turtle import update


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    #count the new items and create their tuples
    for item in set(items_to_add):
        item_count = (item, items_to_add.count(item))
        if item not in current_cart:
            current_cart.setdefault(*item_count)
        else:
            current_cart[item] += item_count[-1]
    
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    cart = {}

    return cart.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)

    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    fulfillment_cart = {}
    aisle_mapping_info = aisle_mapping.copy()
    for item in cart:
        aisle_mapping_info[item].insert(0, cart[item])
        fulfillment_cart[item] = aisle_mapping_info[item]

    return dict(reversed(sorted(fulfillment_cart.items())))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    updated_item_counts = {}
    for item in fulfillment_cart:
        new_item_info = store_inventory[item].copy()
        new_item_info[0] = store_inventory[item][0] - fulfillment_cart[item][0]
        print(new_item_info)
        if new_item_info[0] == 0:
            new_item_info[0] = "Out of Stock"
        updated_item_counts[item] = new_item_info
    
    store_inventory |= updated_item_counts

    return store_inventory