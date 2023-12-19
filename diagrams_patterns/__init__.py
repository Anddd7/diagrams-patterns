from typing import Dict
from diagrams import Cluster, Diagram, Edge, Node


def HiddenPoint():
    return Node("", shape="none", width="0", height="0")


# draw an edge from [f] to [t]‘s cluster
def tocluster(f: Node, t: Node, **attrs: Dict):
    return f - Edge(lhead=t._cluster.name, **attrs) - t


# draw an edge from [f]‘s cluster to [t]
def fromcluster(f: Node, t: Node, **attrs: Dict):
    return f - Edge(ltail=f._cluster.name, **attrs) - t


# draw an edge to connect clusters between the nodes
# patterns:
# - penwidth="0", hide the edge and force clusters to re-order, e.g. TB -> LR
def peercluster(*args: Node, **attrs: Dict):
    if len(args) < 2:
        return

    for i in range(0, len(args) - 1):
        (
            args[i]
            - Edge(
                ltail=args[i]._cluster.name,
                lhead=args[i + 1]._cluster.name,
                **attrs,
            )
            - args[i + 1]
        )

# draw an edge to connect nodes
# patterns:
# - penwidth="0", hide the edge and force nodes to re-order, e.g. wrap, align   
def peernodes(*args: Node, **attrs: Dict):
    if len(args) < 2:
        return

    for i in range(0, len(args) - 1):
        args[i] - Edge(**attrs) - args[i + 1]
