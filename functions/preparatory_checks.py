from data.models import Settings


async def preparatory_checks() -> str:
    settings = Settings()
    for network in settings.networks:
        if not network.rpcs:
            return 'Specify RPCs for all networks!'

        chain_id = network.rpcs[0].chain_id
        for i, rpc in enumerate(network.rpcs):
            if rpc.chain_id != chain_id:
                return f'You specified RPC from different network: {rpc.rpc}'

        if not network.tokens and not network.nfts:
            return "You didn't provide either token or NFT addresses!"

    return ''
