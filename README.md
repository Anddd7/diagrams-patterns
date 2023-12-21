# diagrams-patterns

- diagrams should only used for managing the basic shapes of the cloud components
- but there are standard patterns usually used in cloud architecture, we don't need to draw them from scratch
- e.g. VPC with public/private subnets, NAT gateway, etc.

**diagrams-patterns** is a collection of patterns for diagrams that can be reused in different projects.

## Features

- [x] aws vpc, subnets with styles
  - ![](https://private-user-images.githubusercontent.com/24785373/292077524-68bde01c-b101-4ab7-a9db-8b5ac6c3cb61.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDMxMjkzNjEsIm5iZiI6MTcwMzEyOTA2MSwicGF0aCI6Ii8yNDc4NTM3My8yOTIwNzc1MjQtNjhiZGUwMWMtYjEwMS00YWI3LWE5ZGItOGI1YWM2YzNjYjYxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjIxVDAzMjQyMVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWI2YjlkYjM0MzRkNzY3MjU1MzIwOTliMmU4Y2QzMmIxOTFhMmMxMjAxZDYwNmQ0YzYyOWI0NzQxMGM1OGRiNmYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.k3YkUp2gxXvEhL6dMaS5sz4RFtZ9tuI3vh0gFrlgpxw)
- [x] aws overlapping az on subnets
  - calculate the position based on the number of az and subnets
  - store and reuse the calculated position
  - ![](https://private-user-images.githubusercontent.com/24785373/292077616-04455e5d-a444-4ed8-b837-2a0c711c5d74.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDMxMjk0MDMsIm5iZiI6MTcwMzEyOTEwMywicGF0aCI6Ii8yNDc4NTM3My8yOTIwNzc2MTYtMDQ0NTVlNWQtYTQ0NC00ZWQ4LWI4MzctMmEwYzcxMWM1ZDc0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjIxVDAzMjUwM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTAyNmYzZjJjYmQ0NDYwYTFkOTg4ZmRlMTY3MWFlMDllODY3MWM5YjQ2ODllOWZiOWYxZTlkZmM2YzY2NzBkN2QmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.QoiVrT-Y9UngX9OPBfM5SD0u-IuVsAJfs6g0yD_EDFw)
- [x] aws grid subnets with az
  - ~~use 'anchor', a hidden node, to align the subnets~~
  - not really work
  - ![](https://private-user-images.githubusercontent.com/24785373/292077595-a2d0564e-f7db-4816-9003-b8b3c627e9ff.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDMxMjkzODksIm5iZiI6MTcwMzEyOTA4OSwicGF0aCI6Ii8yNDc4NTM3My8yOTIwNzc1OTUtYTJkMDU2NGUtZjdkYi00ODE2LTkwMDMtYjhiM2M2MjdlOWZmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMjElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjIxVDAzMjQ0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWIzN2U3ZDc5OTI3NDdiOWUwNzY5YzFhZWU5YmNhODI2YmE3NDgwZTk2MzE2Y2FkZDFhMzMyNGE4ZjdkYWZmYjgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.BcL7kEkFjaMCPzuQndODjc2QuEOjjPKKenFxJZqWsj0)
- [ ] dsl investigate
  - dsl 2 py 2 diagrams (refer to d2)

## Roadmap

Currently, the **diagrams-patterns** and diagrams-exporters are built as 'diagrams'-extensions. But since the diagrams is inactive, introducing new tools is a necessary step, e.g. d2.

At that time, the **diagrams-patterns** should be a standalone tool, which provide a standard DSL to describe the common patterns in cloud architecture (or other kinds of diagrams). Then, you can translate the DSL to different tools, e.g. diagrams, d2, etc.

The **diagrams-exporters** plays another role to facilitate with productive tools, e.g. terraform, aws cli, etc. It read the metadata, convert to DSL, then generate the diagrams.

A possible structure is:

```mermaid
flowchart BT
  subgraph diagram-exporters
    terraform-exporter
    awscli-exporter
    kubectl-exporter
  end

  subgraph diagrams-patterns
    subgraph common-patterns
      c4-pattern
      layer-arch-pattern    
    end

    subgraph cloud-patterns
      aws-pattern
      azure-pattern
    end

    subgraph dsl
      dsl-parser

      dsl-to-diagrams
      dsl-to-d2
      dsl-to-mermaid
    end
  end

  diagrams-patterns --> diagram-exporters
  diagrams --> diagrams-patterns
  d2 --> diagrams-patterns
  plantuml --> diagrams-patterns
  
  graphviz --> diagrams
  graphviz --> d2

  plantuml
```

## Reference

- graphviz & dot
  - <https://github.com/pydot/pydot>

- d2
  - <https://github.com/terrastruct/d2>
  - <https://github.com/MrBlenny/py-d2>

- read tfstate and generate graph
  - <https://github.com/cycloidio/inframap>
  - <https://github.com/28mm/blast-radius>

- read aws cli and generate graph
  - <https://github.com/Cloud-Architects/cloudiscovery>

- other terraform interesting tools
  - <https://github.com/cycloidio/terracost>
  - <https://pypi.org/project/python-hcl2/>
