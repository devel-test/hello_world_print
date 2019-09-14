import os
import signal
from flask import Flask
from hw_app import hello_world_print

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))


@app.route("/")
def generate_hw_app():
    page = '<html><body><h1>'
    page += hello_world_print.get_phrase()
    page += '</h1></body></html>'
    return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))