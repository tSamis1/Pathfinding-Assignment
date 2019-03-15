import copy
class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def aStarEight(maze, start, end):

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    unchecked = []
    checked = []

    # Add the start node
    unchecked.append(start_node)

    # Loop until you find the end
    while len(unchecked) > 0:

        # Get the current node
        current_node = unchecked[0]
        current_index = 0
        for index, item in enumerate(unchecked):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        unchecked.pop(current_index)
        checked.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent

            path = path[::-1] # Return reversed path
            return path[1:len(path)-1]

        # Generate neighbours
        neighbours = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] == 'X':
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            neighbours.append(new_node)

        # Loop through neighbours
        for neighbour in neighbours:

            # neighbour is on the closed list
            for closed_neighbour in checked:
                if neighbour == closed_neighbour:
                    continue

            # Create the f, g, and h values
            neighbour.g = current_node.g + 1
            neighbour.h = max(abs((neighbour.position[0] - end_node.position[0])), abs((neighbour.position[1] - end_node.position[1])))
            neighbour.f = neighbour.g + neighbour.h

            # neighbour is already in the open list
            debug = False
            for unchecked_node in unchecked:
                if neighbour == unchecked_node and neighbour.g >= unchecked_node.g:
                    debug = True
                    continue

            # Add the neighbour to the open list
            if not debug:
                unchecked.append(neighbour)



def aStarFour(maze, start, end):

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    unchecked = []
    checked = []

    # Add the start node
    unchecked.append(start_node)

    # Loop until you find the end
    while len(unchecked) > 0:

        # Get the current node
        current_node = unchecked[0]
        current_index = 0
        for index, item in enumerate(unchecked):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        unchecked.pop(current_index)
        checked.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent

            path = path[::-1] # Return reversed path
            return path[1:len(path)-1]

        # Generate neighbours
        neighbours = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] == 'X':
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            neighbours.append(new_node)

        # Loop through neighbours
        for neighbour in neighbours:

            # neighbour is on the closed list
            for closed_neighbour in checked:
                if neighbour == closed_neighbour:
                    continue

            # Create the f, g, and h values
            neighbour.g = current_node.g + 1
            neighbour.h = abs((neighbour.position[0] - end_node.position[0])) + abs((neighbour.position[1] - end_node.position[1]))
            neighbour.f = neighbour.g + neighbour.h

            # neighbour is already in the open list
            better_path = False
            for unchecked_node in unchecked:
                if neighbour == unchecked_node and neighbour.g >= unchecked_node.g:
                    better_path = True
                    continue

            # Add the neighbour to the open list
            if not better_path:
                unchecked.append(neighbour)

def greedyEight(maze, start, end):

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    unchecked = []
    checked = []

    # Add the start node
    unchecked.append(start_node)

    # Loop until you find the end
    while len(unchecked) > 0:

        # Get the current node
        current_node = unchecked[0]
        current_index = 0
        for index, item in enumerate(unchecked):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        unchecked.pop(current_index)
        checked.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            path = path[::-1]
            return path[1:len(path)-1]

        # Generate neighbours
        neighbours = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] == 'X':
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            neighbours.append(new_node)

        # Loop through neighbours
        for neighbour in neighbours:

            # neighbour is on the closed list
            for closed_neighbour in checked:
                if neighbour == closed_neighbour:
                    continue

            # Create the f, g, and h values
            neighbour.g = current_node.g + 1
            neighbour.h = max(abs((neighbour.position[0] - end_node.position[0])), abs((neighbour.position[1] - end_node.position[1])))
            neighbour.f = neighbour.h

            # neighbour is already in the open list
            for checked_node in unchecked:
                if neighbour == checked_node:
                    continue

            # Add the neighbour to the open list
            unchecked.append(neighbour)

def greedyFour(maze, start, end):

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    unchecked = []
    checked = []

    # Add the start node
    unchecked.append(start_node)

    # Loop until you find the end
    while len(unchecked) > 0:

        # Get the current node
        current_node = unchecked[0]
        current_index = 0
        for index, item in enumerate(unchecked):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        unchecked.pop(current_index)
        checked.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            path = path[::-1]
            return path[1:len(path)-1]

        # Generate neighbours
        neighbours = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] == 'X':
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            neighbours.append(new_node)

        # Loop through neighbours
        for neighbour in neighbours:

            # neighbour is on the closed list
            for closed_neighbour in checked:
                if neighbour == closed_neighbour:
                    continue

            # Create the f, g, and h values
            neighbour.g = current_node.g + 1
            neighbour.h = abs((neighbour.position[0] - end_node.position[0])) + abs((neighbour.position[1] - end_node.position[1]))
            neighbour.f = neighbour.h

            # neighbour is already in the open list
            for checked_node in unchecked:
                if neighbour == checked_node:
                    continue

            # Add the neighbour to the open list
            unchecked.append(neighbour)

