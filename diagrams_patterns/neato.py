from diagrams import Node, setcluster, Cluster

NEATO_STYLE_DiagramAttr = {"layout": "neato", "compound": "true", "splines": "spline"}


def ThumbtackNode(x, y):
    return Node("", shape="none", pin="true", pos=f"{x},{y}")


# use thumbtack node to pin the border of cluster
def PinedCluster(
    cluster: Cluster,
    x=0,
    y=0,
    width=0,
    height=0,
):
    cluster.dot.graph_attr.update(
        {
            "pin_x": f"{x}",
            "pin_y": f"{y}",
            "pin_w": f"{width}",
            "pin_h": f"{height}",
        }
    )
    with cluster:
        ThumbtackNode(x, y)
        ThumbtackNode(x + width, y + height)
    return cluster


# get the pin position of cluster
def getpinedpos(cluster: Cluster):
    return (
        float(cluster.dot.graph_attr.get("pin_x")),
        float(cluster.dot.graph_attr.get("pin_y")),
        float(cluster.dot.graph_attr.get("pin_w")),
        float(cluster.dot.graph_attr.get("pin_h")),
    )
