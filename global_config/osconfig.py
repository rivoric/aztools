from os import environ
from typing import Any

def get_env_var_default(name: str, default: Any = None) -> Any:
    if name in environ:
        return environ[name]
    return default