# Generate the maps for the algorithms to run on, then run them
def main():
    
    # input and generate the four way movement maps
    input = open("pathfinding_a.txt")
    output = open("pathfinding_a_out.txt", 'w')
    lines = input.readlines()
    lines = [x.strip() for x in lines]
    mapsA = []
    map = []
    for line in lines:
        if line != '':
            map.append(line)
        else:
            newMap = []
            counterRow = 0
            for rows in map:
                row = []
                counterColumn = 0
                for elem in rows:
                    if elem == 'S':
                        start = (counterRow, counterColumn)
                    if elem == 'G':
                        goal = (counterRow, counterColumn)
                    row.append(elem)
                    counterColumn += 1
                newMap.append(row)
                counterRow += 1
            fullMap = [newMap, start, goal]
            mapsA.append(fullMap)
            map = []
    newMap = []
    counterRow = 0
    for rows in map:
        row = []
        counterColumn = 0
        for elem in rows:
            if elem == 'S':
                start = (counterRow, counterColumn)
            if elem == 'G':
                goal = (counterRow, counterColumn)
            row.append(elem)
            counterColumn += 1
        newMap.append(row)
        counterRow += 1
    fullMap = [newMap, start, goal]
    mapsA.append(fullMap)

    # run the 4 way movement algorithms on the maps
    for map in mapsA:
        answer1 = aStarFour(map[0], map[1], map[2])
        answer2 = greedyFour(map[0], map[1], map[2])
        answer_map1 = copy.deepcopy(map[0])
        answer_map2 = copy.deepcopy(map[0])
        output.write('A*\n')
        for position in answer1:
            if position != map[1] or position != map[2]:
                answer_map1[position[0]][position[1]] = 'P'
        for row in answer_map1:
            for elem in row:
                output.write(elem)
            output.write('\n')
        output.write('Greedy\n')
        for position in answer2:
            if position != map[1] or position != [map[2]]:
                answer_map2[position[0]][position[1]] = 'P'
        for row in answer_map2:
            for elem in row:
                output.write(elem)
            output.write('\n')
        output.write('\n')

    # input and generate the eight way movement maps
    input = open("pathfinding_b.txt")
    output = open("pathfinding_b_out.txt", 'w')
    lines = input.readlines()
    lines = [x.strip() for x in lines]
    mapsB = []
    map = []
    for line in lines:
        if line != '':
            map.append(line)
        else:
            newMap = []
            counterRow = 0
            for rows in map:
                row = []
                counterColumn = 0
                for elem in rows:
                    if elem == 'S':
                        start = (counterRow, counterColumn)
                    if elem == 'G':
                        goal = (counterRow, counterColumn)
                    row.append(elem)
                    counterColumn += 1
                newMap.append(row)
                counterRow += 1
            fullMap = [newMap, start, goal]
            mapsB.append(fullMap)
            map = []
    newMap = []
    counterRow = 0
    for rows in map:
        row = []
        counterColumn = 0
        for elem in rows:
            if elem == 'S':
                start = (counterRow, counterColumn)
            if elem == 'G':
                goal = (counterRow, counterColumn)
            row.append(elem)
            counterColumn += 1
        newMap.append(row)
        counterRow += 1
    fullMap = [newMap, start, goal]
    mapsB.append(fullMap)

    # run the 8 way movement algorithms on the maps
    for map in mapsB:
        answer1 = aStarEight(map[0], map[1], map[2])
        answer2 = greedyEight(map[0], map[1], map[2])
        answer_map1 = copy.deepcopy(map[0])
        answer_map2 = copy.deepcopy(map[0])
        output.write('A*\n')
        for position in answer1:
            if position != map[1] or position != map[2]:
                answer_map1[position[0]][position[1]] = 'P'
        for row in answer_map1:
            for elem in row:
                output.write(elem)
            output.write('\n')
        output.write('Greedy\n')
        for position in answer2:
            if position != map[1] or position != [map[2]]:
                answer_map2[position[0]][position[1]] = 'P'
        for row in answer_map2:
            for elem in row:
                output.write(elem)
            output.write('\n')
        output.write('\n')

main()
