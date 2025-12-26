from flask import Flask, request, jsonify


app = Flask(__name__)
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Hello, World!"})


@app.route('/new-endpoint', methods=['GET'])
def new_endpoint():
    return jsonify({"message": "This is a new endpoint!"})


@app.route('/new-endpoint', methods=['POST'])
def new_endpoint_post():
    data = request.get_json()
    return jsonify({"received_data": data}), 201
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
