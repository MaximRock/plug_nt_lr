import random

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

issue = []

@app.route('/rest/api/2/issue', methods=['POST'])
def create_issue():
    new_one = request.json
    n_dict: dict = new_one
    if 'fields' in n_dict:
        id_number = int(random.randint(100, 999))
        key_nymber = 'test-' + str(random.randint(100, 999))
        n_dict['id'] = id_number
        n_dict['key'] = key_nymber
        summary = n_dict['fields']['summary']
        id = {'id': id_number, 'key': key_nymber, 'summary': summary}
        issue.append(n_dict)
        return jsonify(id)
    else:
        return "'messge': 'incorrect body'", 400



@app.route('/rest/api/2/issue/<int:issue_id>', methods=['GET'])
def get_issue(issue_id):
    item = next((i for i in issue if i['id'] == issue_id), None)
    if not item:
        return "'messge': 'No issue_id'", 400
    return jsonify(item)


@app.route('/rest/api/2/issue/all', methods=['GET'])
def get_issue_all():
    return jsonify(issue)


@app.route('/rest/api/2/issue/<int:issue_id>', methods=['PUT'])
def update_issue(issue_id):
    item = next((i for i in issue if i['id'] == issue_id), None)
    params = request.json
    if not item:
        return "'messge': 'No issue_id'", 400
    item.update(params)
    return item


@app.route('/rest/api/2/issue/<int:issue_id>', methods=['DELETE'])
def delete_issue(issue_id):
    index = next((i for i in issue if i['id'] == issue_id), None)
    if not index:
        return "'messge': 'No issue_id'", 404
    else:
        issue.remove(index)
        return '', 204


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')




