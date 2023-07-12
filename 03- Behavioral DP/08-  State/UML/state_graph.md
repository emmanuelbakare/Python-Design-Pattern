```mermaid

graph LR
A[Context] --> B[State]
A -->|"SetState()"| B
B -->|"Handle()"| A

```