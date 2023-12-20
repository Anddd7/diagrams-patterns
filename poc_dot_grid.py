from diagrams import Cluster, Diagram, Node, Edge, getcluster

from diagrams.generic.blank import Blank
from diagrams.aws.network import (
    NATGateway,
    InternetGateway,
    ElasticLoadBalancing,
)
from diagrams.aws.database import RDSInstance
from diagrams.aws.compute import EKS
from diagrams_patterns.aws import (
    SecureSubnetCluster,
    VPCCluster,
    PrivateSubnetCluster,
    PublicSubnetCluster,
    IntraSubnetCluster,
    RegionCluster,
    CloudCluster,
    AccountCluster,
    AZCluster,
)
from diagrams_patterns import HiddenPoint, peernodes


class Anchor:
    _anchorq = []

    def pin(self):
        # with getcluster():
        next = HiddenPoint()
        if len(self._anchorq) > 0:
            peernodes(self._anchorq[len(self._anchorq) - 1], next, penwidth="0")
        self._anchorq.append(next)


graph_attr = {"compound": "true"}
with Diagram(
    "dist/poc_dot_grid", show=False, direction="TB", graph_attr=graph_attr
) as diag:
    region = "us-east-1"

    igw = InternetGateway()

    with AZCluster(f"az-{region}-1a"):
        with PublicSubnetCluster(f"sn-public-{region}-1a"):
            elb = ElasticLoadBalancing()
            nat = NATGateway()
        with PrivateSubnetCluster(f"sn-private-{region}-1a"):
            Blank()
        with IntraSubnetCluster(f"sn-intra-{region}-1a"):
            Blank()

    with AZCluster(f"az-{region}-1b"):
        with PublicSubnetCluster(f"sn-public-{region}-1b"):
            Blank()
        with PrivateSubnetCluster(f"sn-private-{region}-1b"):
            Blank()
        with IntraSubnetCluster(f"sn-intra-{region}-1b"):
            rds = RDSInstance()

    with AZCluster(f"az-{region}-1c"):
        with PublicSubnetCluster(f"sn-public-{region}-1c"):
            Blank()
        with PrivateSubnetCluster(f"sn-private-{region}-1c"):
            Blank()
            eks = EKS()
        with IntraSubnetCluster(f"sn-intra-{region}-1c"):
            Blank()

    igw >> elb >> eks >> rds
    eks >> nat >> igw
