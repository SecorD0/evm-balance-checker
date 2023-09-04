from data.models import Network


def get_network_name(network: Network) -> str:
    return str(network.name or network.rpcs[0].chain_id)
