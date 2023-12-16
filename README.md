# diagrams-patterns

- diagrams should only used for managing the basic shapes of the cloud components
- but there are standard patterns usually used in cloud architecture, we don't need to draw them from scratch
- e.g. VPC with public/private subnets, NAT gateway, etc.

**diagrams-patterns** is a collection of patterns for diagrams that can be reused in different projects.

## Features

- [x] aws vpc, subnets with styles
- [x] aws overlapping az on subnets
- [ ] dsl 2 py 2 diagrams (refer to d2)

## Reference

- [ ] <https://github.com/terrastruct/d2?tab=readme-ov-file#community-plugins>

- [ ] read tfstate and generate graph
  - <https://github.com/cycloidio/inframap>
  - <https://github.com/28mm/blast-radius>

- [ ] read aws cli and generate graph
  - <https://github.com/Cloud-Architects/cloudiscovery>

- [ ] other terraform interesting tools
  - <https://github.com/cycloidio/terracost>
  - <https://pypi.org/project/python-hcl2/>
