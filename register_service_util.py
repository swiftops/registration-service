from flask import jsonify
from service_util import register_service_util, update_service_util, delete_service_util,\
    get_service_util, service_validation, update_filter_service_util


def add_master_service():
    input_json = service_validation()
    response = register_service_util(input_json, True)
    return jsonify(response)


def update_master_service():
    input_json = service_validation()
    response = update_service_util(input_json)
    return jsonify(response)


def delete_master_service():
    input_json = service_validation()
    response = delete_service_util(input_json["data"]["keyword"], True)
    return jsonify(response)


def get_master_data():
    input_json = service_validation()
    response = get_service_util(input_json["data"]["keyword"], True)
    return jsonify(response)


def register_service():
    input_json = service_validation()
    response = register_service_util(input_json, False)
    return jsonify(response)


def update_service():
    input_json = service_validation()
    response = update_filter_service_util(input_json)
    return jsonify(response)


def delete_service():
    input_json = service_validation()
    response = delete_service_util(input_json["data"]["keyword"], False)
    return jsonify(response)


def get_service_data():
    input_json = service_validation()
    response = get_service_util(input_json["data"]["keyword"], False)
    return jsonify(response)
	
