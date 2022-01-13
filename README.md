# metro

Finds the route with less stations between two stations of a metro network using breadth-first search (BFS). Stations can also have color (red or green). An "express" metro train (with color red or green) will stop only on the non-colored stations and the ones matching its color.  The direction of the metro train is only forward.

## Usage

Run:

```shell
$ python3 metro.py maps/your_map.csv start_station end_station [train_color]
```

- Optional argument `train_color` must be "red" or "green"

### Input stations file

Stations must be submitted in a `.csv` file, indicating the station name, adjacent stations (`adj`) and color (in that order). Maps must be placed on the maps/ directory.

- The list of adjacent stations must be separated with a semicolon (;)
- If station has no color o adjacent stations, leave blank

Sample input file:

```tex
name,adj,color
A,B,
B,C,
C,D;G,
D,E,
```
- station C has two adjacent stations: D and G


### Running tests

```
python3 test_metro.py
```
