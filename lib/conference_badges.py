def badge_maker(name):
   return  "Hello, my name is {}.".format(name)

def batch_badge_creator(names):
        return [badge_maker(name) for name in names]

def assign_rooms(names):
    room_assignments = []
    for index, name in enumerate(names, start = 1):
        message = (f"Hello, {name}! You'll be assigned to room {index}!")
        room_assignments.append(message)
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
         print(badge)
    
    rooms = assign_rooms(names)
    for room in rooms:
         print(room)
