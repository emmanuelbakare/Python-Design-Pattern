```mermaid 

graph TB
A[Client] --> B[TargetInterface]
A --> C[Adaptee]
B --> D[Adapter]
D --> C
A -->|"Request()"| B
B -->|"SpecificRequest()"| D
D -->|"SpecificRequest()"| C

```