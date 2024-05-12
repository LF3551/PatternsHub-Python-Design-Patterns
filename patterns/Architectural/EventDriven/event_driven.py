import logging

class EventManager:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)
        logging.info(f"Listener subscribed to {event_type}")

    def unsubscribe(self, event_type, listener):
        if event_type in self.listeners:
            self.listeners[event_type].remove(listener)
            logging.info(f"Listener unsubscribed from {event_type}")

    def notify(self, event_type, data):
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener.update(data)
            logging.info(f"Event {event_type} triggered")

class EventListener:
    def update(self, data):
        raise NotImplementedError("Subclass must implement this method")

class EmailNotificationListener(EventListener):
    def update(self, data):
        logging.info(f"Email sent with content: {data}")

class LoggingListener(EventListener):
    def update(self, data):
        logging.info(f"Log entry: {data}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    manager = EventManager()
    
    email_listener = EmailNotificationListener()
    logging_listener = LoggingListener()

    manager.subscribe("order_placed", email_listener)
    manager.subscribe("order_placed", logging_listener)

    manager.notify("order_placed", "Order #1234 has been placed")
