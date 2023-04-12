from models.OrderModels import Order


def order_helper(order: Order) -> dict:
    subtotal_list = [item.dish.price * item.quantity for item in order.order_items]
    total = sum(subtotal_list)
    return {
        "id": order.id,
        "date": order.order_date,
        "status": order.status,
        "is_active": order.is_active,
        "observations": order.observations,
        "on_site": order.on_site,
        "customer_name": order.customer_name,
        "dishes": [
            {
                "quantity": item.quantity,
                "dish": item.dish.name,
                "price": item.dish.price,
                "subtotal": item.dish.price * item.quantity
            }
            for item in order.order_items
        ],
        "total": total
    }


def orders_active(order: Order) -> dict:
    return {
        "id": order.id,
        "dishes": [
            {
                "item": f"{item.dish.name} - {item.quantity} - {order.status}"
            }
            for item in order.order_items
        ]
    }
