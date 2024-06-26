# server.py
from flask import Flask
from flask_socketio import SocketIO, emit, disconnect
import hashlib
# from engine.controller import Controller 

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)
# controller = Controller()

VALID_PASSWORD_HASH = hashlib.sha256("__h0m0l__".encode()).hexdigest()

@app.route("/")
def index():
    return "[+] Flask-SocketIO Server is Running"

@socketio.on("connect")
def handle_connect(auth):
    print(auth)
    if auth and hashlib.sha256(auth.get("password").encode()).hexdigest() == VALID_PASSWORD_HASH:
        print("[+] Client connected")
    else:
        print("[-] Unauthorized connection attempt")
        disconnect()

@socketio.on("disconnect")
def handle_disconnect():
    print("[+] Client disconnected")

@socketio.on("_235")
def handle_order(data):
    print("[+] Received order:", data)
    emit("_l235", {"status": 200})

if __name__ == "__main__":
    socketio.run(app, debug=True)
