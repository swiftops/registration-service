from flask import Flask
import connexion
import register_service_util as util

app = Flask(__name__)
app = connexion.App(__name__)
app.add_api('swagger.yaml')


@app.route("/swiftservice", methods=['POST'])
def add_master_service():
    return util.add_master_service()


@app.route("/swiftservice", methods=['PUT'])
def update_master_service():
    return util.update_master_service()


@app.route("/swiftservice", methods=['DELETE'])
def delete_master_service():
    return util.delete_master_service()


@app.route("/get_master_data", methods=['POST'])
def get_master_data():
    return util.get_master_data()


@app.route("/filterservice", methods=['POST'])
def register_service():
    return util.register_service()


@app.route("/filterservice", methods=['PUT'])
def update_service():
    return util.update_service()


@app.route("/filterservice", methods=['DELETE'])
def delete_service():
    return util.delete_service()


@app.route("/get_filter_service", methods=['POST'])
def get_service_data():
    return util.get_service_data()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)


