```mermaid

sequenceDiagram
    participant Director
    participant Builder
    participant Product
    
    Director->>Builder: construct()
    Builder->>Product: buildPartA()
    Builder->>Product: buildPartB()
    Product-->>Builder: Assembled Product
    Builder-->>Director: Completed Product


```