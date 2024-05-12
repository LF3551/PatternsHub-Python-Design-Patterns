import logging

# Command classes
class Command:
    def execute(self):
        raise NotImplementedError("Subclass must implement abstract method")

class AddItemCommand(Command):
    def __init__(self, store, item):
        self.store = store
        self.item = item

    def execute(self):
        self.store.add_item(self.item)
        logging.info(f"Added item: {self.item}")

# Query classes
class Query:
    def execute(self):
        raise NotImplementedError("Subclass must implement abstract method")

class GetAllItemsQuery(Query):
    def __init__(self, store):
        self.store = store

    def execute(self):
        logging.info("Fetching all items")
        return self.store.get_all_items()

# Receiver class
class Store:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_all_items(self):
        return self.items

# Invoker class
class CQRS:
    def dispatch(self, action):
        return action.execute()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    store = Store()
    cqrs = CQRS()

    # Commands
    cqrs.dispatch(AddItemCommand(store, "Apple"))
    cqrs.dispatch(AddItemCommand(store, "Banana"))

    # Queries
    all_items = cqrs.dispatch(GetAllItemsQuery(store))
    print("All items in store:", all_items)
