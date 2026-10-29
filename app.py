import os
import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("APP_ENV", "dev")
    return (f"<h1>myapp is running</h1>"
            f"<p>Served by: {socket.gethostname()}</p>"
            f"<p>Environment: {env}</p>")

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
