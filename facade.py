class CheckoutProcess:
    def __init__(self, order):
        self._order = order

    def set_shipping_address(address):
        self._order._shipping_address = address

    def set_payment_method(payment_method):
        self._order._payment_method = payment_method

    def review_order():
        print(f"Order contains {order._items}")
        print(f"Shipping address is {order._shipping_address}")
        print(f"Payment method is {order._payment_method}")

    def place_order():
        order.confirm()


class OneClickCheckout:
    def __init__(self, order, default_address, default_payment):
        self._checkout_process = CheckoutProcess(order)
        self._default_address = default_address
        self._default_payment = default_payment

    def click():
        self._checkout_process.set_shipping_address(default_address)
        self._checkout_process.set_payment_method(default_payment)
