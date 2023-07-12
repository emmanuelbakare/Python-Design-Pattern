```mermaid

graph LR
A[Subject] -->|registers| B[Observer]
A -->|deregisters| B
A -->|notifies| B
B -->|"update()"| A

```