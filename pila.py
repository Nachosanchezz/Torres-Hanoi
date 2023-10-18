class Pila:
    def __init__(self):
        self.items = []

    def push(self, valor):
        self.items.append(valor)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        if not self.is_empty():
            return "\n".join(map(str, self.items))
        else:
            return "Pila vacía"
