from tabulate import tabulate
import argparse
import os


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
        out = queue[0]
        out_index = headers.index(out)
        queue = queue[1:]

        for i in roads:
            if i[0] == out and i[1] not in queue:
                if recent[out_index][0] + i[2] < recent[headers.index(i[1])][0]:
                    if i[1] in previous:
                        queue.insert(0, i[1])
                    else:
                        previous.append(i[0])
                        queue.append(i[1])
        new_row[1] = queue

        for i in range(2, len(headers)):
            for track in roads:
                if track[0] == out and track[1] == headers[i]:
                    if recent[out_index][0] + track[2] < new_row[i][0]:
                        new_row[i] = [recent[out_index][0] + track[2], out]

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
    return (strip[0], strip[1], int(strip[2]))


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
        main(args.file)
    except FileNotFoundError:
        print("No such file or directory")
