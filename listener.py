
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/deploy', methods=['POST'])
def handle_deploy():


  return jsonify({"status": "success"}), 200
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050, debug=True)