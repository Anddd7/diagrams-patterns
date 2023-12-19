from diagrams import Node, setcluster, Cluster
from diagrams_patterns.aws import (
    PublicSubnetCluster,
    PrivateSubnetCluster,
    IntraSubnetCluster,
    VPCCluster,
    AZCluster,
)
from diagrams_patterns.neato import PinedCluster


class PinedVPC:
    _default_az_names = ["1a", "1b", "1c", "1d", "1e", "1f"]
    _default_layer_types = [
        PublicSubnetCluster,
        PrivateSubnetCluster,
        IntraSubnetCluster,
    ]
    _default_layer_names = ["public", "private", "intra"]

    # style

    _vpc_padding = 0.6
    _az_margin = 2
    _az_padding = 0.4
    _subnet_margin = 2

    # objects

    _vpc = None
    _subnets = []
    _width = 0
    _height = 0

    def __init__(
        self,
        az_count=3,
        layer_count=3,
        area_size=3,
        az_names=_default_az_names,
        layer_types=_default_layer_types,
        layer_names=_default_layer_names,
        x=0,
        y=0,
    ):
        az_width = area_size + 2 * self._az_padding
        az_height = (
            area_size * layer_count
            + self._subnet_margin * (layer_count - 1)
            + 2 * self._az_padding
        )

        vpc_width = (
            az_width * az_count
            + self._az_margin * (az_count - 1)
            + 2 * self._vpc_padding
        )
        vpc_height = az_height + 2 * self._vpc_padding

        self._width = vpc_width
        self._height = vpc_height

        self._vpc = PinedCluster(
            VPCCluster("vpc"),
            x,
            y,
            vpc_width,
            vpc_height,
        )

        for ia in range(az_count):
            azx = x + self._vpc_padding + ia * (az_width + self._az_margin)
            azy = y + self._vpc_padding

            PinedCluster(
                AZCluster(f"az-{az_names[ia]}"),
                azx,
                azy,
                az_width,
                az_height,
            )

            for il, type in enumerate(layer_types):
                snx = azx + self._az_padding
                sny = azy + self._az_padding + il * (area_size + self._subnet_margin)
                name = f"sn-{layer_names[il]}-{az_names[ia]}"
                subnet = PinedCluster(
                    type(name),
                    snx,
                    sny,
                    area_size,
                    area_size,
                )
                self._subnets.append(subnet)

    def getvpc(self):
        return self._vpc

    def getsubnet(self, az, layer):
        if isinstance(az, str):
            az = self._default_az_names.index(az)
        if isinstance(layer, str):
            layer = self._default_layer_names.index(layer)

        return self._subnets[az * 3 + layer]

    def getwidth(self):
        return self._width

    def getheight(self):
        return self._height
