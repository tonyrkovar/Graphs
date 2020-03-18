from util import Stack, Queue


def get_earliest(ancestors):
    is_earliest = set()
    for person in ancestors:
        is_earliest.add(person[0])
    for person in ancestors:
        if person[1] in is_earliest:
            is_earliest.remove(person[1])
    return is_earliest


def earliest_ancestor(ancestors, starting_node):
    q = Queue()

    q.enqueue([starting_node])

    visited = set()

    earliest = get_earliest(ancestors)

    avalible_paths = []

    longest_path = []

    while q.size() > 0:
        current_path = q.dequeue()
        if len(current_path) > len(longest_path):
            longest_path = current_path

        current_child = current_path[-1]

        if starting_node in earliest:
            return -1
        if current_child in earliest:
            avalible_paths.append(current_path)
        if current_child not in visited:
            visited.add(current_child)
            for person in ancestors:
                if person[1] == current_child:
                    q.enqueue([*current_path, person[0]])
    print(avalible_paths)

    return longest_path[-1]


"""
Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.
"""
# The function will take in a list of Tuples dictating ancestry relations IE: (1, 3), (2, 3), (3, 6)
# For the person at 3 they will have relations set up 1 -> 3, 2 -> 3, 3 -> 6
# In the tuple the first value will be the "parent" the second value will be the "child"
# Travers the ancestors list w/ a for loop(Shown above currently.)
# Track the path taken to get to the earliest known ancestor IE: Longest path, (I will probably want use len(path))
