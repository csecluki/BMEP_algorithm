from tabulate import tabulate

roads = []
iteration = 0
queue = []
headers = ["Iteration", "Queue"]
tot = 0
table = []

starting_point = input("Podaj punkt startowy: ")
ending_point = input("Podaj punkt koncowy: ")

headers.append(starting_point)

while True:
    new_record = input("Podaj trase (start_koniec_dlugosc): ")
    if new_record != "":
        new_record = new_record.split(sep=" ")
        roads.append(new_record)
    else:
        break

for i in range(len(roads)):
    # noinspection PyTypeChecker
    roads[i][2] = int(roads[i][2])
    # noinspection PyTypeChecker
    tot += roads[i][2] ** 2

for i in roads:
    if i[0] not in headers:
        headers.append(i[0])

if ending_point not in headers:
    headers.append(ending_point)
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
print("Odpowiedz:")
print("\tdlugosc trasy:", recent[headers.index(ending_point)][0])
print("\tkolejnosc:", answer)
