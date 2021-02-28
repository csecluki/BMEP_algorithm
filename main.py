import os
import time
import argparse
from tabulate import tabulate


def main(filename):
    headers = ["Iteration", "Queue"]
    table = []
    roads = []
    queue = []
    tot = 0
    iteration = 0

    if os.path.isfile(filename):
        absolute_path = filename
    else:
        absolute_path = os.getcwd() + filename

    with open(absolute_path, "r") as file:
        starting_point = file.readline().strip()
        ending_point = file.readline().strip()
        headers.append(starting_point)
        for line in file:
            road = stripline(line)
            roads.append(road)
            if road[1] not in headers:
                headers.append(road[1])
            tot += road[2] ** 2

    queue.append(starting_point)

    first_row = [iteration, queue, [0, False]]
    first_row.extend([[tot, False] for _ in range(len(headers) - 3)])
    table.append(first_row)

    recent = first_row[:]
    previous = [starting_point]

    while len(queue) > 0:
        new_row = recent[:]
        iteration += 1
        new_row[0] = iteration
        current_node = queue[0]
        current_node_index = headers.index(current_node)
        queue = queue[1:]

        for i in roads:
            start_node = i[0]
            end_node = i[1]
            distance = i[2]
            if start_node == current_node and end_node not in queue:
                if recent[current_node_index][0] + distance < recent[headers.index(end_node)][0]:
                    if end_node in previous:
                        queue.insert(0, end_node)
                    else:
                        previous.append(start_node)
                        queue.append(end_node)
        new_row[1] = queue

        for i in range(2, len(headers)):
            for track in roads:
                start_node = track[0]
                end_node = track[1]
                distance = track[2]
                if start_node == current_node and end_node == headers[i]:
                    if recent[current_node_index][0] + distance < new_row[i][0]:
                        new_row[i] = [recent[current_node_index][0] + distance, current_node]

        recent = new_row[:]
        table.append(new_row)

    answer = ending_point
    while True:
        x = answer[0]
        if type(recent[headers.index(x)][1]) == str:
            path = recent[headers.index(x)][1]
            answer = path + " -> " + answer
        else:
            break

    print()
    print(tabulate(table, headers=headers))
    print()
    print("Answer:")
    print("\tTrack length:", recent[headers.index(ending_point)][0])
    print("\tOrder:", answer)
    print()


def stripline(line):
    strip = line.split()
    return tuple([strip[0], strip[1], int(strip[2])])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Pathfinding BMEP algorithm to find shortest path from starting node "
                                                 "to ending node in directed graph")
    parser.add_argument(
        "-f", "--file",
        help=".txt file with description of graph in given pattern: first line - starting point, "
             "second line - ending point, following lines - roads between nodes "
             "StartNode_EndNode_Distance (example: 'a b 5')",
        required=True
    )
    args = parser.parse_args()
    try:
        t0 = time.time()
        main(args.file)
        print(f"Computed in: {round(time.time() - t0, 6)}s.")
        print()
    except FileNotFoundError:
        print("No such file or directory")
