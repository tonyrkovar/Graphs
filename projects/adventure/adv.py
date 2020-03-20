from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

    # You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"


# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def room_traversal(player):
    q = Queue()
    q.enqueue(player.current_room)

    visited = {}
    for room in room_graph:
        visited[room] = {}
        for direction in room_graph[room][1]:
            visited[room][direction] = '?'

    print(visited)

    last_room = 0
    current_exits = player.current_room.get_exits()

    def traverse(move):
        traversal_path.append(move)

        last_room = player.current_room.id
        next_direction = player.current_room.get_room_in_direction(move)
        print('pop')
        print(len(q.queue))
        if next_direction is None:
            print("That's a wall dummy")
            return

        player.travel(move)
        q.enqueue(player.current_room)
        visited[last_room][move] = player.current_room.id

    while q.size() > 0:
        current_room = q.dequeue()
        current_exits = current_room.get_exits()
        cr_id = current_room.id

        if len(current_exits) == 1:
            traverse(current_exits[0])
        else:
            for i in visited[cr_id]:
                if visited[cr_id][i] is '?':
                    traverse(i)

    print(cr_id, "last room id")
    print(visited)
# Start at a single room, then you want to pick a direction to move.
# If you move north(based off the test loop file) you will reach a dead end after 2 moves.
# I need to traverse the rooms in a way that will have me touch every room, atleast once.
# What do I track here?
# I currently have a dictionary that has all of the room ID's along with
#  avalible paths(paths_from_room)
# Write a conditional that will check if a room is a dead end
# Write a condition/track a variable that will ensure i do not repeat paths.


room_traversal(player)
print(traversal_path)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
