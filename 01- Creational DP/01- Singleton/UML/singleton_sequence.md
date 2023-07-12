```mermaid
sequenceDiagram
    participant Client
    participant Singleton

    Client->>Singleton: GetInstance()
    Singleton-->>Client: Instance
    Client->>Singleton: Operation()
    Singleton-->>Client: Result


```