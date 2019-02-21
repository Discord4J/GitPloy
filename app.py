import os

from flask import Flask, request
from subprocess import call

app = Flask(__name__)


@app.route("/handle_webhook")
def handle():
    payload = request.json
    if 'master' in payload['ref']:
        call("./refresh-site.sh", cwd=os.path.expanduser("~/"))


if __name__ == "__main__":
    app.run('0.0.0.0', port=7777)
