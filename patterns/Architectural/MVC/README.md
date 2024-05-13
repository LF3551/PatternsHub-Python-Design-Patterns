# [MVC (Model-View-Controller) Pattern](../) 🎨

## Overview 🌐
The Model-View-Controller (MVC) pattern is an architectural design pattern that separates an application into three interconnected components. This separation helps to manage complexity by dividing the application into the model (data), the view (user interface), and the controller (business logic), promoting organized coding and modular testing.

## Use Cases 🔍
- Web applications that require clear separation between the presentation layer and business logic.
- Applications that need multiple views of the same data simultaneously.
- Systems that require a flexible architecture to evolve the user interface without affecting the underlying business logic.

## Implementation 🛠️
The `mvc.py` file outlines a simple implementation of the MVC pattern with a focus on separation of concerns:
- **Model**: Manages the data, logic, and rules of the application.
- **View**: Displays the data to the user and sends user actions to the controller.
- **Controller**: Accepts input and converts it to commands for the model or view.

## Example Usage 📝
```python
# Example: MVC in a Python application
class Model:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)
        return item

class View:
    def display_item(self, item):
        print(f"Item: {item}")

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_item(self, item):
        new_item = self.model.add_data(item)
        self.view.display_item(new_item)

# Setup
model = Model()
view = View()
controller = Controller(model, view)

# Simulation of user interaction
controller.add_item('Apple')
```

## Output 📊
```python
Item: Apple
```
This output demonstrates a simple interaction within the MVC architecture, highlighting how the user's input is processed and displayed.

## Business Logic Method 🧠
Here's how business logic can be integrated into the controller to make decisions:
```python
def update_item(self, item, new_value):
    if item in self.model.data:
        index = self.model.data.index(item)
        self.model.data[index] = new_value
        self.view.display_item(new_value)
    else:
        self.view.display_error("Item not found")

```
## Testing 🧪
The `test_mvc.py` file includes tests to ensure that:

- The model manages data correctly.
- The view displays what it receives without processing.
- The controller correctly interacts between the model and the view.