from diagrams_ext import Cluster, Diagram, Node

from diagrams_ext.aws.network import (
    NATGateway,
    InternetGateway,
    ElasticLoadBalancing,
)
from diagrams_ext.aws.database import RDSInstance
from diagrams_ext.aws.compute import EKS
from diagrams_ext.generic.blank import Blank
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
from diagrams_patterns.neato import (
    PinedCluster,
    getpinedpos,
    NEATO_STYLE_DiagramAttr,
    getx,
    gety,
    PinedPosManager,
)

with Diagram("dist/poc_neato_overlap", show=False, graph_attr=NEATO_STYLE_DiagramAttr):
    pinedvpc = PinedVPC()

    with pinedvpc.getvpc():
        igw = InternetGateway(
            pin="true", pos=f"{getx(shfit=pinedvpc._width/2)},{gety(shfit=-2)}"
        )

    with pinedvpc.getsubnet("1b", "public") as instance:
        pos = PinedPosManager()
        nat = NATGateway(pin="true", pos=pos.nextpos())
        elb = ElasticLoadBalancing(pin="true", pos=pos.nextpos())
        Blank(pin="true", pos=pos.nextpos())
        ElasticLoadBalancing(pin="true", pos=pos.nextpos())

    with pinedvpc.getsubnet(1, 1) as instance:
        pos = PinedPosManager()
        eks = EKS(pin="true", pos=pos.nextpos())

    with pinedvpc.getsubnet(1, "intra") as instance:
        pos = PinedPosManager()
        rds = RDSInstance(pin="true", pos=pos.nextpos())

    igw >> elb >> eks >> rds
    eks >> nat >> igw
