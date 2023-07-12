```mermaid
sequenceDiagram
    participant Client
    participant Component
    participant Leaf
    participant Composite
    
    Client->>Component: operation()
    Component->>Leaf: operation()
    Leaf-->>Component: operation()
    
    alt Composite
        Component->>Composite: operation()
        Composite->>+Component: operation()
        Component->>Leaf: operation()
        Leaf-->>Component: operation()
        Composite-->>Component: operation()
    end
    Component-->>Client: operation()


```