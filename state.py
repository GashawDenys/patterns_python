class ProductStateBase(object):
    def get_location(self):
        raise NotImplementedError()


class ProductInStockState(ProductStateBase):
    def get_location(self):
        return 'In stock'


class ProductDeliveringState(ProductStateBase):
    def get_location(self):
        return "Is delivering"


class ProductDeliveredState(ProductStateBase):
    def get_location(self):
        return "Is delivered"


class Product(object):
    def __init__(self):
        self._current_state = None
        self._states = self.get_states()

    def get_states(self):
        return [ProductInStockState(), ProductDeliveringState(), ProductDeliveredState()]

    def next_state(self):
        if self._current_state is None:
            self._current_state = self._states[0]
        else:
            index = self._states.index(self._current_state)
            if index < len(self._states) - 1:
                index += 1
            else:
                index = 0
            self._current_state = self._states[index]
        return self._current_state

    def order(self):
        state = self.next_state()
        print(state.get_location())


product = Product()
[product.order() for i in range(3)]
