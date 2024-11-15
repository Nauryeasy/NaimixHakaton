from functools import lru_cache

import punq
from punq import Scope


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container():

    container = punq.Container()

    return container
