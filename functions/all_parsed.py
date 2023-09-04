from data.models import Settings
from utils.db_api.database import get_addresses


async def all_parsed(settings: Settings) -> bool:
    for network in settings.networks:
        chain_id = network.rpcs[0].chain_id
        rows = get_addresses(chain_id=chain_id)
        for row in rows:
            if None in row:
                return False

    return True
