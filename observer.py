from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, message):
        pass


class Observable(metaclass=ABCMeta):
    def __init__(self):
        self.observers = []

    def register(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)


class Store(Observable):
    def add_news(self, news):
        self.notify_observers(news)


class Customer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} получил новость о том что {}'.format(self.name, message))


if __name__ == '__main__':
    newspaper = Store()
    newspaper.register(Customer('Денис'))
    newspaper.register(Customer('Владислав'))
    newspaper.register(Customer('Кирилл'))
    newspaper.add_news('на вебсайте добавлена новая категория товаров')
