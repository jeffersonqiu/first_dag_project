from networkx.utils.backends import _dispatch

@_dispatch
def build_auxiliary_node_connectivity(G): ...
@_dispatch
def build_auxiliary_edge_connectivity(G): ...
