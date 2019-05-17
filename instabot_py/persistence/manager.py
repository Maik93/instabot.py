class PersistenceManager:
    def __new__(cls, config, bot):

        if not config or not config.get("type", None):
            # In memory database
            connection_string = 'sqlite:///:memory:'
            from instabot_py.persistence.sql import Persistence
            return Persistence(connection_string, bot)
        elif config["type"].lower() == "sql":
            from instabot_py.persistence.sql import Persistence
            return Persistence(config["connection_string"], bot)
