async_mode = None

import os

import socketio
from online_users import online_users
from messenger_backend.models import Conversation

basedir = os.path.dirname(os.path.realpath(__file__))
sio = socketio.Server(async_mode=async_mode, logger=False)
thread = None


@sio.event
def connect(sid, environ):
    sio.emit("my_response", {"data": "Connected", "count": 0}, room=sid)


@sio.on("go-online")
def go_online(sid, user_id):
    if user_id not in online_users:
        online_users.append(user_id)
    sio.emit("add-online-user", user_id, skip_sid=sid)


@sio.on("new-message")
def new_message(sid, message):
    sio.emit(
        "new-message",
        {"message": message["message"], "sender": message["sender"]},
        skip_sid=sid,
    )


@sio.on("logout")
def logout(sid, user_id):
    if user_id in online_users:
        online_users.remove(user_id)
    sio.emit("remove-offline-user", user_id, skip_sid=sid)


@sio.on("clear-unread")
def clear_unread(sid, other_user_id, conversation_id):
	conversation = Conversation.objects.filter(id=conversation_id).first() if conversation_id else None
	if conversation == None: 
		return
	if conversation.user1 and conversation.user1.id != other_user_id:
		conversation.user1Unread = 0
	elif conversation.user2 and conversation.user2.id != other_user_id:
		conversation.user2Unread = 0
	conversation.save()