```mermaid
graph LR
A[Client] --> B[Facade]
B --> C[Subsystem1]
B --> D[Subsystem2]
B --> E[Subsystem3]
C --> F["Operation()"]
D --> G["Operation()"]
E --> H["Operation()"]

```