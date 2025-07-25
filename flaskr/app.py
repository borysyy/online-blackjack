from utils import generate_room_code
from flask import Flask, render_template, redirect, url_for, request, session
from flask_socketio import SocketIO, send, emit, join_room, leave_room


app = Flask(__name__)
app.config['SECRET_KEY'] = 'random'
socketio = SocketIO(app, manage_session=True)


rooms = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-user', methods=['POSt'])
def create_user():
    if request.method == 'POST':
        
        username = request.form.get('username')
        session['username'] = username
        
        return redirect(url_for('join_create'))
    
@app.route('/join-create')
def join_create():
    username = session.get('username')
    return render_template('join_create.html', username=username)

@app.route('/create-room', methods=['POST'])
def create_room():
    room_code = generate_room_code(rooms)
    rooms[room_code] = {'players': []}
    return redirect(url_for('room', room_code=room_code))

@app.route('/join-room', methods=['POST'])
def join_room_route():
    room_code = request.form.get('roomCode').upper()
    return redirect(url_for('room', room_code=room_code))

@app.route('/room/<room_code>', methods=['GET', 'POST'])
def room(room_code):
    if room_code not in rooms:
        return "Room not found", 404
    if request.method == 'GET':
        room_data = rooms[room_code]
        return render_template('room.html', room_data=room_data, room_code=room_code)

@socketio.on('join_room')
def handle_join(data):
    room = data['room']
    username = session.get('username')
        
    if username not in rooms[room]['players']:
        rooms[room]['players'].append(username)
        join_room(room)
        emit('user_joined', {'username': username}, room=room, include_self=False)
        emit('room_state', {'players': rooms[room]['players']}, room=room)
        
@socketio.on('check_state')
def room_state(data):
    room = data['room']
    players = rooms[room]['players']
    emit('room_state', {'players': players}, to=request.sid)

    

# @socketio.on('join_room')
# def handle_join(data):
#     room_code = data['room']
#     if room_code in rooms:
#         rooms[room_code]['players'].append(request.sid)
#         join_room(room_code)
#         emit('joined', {'room': room_code}, room=room_code)
#     else:
#         emit('error', {'message': 'Room not found'})

   
# @socketio.on('leave')
# def on_leave(data):
#     room = data['room']
#     username = data['username']
#     leave_room(room)
#     message = f"User {username} left room {room}"
#     send(message, to=room)
    


if __name__ == '__main__':
    socketio.run(app)