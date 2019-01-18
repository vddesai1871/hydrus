from flask import Flask
from flask_socketio import SocketIO, Namespace, emit


class MyCustomNamespace(Namespace):
    def on_connect(self):
        print("A Client connected")

    def on_disconnect(self):
        print("A client disconnected")

    def on_my_event(self, data):
        print("Received event")
        print(data)
        emit('my_response', {"message": "got it"})


socketio = SocketIO()


def create_socket(app: Flask) -> SocketIO:
    socketio.init_app(app)
    socketio.on_namespace(MyCustomNamespace('/test'))
    return socketio
