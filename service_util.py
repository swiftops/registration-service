from flask import request
from database_config import get_collection, get_service_collection, get_master_collection
from authentication import _validate_user


def register_service_util(input_json, is_master):
    db = get_collection(is_master)
    swiftservice = _create_service_input(input_json)
    try:
        result = db.insert_one(swiftservice)
        data = {
            "result id": str(result.inserted_id)
        }
        response = _create_rest_success_output(data)
    except Exception as e:
        response = _create_rest_error_output("Error while registering service : " + str(e), 500)
    return response


def update_service_util(input_json):
    db = get_master_collection()
    try:
        db.find_one_and_update(
            {"master.key": {"$regex": "release", "$options": "i"}},
            {"$addToSet": {"master.value" + "." + input_json["data"]["rel"]: input_json["data"]["build"]}},
            upsert=True
        )

        db.find_one_and_update(
            {"master.key": {"$regex": "performance", "$options": "i"}},
            {"$addToSet": {"master.value" + "." + input_json["data"]["rel"]: input_json["data"]["rel"]}},
            upsert=True
        )

        db.find_one_and_update(
            {"master.key": {"$regex": "build", "$options": "i"}},
            {"$addToSet": {"master.value" + "." + input_json["data"]["build"]: input_json["data"]["rel"]}},
            upsert=True
        )

        data = {"success": "success"}
        response = _create_rest_success_output(data)
    except Exception as e:
        response = _create_rest_error_output("Error while updating service" + str(e), 500)
    return response


def delete_service_util(keyword, is_master):
    db = get_collection(is_master)
    try:
        if is_master:
            db.delete_one({"master.key": {"$regex": keyword, "$options": "i"}})
        else:
            db.delete_one({"name": {"$regex": keyword, "$options": "i"}})
        data = {"success": "success"}
        response = _create_rest_success_output(data)
    except Exception as e:
        response = _create_rest_error_output("Error while deleting service" + str(e), 500)
    return response


def get_service_util(query, is_master):
    db = get_collection(is_master)
    try:
        if is_master:
            result = db.find_one({"master.key": {"$regex": query, "$options": "i"}})
        else:
            result = db.find_one({"name": {"$regex": query, "$options": "i"}})
        response = _create_rest_success_output((str(result)))
    except Exception as e:
        response = _create_rest_error_output("Error while deleting service" + str(e), 500)
    return response


def _create_rest_error_output(error_message, error_code):
    response = {
        "success": "false",
        "data": {},
        "error": {
            "code": error_code,
            "message": error_message
        }
    }
    return response


def _create_rest_success_output(data):
    response = {
        "success": "true",
        "data": data,
        "error": {}
    }
    return response


def _create_service_input(input_json):
    swiftservice = {}
    for val in input_json["data"]:
        temp = str(val)
        swiftservice[temp] = input_json["data"][temp]
    return swiftservice


def service_validation():
    if request.is_json:
        input_json = request.get_json()
        authtoken = input_json["authheader"]["authtoken"]
        _validate_user(authtoken)
    else:
        input_json = {"Error", "Invalid input type"}
    return input_json


def update_filter_service_util(input_json):
    db = get_service_collection()
    swiftservice = _create_service_input(input_json)
    try:
        db.find_one_and_update(
            {"name": input_json["data"]["name"]},
            {"$set": swiftservice}
        )
        data = {"success": "success"}
        response = _create_rest_success_output(data)
    except Exception as e:
        response = _create_rest_error_output("Error while updating service" + str(e), 500)
    return response

