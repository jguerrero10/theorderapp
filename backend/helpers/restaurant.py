from models.RestaurantModels import Restaurant


def restaurant_helper(restaurant: Restaurant) -> dict:
    return {
        "id": restaurant.id,
        "name": restaurant.name,
        "logo": restaurant.logo,
        "dishes": [
            {
                "id": dish.id,
                "name": dish.name,
                "description": dish.description,
                "price": dish.price
            }
            for dish in restaurant.dishes
        ]
    }
