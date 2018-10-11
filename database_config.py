from pymongo import MongoClient

config = {}

with open('system.properties') as f:
    for line in f.readlines():
        line = line.strip()
        parts = line.split("=")
        key = parts[0]
        value = parts[1]
        config[key] = value

client = MongoClient(config['DB_IP'], int(config['DB_PORT']))


def get_master_collection():
    db = client.botengine.master
    return db


def get_service_collection():
    db = client.botengine.services
    return db


def get_collection(is_master):
    if is_master:
        db = get_master_collection()
    else:
        db = get_service_collection()
    return db
