from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

counter = 0  # Variable pour stocker la valeur incrémentée
increment_interval = 1

def increment_counter():
    global counter
    while True:
        counter += 1
        socketio.emit('counter_update', {'data': counter}, namespace='/')
        time.sleep(increment_interval)

# Lancer la fonction d'incrémentation en arrière-plan
increment_thread = threading.Thread(target=increment_counter)
increment_thread.daemon = True
increment_thread.start()

@app.route('/')
def index():
    return render_template('index.html')

#if __name__ == '__main__':
   #socketio.run(app, debug=True)
