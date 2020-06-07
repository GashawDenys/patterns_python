class Product:
    def show(self):
        raise NotImplementedError()


class Iphone(Product):
    def show(self):
        print('Iphone added on the website')


class Macbook(Product):
    def show(self):
        print('Macbook added on the website')


class Store:
    # factory method
    def add_product(self, name):
        raise NotImplementedError


class MyStore(Store):
    def add_product(self, name):
        if name == 'iphone':
            return Iphone()
        elif name == 'macbook':
            return Macbook()
        else:
            return Product()


store = MyStore()
store.add_product('iphone').show()
store.add_product('macbook').show()
try:
    store.add_product('airpods').show()
except:
    print("NotImplementedError")
