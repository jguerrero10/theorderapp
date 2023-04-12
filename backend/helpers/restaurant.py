from models.RestaurantModel import Restaurant


def restaurant_helper(restaurant: Restaurant) -> dict:
    return {
        "id": restaurant.id,
        "name": restaurant.name,
        "logo": restaurant.logo
    }