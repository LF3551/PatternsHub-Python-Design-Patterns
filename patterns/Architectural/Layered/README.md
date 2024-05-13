# [Layered (n-tier) Architecture Pattern](../) 📚

## Overview 🌐
The Layered architecture pattern, also known as n-tier architecture pattern, organizes applications into a series of layers, each with specific responsibilities and dependencies. This structure promotes a separation of concerns across the application, making it easier to manage, scale, and evolve.

## Use Cases 🔍
- Enterprise applications that require a clear separation between the user interface, business logic, and data access layers.
- Applications that need to be highly maintainable and scalable, where changes in one part of the system should have minimal impact on others.
- Systems where business policies and rules change frequently and need to be isolated from other components.

## Implementation 🛠️
The `layered_architecture.py` file contains an implementation that divides an application into three main layers:
- **Presentation Layer**: Handles all user interface and browser communication logic.
- **Business Logic Layer**: Acts as an intermediary for data exchange between the presentation layer and the database or persistence layer.
- **Data Access Layer**: Provides simple APIs for connecting and performing operations on the database.

## Example Usage 📝
```python
# Example: Using the layers in a simple application
from layered_architecture import PresentationLayer, BusinessLayer, DataAccessLayer

# Initialize layers
presentation = PresentationLayer()
business = BusinessLayer()
data_access = DataAccessLayer()

# Flow of data through layers
user_input = presentation.get_user_input()
processed_data = business.process_data(user_input)
result = data_access.save_data(processed_data)
presentation.display_result(result)
```

## Output 📊
```python
Data saved successfully: {processed_data}
```
This output indicates how data moves through each layer, from input to processing and finally to storage, showcasing the decoupled nature of each component.

## Business Logic Method 🧠

Here's an example to demonstrate how complex business rules can be implemented within the business layer:
```python
# Business rule implementation
def apply_discount(order_details):
    if order_details['quantity'] > 20:
        return order_details['price'] * 0.85  # Apply 15% discount
    return order_details['price']

# Using the business logic in a transaction
order_data = {'quantity': 25, 'price': 100}
discounted_price = apply_discount(order_data)
print(f"Discounted Price: {discounted_price}")
```
## Testing 🧪
The `test_layered_architecture.py` file includes tests to ensure that:
- Each layer only interacts with its adjacent layers.
- Business rules are correctly applied and isolated within the business layer.
- Data integrity and transaction safety are maintained through all layers.