class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.galletas = []

    def __str__(self):
        galletas = []
        for _ in range(self.size):
            galletas.append("🍪")
        return "".join(
            galletas
        )  # Une todos los emojis de galleta en una cadena y devuélvela

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        for _ in range(n):
            self.galletas.append("🍪")

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        else:
            for _ in range(n):
                self.galletas.pop()

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError
        self._capacity = value

    @property
    def size(self):
        return len(self.galletas)


#
jarra = Jar()

#
print("Estado inicial de la jarra:", jarra)

#
jarra.deposit(5)
#
print("Estado de la jarra después de depositar 5 galletas:", jarra)

#
jarra.withdraw(2)

#
print("Estado de la jarra después de retirar 2 galletas:", jarra)

# 
print("Capacidad máxima de la jarra:", jarra.capacity)
print("Número actual de galletas en la jarra:", jarra.size)
