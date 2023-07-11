```mermaid 

classDiagram
    class Target {
        + request(): void
    }

    class Adaptee {
        + specific_request(): void
    }

    class Adapter {
        - adaptee: Adaptee
        + request(): void
    }

    Target ..> Adapter: uses
    Adapter --> Adaptee: adapts

```