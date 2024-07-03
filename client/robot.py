# client.py
import socketio
import hashlib

sio = socketio.Client()

password = "__h0m0l__"

@sio.event
def connect():
    print("[+] Connection established")

@sio.event
def disconnect():
    print("[-] Connection lost!")

@sio.event
def order_response(data):
    if 200 > data.get("status") > 300: 
        print("[+] Data was sent successfully.")
    else:
        print("[-] Failed to send data.")

if __name__ == "__main__":
    try:
        sio.connect("http://192.168.137.248:5000", auth={"password": password})

        sio.emit("_235", {"order": 0})

        sio.wait()
    except KeyboardInterrupt:
        print("[-] Quit")
    except Exception as e:
        print("[-] Error : {e}")

