class Memory:

    def __init__(self):
        self.logs = []

    def add(self, item):
        self.logs.append(item)

    def get(self):
        return "\n".join(self.logs)