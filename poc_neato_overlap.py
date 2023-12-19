from diagrams import Cluster, Diagram, Node

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
from diagrams_patterns.neato_aws import PinedVPC
from diagrams_patterns.neato import PinedCluster, getpinedpos, NEATO_STYLE_DiagramAttr

with Diagram("dist/poc_neato_overlap", show=False, graph_attr=NEATO_STYLE_DiagramAttr):
    pinedvpc = PinedVPC()
    padding = 0.4

    with pinedvpc.getvpc():
        igw = InternetGateway(pin="true", pos=f"{pinedvpc._width/2},{-2}")

    with pinedvpc.getsubnet("1b", "public") as instance:
        x, y, _, _ = getpinedpos(instance)
        x, y = x + padding, y + padding
        nat = NATGateway(pin="true", pos=f"{x},{y}")
        elb = ElasticLoadBalancing(pin="true", pos=f"{x+2},{y}")

    with pinedvpc.getsubnet(1, 1) as instance:
        x, y, _, _ = getpinedpos(instance)
        x, y = x + padding, y + padding
        eks = EKS(pin="true", pos=f"{x},{y}")

    with pinedvpc.getsubnet(1, "intra") as instance:
        x, y, _, _ = getpinedpos(instance)
        x, y = x + padding, y + padding
        rds = RDSInstance(pin="true", pos=f"{x},{y}")

    igw >> elb >> eks >> rds
    eks >> nat >> igw
