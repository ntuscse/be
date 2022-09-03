from be.api.v1.db.products import read_product
from be.api.v1.models.orders import OrderItem
from be.api.v1.models.cart import Cart, PriceModel


def generate_order_items_from_cart(cart: Cart):
    cart_order_items = []
    for i in cart.items:
        product = read_product(i.productId)
        if not product:
            raise Exception(f"productId {i.productId} could not be found")
        cart_order_items.append(
            OrderItem(
                id=product.id,
                name=product.name,
                price=product.price,
                images=product.images,
                sizes=product.sizes,
                productCategory=product.productCategory,
                isAvailable=product.isAvailable,
                quantity=i.quantity
            ))
    return cart_order_items


def calc_cart_value(cart_order_items: list[OrderItem]):
    subtotal = 0
    for i in cart_order_items:
        subtotal += i.price * i.quantity

    # handle promo code
    # promo = getPromo(promoCode) if cart.promoCode else None

    # discount_value = 0
    # if promo.target.type == 'cart':
    #     if promo.type == 'fixed_value':
    #         discount_value = promo.value
    #     elif promo.type == 'percentage':
    #         discount_value = promo.value * subtotal
    # if promo.target.type == 'product':
    #     discount_product_id = promo.target.product_id
    #     discount_product = next(item for item in items_products if item["productId"] == discount_product_id)
    #     if not discount_product:
    #         raise HTTPException(status_code=400, detail="Promo code can't be applied to any item in cart")
    #     if promo.type == 'fixed_value':
    #         item_discount_value = max(promo.value, discount_product.price)
    #
    #     elif promo.type == 'percentage':
    #         item_discount_value = promo.value * discount_product.price

    grand_total = subtotal

    return PriceModel(
        currency = 'sgd',
        subtotal = subtotal,
        discount = 0, # todo
        grandTotal = grand_total
    )
