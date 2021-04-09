from flask import Flask, jsonify, request
import json

app = Flask(__name__)
# These two lines should always be at the end of your app.py file.

todos = [{ "label": "My first task", "done": False },
    { "label": "My second task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

    #return "<h1>Hello!</h1>"
    
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

