from dataclasses import dataclass
import os


def _required_setting(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def _boolean_setting(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class CosmosSettings:
    endpoint: str
    credential: str
    database_name: str
    container_name: str
    connection_verify: bool

    @classmethod
    def from_environment(cls) -> "CosmosSettings":
        return cls(
            endpoint=_required_setting("COSMOS_ENDPOINT"),
            credential=_required_setting("COSMOS_KEY"),
            database_name=os.getenv("COSMOS_DATABASE", "workshop-planner"),
            container_name=os.getenv("COSMOS_CONTAINER", "workshops"),
            connection_verify=_boolean_setting("COSMOS_SSL_VERIFY", True),
        )