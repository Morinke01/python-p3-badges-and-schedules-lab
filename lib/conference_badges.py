def badge_maker(name):
    return (f'Hello, my name is {name}.')

def batch_badge_creator(names):
    return [f'Hello, my name is {name}.' for name in names]

def assign_rooms(names):
    if len(names) > 8:
        raise ValueError("Not enough rooms for all speakers.")

    room_assignments = []

    for room, speaker in zip(range(1, 9), names):
        room_assignments.append(f"Hello, {speaker}! You'll be assigned to room {room}!")

    return room_assignments

def printer(names):
    badge_messages = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    for badge_message in badge_messages:
        print(badge_message)
    
    for room_assignment in room_assignments:
        print(room_assignment)
