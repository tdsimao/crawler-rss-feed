from flask import Flask, make_response, jsonify
from flask_httpauth import HTTPBasicAuth
from crawler_rss_feed import get_feed

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": "pass1",
    "user2": "pass2"
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/autoesporte/feed')
@auth.login_required
def index():
    return jsonify(get_feed())


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


if __name__ == '__main__':
    app.run()
