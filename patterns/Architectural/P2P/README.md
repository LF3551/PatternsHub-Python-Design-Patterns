# [Peer-to-Peer (P2P) Architecture Pattern](../) 🤝

## Overview 🌐
The Peer-to-Peer (P2P) architecture pattern is a decentralized approach where each part of the system simultaneously acts as both a client and a server to the others. This architecture is used to distribute workloads between peers and is known for its robustness and scalability without the need for central coordination.

## Use Cases 🔍
- Systems where participants need to share resources directly without centralized intermediaries, such as file-sharing networks or cryptocurrency networks.
- Applications requiring high availability and fault tolerance where centralized servers might be a bottleneck or single point of failure.
- Scenarios that benefit from reduced latency because interactions do not require communication through a central server.

## Implementation 🛠️
The `p2p.py` file outlines a basic implementation of the P2P architecture:
- **Peer Discovery**: Mechanism for peers to find each other.
- **Data Exchange**: Methods for peers to request and share data directly.
- **Fault Tolerance**: Strategies to ensure the network remains operational even if several peers fail.

## Example Usage 📝
```python
# Example: Basic P2P Network in Python
class Peer:
    def __init__(self, identifier, peers):
        self.identifier = identifier
        self.peers = peers  # Dictionary of other peers

    def send_data(self, recipient_id, data):
        if recipient_id in self.peers:
            self.peers[recipient_id].receive_data(data)
            print(f"Data sent to {recipient_id}: {data}")
        else:
            print("Peer not found")

    def receive_data(self, data):
        print(f"Data received: {data}")

# Setup a simple network
peer1 = Peer('001', {})
peer2 = Peer('002', {})
peer1.peers['002'] = peer2
peer2.peers['001'] = peer1

# Data exchange
peer1.send_data('002', 'Hello, Peer 2!')

```

## Output 📊
```python
Data sent to 002: Hello, Peer 2!
Data received: Hello, Peer 2!

```
This output shows a direct data exchange between two peers, demonstrating the basic functionality of a P2P network.

## Business Logic Method 🧠

Here’s how complex interactions can be managed in a P2P network:
```python
def broadcast_data(self, data):
    for peer_id in self.peers:
        self.send_data(peer_id, data)
```
## Testing 🧪
The `test_p2p.py` file includes tests to ensure that:

- Peers can discover and interact with each other correctly.
- Data is accurately transmitted and received without loss.
- The network can expand and contract dynamically with peers joining and leaving.