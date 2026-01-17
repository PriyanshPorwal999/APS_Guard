from dataclasses import dataclass
import os
import pymongo

@dataclass
class EnvironmentVariable:
    mongo_db_url: str = os.getenv("MONGO_DB_URL")

env_var = EnvironmentVariable()

if env_var.mongo_db_url is None:
    raise Exception("MONGO_DB_URL is not set or .env file not loaded")

print("Mongo URL Loaded:", env_var.mongo_db_url)

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
