from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


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


# def get_unvisited(room):
#     for path in room:
#         # print(room[path])
#         if room[path] == '?':
#             return path


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


opposite = {
    'n': 's',
    'w': 'e',
    'e': 'w',
    's': 'n'
}


# def get_unvisited(room):

"""
Depth First Traversal that takes in the player object, extracts the current room(should be the starting room)
and traverses the maze until it hits a deadend or a room where all of the adjacent rooms have been visited.
"""


def traverse_rooms(room):
    visited = []
    s = Stack()
    s.push(room.id)
    while s.size() > 0:
        room = s.pop()
        if room not in visited:
            visited.append(room)
            room_exits = room_graph[room][1]
            for direction in room_exits:
                if room_exits[direction] not in visited:
                    s.push(room_exits[direction])
    return visited


"""
Breadth First Search that takes in the room ID's and looks for the shortest path to the next unvisited room.
"""


def shortest_route(starting_room, destination_room):
    print(
        f'starting_room: {starting_room}, destination_room: {destination_room}')
    q = Queue()
    q.enqueue([starting_room])
    visited = set()
    while q.size() > 0:
        current_path = q.dequeue()
        current_room = current_path[-1]
        if current_room not in visited:
            visited.add(current_room)
            if current_room == destination_room:
                return current_path
            room_exits = room_graph[current_room][1]
            for direction in room_exits:
                q.enqueue([*current_path, room_exits[direction]])


def player_traversal(player):
    """
    Runs traverse room(DFT) that returns an array to help build the Traversal Path list by moving
    the player along the path returned from traverse rooms.

    Move the player along the path returned from traverse rooms, appending each movement to
    traversal_path, when the method reaches a "Dead end", run a BFS to find the next unvisited room.
    """

    path = traverse_rooms(player.current_room)
    for i in range(len(path) - 1):
        current_room = player.current_room

        exits = current_room.get_exits()
        path_to_next = shortest_route(path[i], path[i+1])
        print(f'{path_to_next}, Return from bfs')
        for i in range(len(path_to_next) - 1):
            path_exits = room_graph[path_to_next[i]][1]
            print(path_exits, path_to_next[i])
            for direction in path_exits:
                if path_exits[direction] == path_to_next[i + 1]:
                    player.travel(direction)
                    traversal_path.append(direction)
                else:
                    pass


"""
The BFS I want to write will take in the current room ID and then the next room ID in my "path" array, and find the shorted route to get to that room.
"""


# TRAVERSAL TEST
player_traversal(player)
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
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms {len(traversal_path)} ")
