from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def server_is_up():
    app.logger.info('server is up and running')
    return jsonify({'response': 'server is up and running'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
