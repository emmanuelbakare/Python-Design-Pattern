```mermaid

graph LR
A[Director] --> B[Builder]
B --> C[Product]
A --> D[Construct]
D --> E[BuilderStep1]
D --> F[BuilderStep2]
D --> G[BuilderStep3]
E --> H[Part1]
F --> I[Part2]
G --> J[Part3]
H --> C
I --> C
J --> C

```