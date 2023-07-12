```mermaid

graph LR
A[Component] -->|implements| B[ConcreteComponent]
A --> C[Decorator]
C --> D[Component]
C --> E["Operation()"]
E --> D
D --> F["Operation()"]

 

```