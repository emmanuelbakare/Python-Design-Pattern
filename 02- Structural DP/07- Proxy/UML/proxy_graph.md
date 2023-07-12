```mermaid
graph LR
A[Client] --> B[Proxy]
B --> C[RealSubject]
A -->|"Request()"| B
B -->|"Request()"| C
C -->|"Request()"| B
B -->|"Request()"| A


```