class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the instance')
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    # Example method
    def some_business_logic(self):
        """
        Perform some business logic, which can be accessed globally through the singleton instance.
        """
        pass

# Example usage
if __name__ == "__main__":
    singleton1 = Singleton()
    print(singleton1)

    singleton2 = Singleton()
    print(singleton2)

    # Both instances are identical
    print(singleton1 is singleton2)
