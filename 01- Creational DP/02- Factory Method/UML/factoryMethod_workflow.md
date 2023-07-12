```mermaid 
graph LR
A[Creator] --> B[Factory]
B --> C[Product]
B --> D[ConcreteFactoryA]
D --> E[ConcreteProductA]
B --> F[ConcreteFactoryB]
F --> G[ConcreteProductB]

```