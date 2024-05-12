# [Architectural Design Patterns](../../) 🏛️
Architectural design patterns deal with the overall layout of software components and their interactions, promoting scalability, maintainability, and the capacity to manage large applications.

## Patterns Covered 📚

### [MVC (Model-View-Controller)](./MVC/) 🎨

The MVC pattern separates application logic into three interconnected components. This separation helps manage complexity when building user interfaces.

**Usage**: Ideal for applications with a GUI, allowing multiple views for a model and separating the backend logic from the client-side view.

### [Microservices](./Microservices/) 🧩

Microservices architecture develops a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms.

**Usage**: Suitable for large, complex applications that require high scalability and flexibility.

### [Layered (n-tier architecture)](./Layered/) 📚

This pattern organizes the software into layers with specific responsibilities, making it easier to replace or upgrade entire layers without affecting the others.

**Usage**: Common in enterprise applications where separation of concerns is important for scalability and security.

### [Event-Driven Architecture](./EventDriven/) 🚀

Components asynchronously communicate events among each other. This pattern is highly scalable and dynamic.

**Usage**: Effective in environments where events are a trigger for multiple actions across disconnected components.

### [CQRS (Command Query Responsibility Segregation)](./CQRS/) ⚙️

Separates read and write operations into different models, using commands to update data, and queries to read data.

**Usage**: Useful in high-performance applications where the scalability of read operations needs to be managed separately from write operations.

### [Serverless Architecture](./Serverless/) ☁️

Runs applications as stateless compute containers that are event-triggered and fully managed by a cloud provider.

**Usage**: Great for reducing the overhead of server management and scaling applications.

### [Peer-to-Peer (P2P)](./P2P/) 🤝

Distributes tasks or workloads between peers, all of whom are equally privileged and operate both as clients and servers.

**Usage**: Suitable for applications requiring a decentralized network where data sharing is key, like file-sharing networks or blockchain applications.

## Implementation 🔧
Each pattern is implemented in its own subdirectory within a repository:
- MVC
- Microservices
- Layered
- Event-Driven
- CQRS
- Serverless
- Peer-to-Peer
Each directory contains:
- Implementation scripts.
- A README.md explaining the pattern and providing examples.
- Tests validating the implementation of the patterns.

## Testing 🧪
You can run the test suite included in each pattern's subdirectory to ensure that the implementations follow the pattern correctly and meet the expected output. This is crucial for verifying that the architectural solutions effectively address the specific challenges they are designed to solve.
