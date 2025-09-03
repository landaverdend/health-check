
from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/deploy', methods=['POST'])
def handle_deploy():
  # Print the payload
  payload = request.get_json()
  print("=== Github Webhook Payload ===\n", payload)
  print(json.dumps(payload, indent=4))
  print("=== END OF PAYLOAD ===")

  return jsonify({"status": "success"}), 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050, debug=True)