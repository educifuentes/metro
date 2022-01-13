import unittest
import metro
from station import Station

class TestCalc(unittest.TestCase):
    """Unit tests for metro.py. """

    def test_path_easy(self):
        # tests route solution for a simple 4-stations map
        stations = metro.load_map('maps/easy.csv')
        # easy - train no color
        self.assertEqual(metro.find_route(stations, 'A', 'D'), ['A','B','C','D'])
        # easy - train red
        self.assertEqual(metro.find_route(stations, 'A', 'D', 'red'), ['A','C','D'])
        # easy - train green
        self.assertEqual(metro.find_route(stations, 'A', 'D', 'green'), ['A','B','D'])

    def test_path_example(self):
        # test route solution for example map
        stations = metro.load_map('maps/example.csv')
        # example - train no color
        self.assertEqual(metro.find_route(stations, 'A', 'F'), ['A','B','C','D','E','F'])
        # example - train red
        self.assertEqual(metro.find_route(stations, 'A', 'F', 'red'), ['A','B','C','H','F'])
        # example - train green
        self.assertEqual(metro.find_route(stations, 'A', 'F', 'green'), ['A','B','C','G','I','F'])

    def test_no_path(self):
        # test that empty path is returned when no route is possible
        stations = metro.load_map('maps/example.csv')
        # example - train no color
        self.assertEqual(metro.find_route(stations, 'H', 'A'), [])
        # example - train no color
        self.assertEqual(metro.find_route(stations, 'F', 'C', 'green'), [])

    def test_path_example_sub_routes(self):
        # tests route solution for stations in between the network
        stations = metro.load_map('maps/example.csv')
        # sub-route no color
        self.assertEqual(metro.find_route(stations, 'C', 'F'), ['C','D','E', 'F'])
        # sub-route red
        self.assertEqual(metro.find_route(stations, 'C', 'F', 'red'), ['C','H','F'])
        # sub-route green
        self.assertEqual(metro.find_route(stations, 'C', 'F', 'green'), ['C','G','I','F'])

    def test_read_map_file(self):
        # test correct reading of csv into dictionary
        stations = metro.load_map('maps/example.csv')
        # correct number of stations
        self.assertEqual(len(stations), 9)
        # check station attributes - adjacent stations list
        self.assertEqual(stations['A'].next, ['B'])
        # check station attributes - empty adjacent stations list
        self.assertEqual(stations['F'].next, [''])
        # check attributes - color
        self.assertEqual(stations['H'].color, 'red')
        # check attributes - empty color
        self.assertEqual(stations['A'].color, '')

    def test_duplicated_stations(self):
        # test program exit if input file have duplicated stations
        with self.assertRaises(SystemExit) as cm:
            metro.load_map('maps/duplicated_stations.csv')
        self.assertEqual(cm.exception.code, "Error: Map file should not contain duplicated stations")

    def test_usage_end_station(self):
        # test program exit when end station can't be reach by express train
        stations = metro.load_map('maps/end_red.csv')
        with self.assertRaises(SystemExit) as cm:
            metro.find_route(stations, 'A', 'D', 'green')
        self.assertEqual(cm.exception.code, "Error: End station D (red) can't be reach by train with color green")

    def test_usage_valid_stations(self):
        # test if not valid start or end stations are given as parameters
        stations = metro.load_map('maps/example.csv')
        # start station not in map
        with self.assertRaises(SystemExit) as cm:
            metro.find_route(stations, 'O', 'D')
        self.assertEqual(cm.exception.code, "Error: Please enter a valid start or end station")
        # end station not in map
        with self.assertRaises(SystemExit) as cm:
            metro.find_route(stations, 'A', 'Z')
        self.assertEqual(cm.exception.code, "Error: Please enter a valid start or end station")
        # both end and start stations not in map
        with self.assertRaises(SystemExit) as cm:
            metro.find_route(stations, 'O', 'Z')
        self.assertEqual(cm.exception.code, "Error: Please enter a valid start or end station")

    def test_usage_train_color(self):
        # test program exit if not valid rain color is given as parameter
        stations = metro.load_map('maps/example.csv')
        with self.assertRaises(SystemExit) as cm:
            metro.find_route(stations, 'A', 'F', 'black')
        self.assertEqual(cm.exception.code, "Error: Train color must be 'red' or 'green'")


# to be able to run with python3 test_metro.py
if __name__ == '__main__':
    unittest.main()
