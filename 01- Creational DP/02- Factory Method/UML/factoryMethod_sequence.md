```mermaid

sequenceDiagram
    participant Creator
    participant ConcreteCreator
    participant Product
    participant ConcreteProduct
    
    Creator->>ConcreteCreator: createProduct()
    alt Condition
        ConcreteCreator->>ConcreteProduct: new ConcreteProduct()
    else
        ConcreteCreator->>Product: new Product()
        ConcreteProduct->>ConcreteProduct: initialize()
    end
    ConcreteCreator-->>Creator: return Product

```