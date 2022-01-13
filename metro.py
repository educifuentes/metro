import sys
import csv
from station import Station

def main():
    # check usage
    # usage: number of args
    if len(sys.argv) < 2 or len(sys.argv) > 5:
        sys.exit("Usage: python metro.py your_map.csv start end [train_color]")

    # set variables
    map_path = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]
    train_color = ''
    if len(sys.argv) != 4:
        train_color = sys.argv[4]

    # load stations into dict
    stations = load_map(map_path)
    # find route
    solution = find_route(stations, start, end, train_color)
    # print route in nice format
    pretty_format_solution = format_solution(solution, start, end, train_color)
    print(pretty_format_solution)

def find_route(stations, start, end, train_color=""):
    """Finds the shortest route between two stations using breadth-first search. Optional argument considering train color."""
    # check correct usage
     # usage - start and end parameters
    if start not in stations.keys() or end not in stations.keys():
        sys.exit("Error: Please enter a valid start or end station")
    # usage - end station can't be reach by express train
    if train_color and stations[end].color and train_color != stations[end].color:
        sys.exit(f'Error: End station {end} ({stations[end].color}) can\'t be reach by train with color {train_color}')
    # usage - correct train color
    if train_color and train_color not in ["red", "green"]:
        sys.exit("Error: Train color must be 'red' or 'green'")

    # shortest path (using breadth-first search)
    # keep track of visited stations
    visited = {}
    # store current station and keep track of current path. tupple: ( current, path)
    queue = []
    # add start station to queue and empty path
    queue.append([start, []])
    # to save final result
    shortest_path = []

    # loop until queue has no elements
    while len(queue) > 0:
        # get first element from queue and unpack it
        current, path = queue.pop(0)

        # stop looping if end station is reached
        if current == end:
            shortest_path = path
            shortest_path.append(current)
            break

        # check if it current has adjacent stations
        if stations[current].next[0]:
            # check adjacent stations of current station
            for adj in stations[current].next:
                if not adj in visited:
                    # log station as visited
                    visited[adj] = True
                    # if train has color, add only compatible stations to path
                    if train_color and stations[adj].color and stations[adj].color != train_color:
                        # check if it adjacent stations to current have adjacent stations
                        if stations[adj].next[0]:
                            # look for adjacent stations for skipped station
                            for next_adj in stations[adj].next:
                                new_path = list(path)
                                new_path.append(current)
                                # add adjacent of skipped station to top of queue
                                queue.insert(0, [next_adj, new_path])
                    # if station cannot be skipped, add to queue
                    else:
                        new_path = list(path)
                        new_path.append(current)
                        queue.append( [adj, new_path])
    return shortest_path

def format_solution(solution, start, end, train_color=""):
    """Returns solution in nice format."""
    route = " - ".join(solution) if solution else f"No route from {start} to {end}"
    # format for train without color
    if train_color == "":
        train_color = "None"
    return f'The route with less stations from station {start} to {end} is:\n{route}\n* Train color: {train_color}'

def load_map(map_path):
    """Load metro map csv file into dictionary of stations."""
    stations = {}
    with open(map_path) as file:
        reader = csv.DictReader(file)
        # iterate over csv rows
        for row in reader:
            row['adj'] = row['adj'].split(";")
            station = Station(row['adj'], row['color'])
            # add to dict only if it has not been stored
            if row['name'] not in stations.keys():
                stations[row['name']] = station
            else:
                # usage - file has duplicated stations
                sys.exit("Error: Map file should not contain duplicated stations")
    return stations

if __name__ == '__main__':
    main()
