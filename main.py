from flask import Flask, request, jsonify


app = Flask(__name__)
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Hello, World!"})


@app.route('/new-endpoint', methods=['GET'])
def new_endpoint():
    return jsonify({"message": "This is a new endpoint!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
