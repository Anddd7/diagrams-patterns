from diagrams import Cluster, Diagram, Node, Edge

from diagrams.generic.blank import Blank
from diagrams.aws.network import (
    NATGateway,
    InternetGateway,
    ElasticLoadBalancing,
    TransitGateway,
    VpnGateway,
)
from diagrams.aws.database import RDSInstance
from diagrams.aws.compute import EKS
from diagrams.aws.storage import S3
from diagrams.aws.management import Organizations, Cloudtrail
from diagrams.aws.security import SingleSignOn
from diagrams.onprem.iac import Terraform
from diagrams.saas.identity import Auth0, Okta
from diagrams_patterns.aws import *
from diagrams_patterns import *

graph_attr = {"compound": "true", "splines": "line"}
with Diagram("dist/poc_aws_complex", show=False, direction="TB", graph_attr=graph_attr):
    org = Organizations()

    with Cluster("saas") as a:
        Auth0()
        okta = Okta()
    with CloudCluster("root") as croot:
        Terraform()
        S3()
        Cloudtrail()
        sso = SingleSignOn()
        tocluster(sso, okta, fontsize="20", label="SAML")
        tocluster(org, sso)

    with Cluster(
        "Organization Units",
        graph_attr={
            "pencolor": "white",
            "bgcolor": "transparent",
            "fontcolor": "gray",
            "fontsize": "50",
            "labeljust": "c",
        },
    ):
        ou_attr = {
            "pencolor": "black",
            "style": "dashed",
            "bgcolor": "transparent",
            "fontcolor": "black",
        }
        tocluster(org, HiddenPoint())

        with Cluster("mgmt", graph_attr=ou_attr):
            with Cluster("demo"):
                eks1 = EKS()
                Cloudtrail()
            with Cluster("corp"):
                eks2 = EKS()
                Cloudtrail()
            with Cluster("auto"):
                eks3 = EKS()
                Cloudtrail()

            with Cluster("network"):
                # p = HiddenPoint()
                p = VpnGateway()
                tgw = TransitGateway()
                peercluster(eks1, p)
                peercluster(eks2, p)
                peercluster(eks3, p)

            with Cluster("audit"):
                VpnGateway()
                pa = TransitGateway()

            with Cluster("identity"):
                S3()
                Terraform()
                Cloudtrail()
                p1 = HiddenPoint()
            with Cluster("identity2"):
                S3()
                Terraform()
                Cloudtrail()
                p2 = HiddenPoint()
            with Cluster("identity3"):
                S3()
                Terraform()
                Cloudtrail()
                p3 = HiddenPoint()

            # p1 - p2 - p3
            peercluster(p1, p2, p3, penwidth="0", minlen="1")

        with Cluster("platform", graph_attr=ou_attr):
            with Cluster("prod"):
                s1 = S3()
                peernodes(
                    EKS(),
                    Cloudtrail(),
                    penwidth="0",
                )
                peercluster(pa, s1, minlen="1")
                peercluster(p, s1, minlen="3")
            with Cluster("dev"):
                s2 = S3()
                peernodes(
                    EKS(),
                    Cloudtrail(),
                    penwidth="0",
                )
                peercluster(pa, s2, minlen="1")
                peercluster(p, s2, minlen="3")
            with Cluster("qa"):
                s3 = S3()
                peernodes(
                    EKS(),
                    Cloudtrail(),
                    penwidth="0",
                )
                peercluster(pa, s3, minlen="1")
                peercluster(p, s3, minlen="3")
            with Cluster("sandbox"):
                s4 = S3()
                peernodes(
                    EKS(),
                    Cloudtrail(),
                    penwidth="0",
                )
                peercluster(pa, s4, minlen="1")
                peercluster(p, s4, minlen="3")
            # peercluster(s1, s2, s3, s4, penwidth="0")
