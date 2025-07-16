import uuid


def generate_room_code(rooms):

    while True:
        code = uuid.uuid4().hex[:4].upper()  
        if not code in rooms:
            return code  
