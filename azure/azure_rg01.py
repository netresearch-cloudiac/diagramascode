from diagrams import Cluster, Diagram
from diagrams.azure.general import Resourcegroups
from diagrams.azure.compute import VM, VMWindows, VMLinux, VMImages, VMScaleSet
from diagrams.azure.network import VirtualNetworks, Firewall, LoadBalancers

graph_attr = {
    "fontsize": "20",
    #"bgcolor": "transparent"
}

with Diagram("IaaS", show=False, graph_attr=graph_attr, filename="iaas01", direction="LR"):
    lb = LoadBalancers("LB_APP01")
    fw = Firewall("AzFW01")

    #lb >> fw
    fw >> lb
    lb >> VM("web01")
    lb >> VMWindows("web02")
    lb >> VMLinux("web03")
    lb >> VMScaleSet("web0xx")

    # Firewall("AzFW01") >> LoadBalancers("LB_APP01") >> VM("web01")
    # Firewall("AzFW01") >> LoadBalancers("LB_APP01") >> VM("web02")

    # Resourcegroups("RG-test")