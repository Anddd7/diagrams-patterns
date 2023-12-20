from diagrams import Node, setcluster, getcluster, Cluster

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
def getpinedpos(cluster: Cluster = None):
    if cluster is None:
        cluster = getcluster()
    return (
        float(cluster.dot.graph_attr.get("pin_x")),
        float(cluster.dot.graph_attr.get("pin_y")),
        float(cluster.dot.graph_attr.get("pin_w")),
        float(cluster.dot.graph_attr.get("pin_h")),
    )


def getx(cluster: Cluster = None, shfit=0):
    if cluster is None:
        cluster = getcluster()
    return float(cluster.dot.graph_attr.get("pin_x")) + shfit


def gety(cluster: Cluster = None, shfit=0):
    if cluster is None:
        cluster = getcluster()
    return float(cluster.dot.graph_attr.get("pin_y")) + shfit


class PinedPosManager:
    _x = 0
    _y = 0
    _width = 0
    _height = 0
    _padding = 0.4
    _node_size = 1.9  # same as the node size

    _cur_x = 0
    _cur_y = 0

    def __init__(self):
        x, y, w, h = getpinedpos()
        self._x = x
        self._y = y
        self._width = w
        self._height = h

    def nextxy(self):
        if (self._cur_x == 0) and (self._cur_y == 0):
            self._cur_x = self._x + self._padding
            self._cur_y = self._y + self._padding
        else:
            self._cur_x = self._cur_x + self._node_size
            if (self._cur_x - self._x) > self._width:
                self._cur_x = self._x + self._padding
                self._cur_y = self._cur_y + self._node_size

        return self._cur_x, self._cur_y

    def nextpos(self):
        x, y = self.nextxy()
        return f"{x},{y}"
