```mermaid
graph LR
A[Context] --> B[Strategy]
A -->|"SetStrategy()"| B
A -->|"ExecuteStrategy()"| B
B -->|"execute()"| A


```