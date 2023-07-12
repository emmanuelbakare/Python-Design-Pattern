```mermaid 
graph LR
A[Client] --> B[Element]
A --> C[Visitor]
B -->|"Accept(Visitor)"| C
C -->|"Visit(Element)"| B



```