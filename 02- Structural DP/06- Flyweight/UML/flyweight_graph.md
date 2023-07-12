```mermaid
graph TB
A[Client] --> B[FlyweightFactory]
B --> C[Flyweight]
B --> D["GetFlyweight()"]
C --> E["Operation()"]
A -->|"Request(state)"| D
D -->|"Operation(state)"| C


```