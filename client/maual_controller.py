from pynput import keyboard
import socketio
from termcolor import colored

password = "__h0m0l__"
sio = socketio.Client()

speed = 40
order = 0

flag = True 

cont_data = {
    "w": 1,
    "s": 2,
    "a": 4,
    "d": 3,
    "q": 5,
    "e": 6
}

@sio.event
def connect():
    print(colored("[+] Connected to server", "green" ,attrs=["bold"]))

@sio.event
def disconnect():
    print(colored("[-] Disconnected from server", "red",attrs=["bold"]))

def on_key_event(key):
    global speed
    global order
    global flag 

    try:
        key_name = key.char

        if key_name == "u" and speed < 100:
            speed += 5 
            print(colored(f"[INFO] Speed (+) : {speed}", "green",attrs=["bold"]))
        if key_name == "j" and speed > 20:
            speed -= 5
            print(colored(f"[INFO] Speed (-) : {speed}", "red",attrs=["bold"]))

        if cont_data.get(key_name) and flag:
            flag = False 
            order = cont_data.get(key_name)
            sio.emit("_235", {"order": order, "speed": speed}, namespace="/")
            print(colored(f"[INFO] Key pressed: {key_name}", "green",attrs=["bold"]))
            print(colored(f"[INFO] Order sent: {order}, Speed: {speed}", "green" ,attrs=["bold"]))
    except AttributeError:
        pass

def on_key_release(key):
    global order
    global flag 
    global speed 

    try:
        key_name = key.char
        print(colored(f"[INFO] Key released: {key_name}", "yellow"))

        if not flag:
            flag = True 

        if order != 0:
            order = 0
            sio.emit("_235", {"order": order, "speed": speed}, namespace="/")
            print(colored(f"[INFO] Order sent: {order}, Speed: {speed}", "yellow"))
    except AttributeError:
        pass

if __name__ == "__main__":
    try:
        print("[INFO] Connecting to server...")
        sio.connect("http://192.168.32.215:5001", auth={"password": password})

        listener = keyboard.Listener(on_press=on_key_event, on_release=on_key_release)
        listener.start()
        listener.join()

        sio.disconnect()
    except KeyboardInterrupt:
        print("bye :)")
    except Exception as e:
        print(f"[-] Error: {e}")
