import heapq

with open("day12input.txt") as infile:
    data = infile.read().split('\n')

grid = []
start, end = [], []
for i in range(len(data)):
    temp = list(data[i])
    for j in range(len(temp)):
        temp[j] = ord(temp[j])
        if temp[j] == 83:
            start = (i, j)
            temp[j] = 97
        elif temp[j] == 69:
            end = (i, j)
            temp[j] = 122
    grid.append(temp)


def solve_puzzle(board, source, destination):
    """This function takes a board and a starting and end destination and returns how many spaces it will take to move
    from the starting square to the destination square"""

    rows = len(board)
    columns = len(board[0])

    # If an empty list is entered
    if columns == 0 or rows == 0:
        return 0
    elif source == destination:
        return 0

    adjacency_dict = {}
    for row in range(rows):
        for col in range(columns):
            adjacency_dict[(row, col)] = {}
            if col > 0 and board[row][col - 1] <= (board[row][col] + 1):
                adjacency_dict[(row, col)][(row, col - 1)] = ('L', 1)
            if col < columns - 1 and board[row][col + 1] <= (board[row][col] + 1):
                adjacency_dict[(row, col)][(row, col + 1)] = ('R', 1)
            if row > 0 and board[row - 1][col] <= (board[row][col] + 1):
                adjacency_dict[(row, col)][(row - 1, col)] = ('U', 1)
            if row < rows - 1 and board[row + 1][col] <= (board[row][col] + 1):
                adjacency_dict[(row, col)][(row + 1, col)] = ('D', 1)

    # Dijkstra's algorithm
    distances = {square: ['', float('inf')] for square in adjacency_dict}
    distances[source] = ['', 0]

    priority_queue = [(0, '', source)]
    while len(priority_queue) > 0 and distances[destination][1] == float('inf'):
        current_distance, current_path, current_square = heapq.heappop(priority_queue)

        if current_distance > distances[current_square][1]:
            continue

        for neighbor, values in adjacency_dict[current_square].items():
            direction = values[0]
            weight = values[1]
            distance = current_distance + weight
            path = current_path + direction

            if distance < distances[neighbor][1]:
                distances[neighbor][1] = distance
                distances[neighbor][0] = path
                heapq.heappush(priority_queue, (distance, path, neighbor))

    return distances[destination][1]


print(solve_puzzle(grid, start, end))
