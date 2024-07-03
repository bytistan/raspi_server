import socketio
import keyboard
import hashlib

password = "__h0m0l__"
sio = socketio.Client()

speed = 30

cont_data = {
        "w":1,
        "s":2,
        "a":4,
        "d":3,
        "q":5,
        "e"6
}

@sio.event
def connect():
    print("[+] Connected to server")

@sio.event
def disconnect():
    print("[-] Disconnected from server")

def send_keypress():
    def on_key_event(e):
        key = e.name
        if key == "u" and speed < 100:
           speed += 5 
        if key == "j" and speed > 20:
            speed -= 5

        if cont_data.get(key):
            sio.emit("_235", {"order": cont_data.get(key) "speed":speed}, namespace="/")
            print(f"[+] : {cont_data.get(key)}")
        else:
            sio.emit("_235", {"key": 0}, namespace="/")

    keyboard.on_press(on_key_event)
    keyboard.wait("esc")  

if __name__ == "__main__":
    try:
        sio.connect("http://192.168.137.248:5000", auth={"password": password})
        send_keypress()
        sio.disconnect()
    except KeyboardInterrupt:
        print("[-] Quit")
    except Exception as e:
        print(f"[-] Error : {e}")
