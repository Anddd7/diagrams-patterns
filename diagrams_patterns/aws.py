from diagrams_ext import Cluster
from diagrams_ext.aws.general import Cloud, Account, Region
from diagrams_ext.aws.network import (
    VPC,
    PrivateSubnet,
    PublicSubnet,
    SecureSubnet,
    IntraSubnet,
)

# Cluster


class VPCCluster(Cluster):
    _icon_node = VPC
    _graph_attr = {
        "bgcolor": "white",
        "pencolor": "#8C4FFF",
    }

    def __init__(
        self,
        label: str = "vpc",
        direction: str = "LR",
    ):
        super().__init__(
            label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr
        )


class AZCluster(Cluster):
    _graph_attr = {
        "bgcolor": "transparent",
        "penwidth": "2.0",
        "style": "rounded,dashed",
    }

    def __init__(
        self,
        label: str = "az",
        direction: str = "LR",
    ):
        super().__init__(label, direction, graph_attr=self._graph_attr)


class PublicSubnetCluster(Cluster):
    _icon_node = PublicSubnet
    _graph_attr = {
        "bgcolor": "#F2F6E8",
        "pencolor": "#7AA116",
    }

    def __init__(
        self,
        label: str = "public",
        direction: str = "LR",
    ):
        super().__init__(
            label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr
        )


class PrivateSubnetCluster(Cluster):
    _icon_node = PrivateSubnet
    _graph_attr = {
        "bgcolor": "#E6F6F7",
        "pencolor": "#00A4A6",
    }

    def __init__(
        self,
        label: str = "private",
        direction: str = "LR",
    ):
        super().__init__(
            label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr
        )


class SecureSubnetCluster(Cluster):
    _icon_node = SecureSubnet
    _graph_attr = {
        "bgcolor": "#F8CECC",
        "pencolor": "#B85450",
    }

    def __init__(
        self,
        label: str = "secure",
        direction: str = "LR",
    ):
        super().__init__(
            label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr
        )


class IntraSubnetCluster(Cluster):
    _icon_node = IntraSubnet
    _graph_attr = {
        "bgcolor": "#FFE6CC",
        "pencolor": "#D79B00",
    }

    def __init__(
        self,
        label: str = "intra",
        direction: str = "LR",
    ):
        super().__init__(
            label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr
        )


class CloudCluster(Cluster):
    _icon_node = Cloud
    _graph_attr = {
        "bgcolor": "white",
        "pencolor": "#F78E04",
    }

    def __init__(
        self,
        label: str = "cloud",
        direction: str = "LR",
    ):
        super().__init__(
            label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr
        )


class AccountCluster(Cluster):
    _icon_node = Account
    _graph_attr = {
        "bgcolor": "white",
        "pencolor": "#CD2264",
    }

    def __init__(
        self,
        label: str = "account",
        direction: str = "LR",
    ):
        super().__init__(
            label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr
        )


class RegionCluster(Cluster):
    _icon_node = Region
    _graph_attr = {"bgcolor": "white", "pencolor": "#147EBA", "style": "rounded,dashed"}

    def __init__(
        self,
        label: str = "region",
        direction: str = "LR",
    ):
        super().__init__(
            label, direction, icon_node=self._icon_node, graph_attr=self._graph_attr
        )
