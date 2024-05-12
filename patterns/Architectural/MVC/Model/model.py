class DataModel:
    def __init__(self):
        self.data = {}

    def add_item(self, key, value):
        self.data[key] = value
        return self.data[key]

    def get_item(self, key):
        return self.data.get(key, None)
