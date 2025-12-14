# game/lobby.py

lobby = {}  # room_id : [user_ids]

def join_lobby(user_id):
    room_id = 1  # for now only ONE room

    if room_id not in lobby:
        lobby[room_id] = []

    if user_id not in lobby[room_id]:
        lobby[room_id].append(user_id)

    return room_id, len(lobby[room_id])
