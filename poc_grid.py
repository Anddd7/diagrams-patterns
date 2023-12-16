from diagrams import Cluster, Diagram, Node, Edge

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
)

anchorq = []


def anchor():
    next = Blank()
    if len(anchorq) > 0:
        anchorq[len(anchorq) - 1] - next
    anchorq.append(next)


graph_attr = {"compound": "true", "packmode": "clust"}
with Diagram(
    "dist/poc_grid", show=False, graph_attr=graph_attr
) as diag:
    # input
    subnet_area = 3
    az_count = 3
    az_names = ["1a", "1b", "1c", "1d", "1e", "1f"]
    layer_count = 3
    layer_types = [PublicSubnetCluster, PrivateSubnetCluster, IntraSubnetCluster]
    layer_names = ["public", "private", "intra"]

    igw = InternetGateway()

    with Cluster(
        f"az-{az_names[0]}",
        graph_attr={
            "bgcolor": "transparent",
            "penwidth": "2.0",
            "style": "rounded,dashed",
        },
    ) as az1:
        with PublicSubnetCluster(f"sn-{layer_names[0]}-{az_names[0]}") as instance:
            anchor()
        with PrivateSubnetCluster(f"sn-{layer_names[1]}-{az_names[0]}") as instance:
            nat = NATGateway()
            elb = ElasticLoadBalancing()
        with IntraSubnetCluster(f"sn-{layer_names[2]}-{az_names[0]}") as instance:
            Blank()

    with Cluster(
        f"az-{az_names[1]}",
        graph_attr={
            "bgcolor": "transparent",
            "penwidth": "2.0",
            "style": "rounded,dashed",
        },
    ) as az2:
        with PublicSubnetCluster(f"sn-{layer_names[0]}-{az_names[1]}") as instance:
            anchor()
        with PrivateSubnetCluster(f"sn-{layer_names[1]}-{az_names[1]}") as instance:
            Blank()
            eks = EKS()
        with IntraSubnetCluster(f"sn-{layer_names[2]}-{az_names[1]}") as instance:
            Blank()

    with Cluster(
        f"az-{az_names[2]}",
        graph_attr={
            "bgcolor": "transparent",
            "penwidth": "2.0",
            "style": "rounded,dashed",
        },
    ) as az3:
        with PublicSubnetCluster(f"sn-{layer_names[0]}-{az_names[2]}") as instance:
            anchor()
        with PrivateSubnetCluster(f"sn-{layer_names[1]}-{az_names[2]}") as instance:
            Blank()
            rds = RDSInstance()
        with IntraSubnetCluster(f"sn-{layer_names[2]}-{az_names[2]}") as instance:
            Blank()

    igw >> elb >> eks >> rds
    eks >> nat >> igw
