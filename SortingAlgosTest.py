import unittest
from tutorial import DrawingInformation  # Adjust import path if needed
from BubbleSort import BubbleSort  # Adjust import path if needed

class MyTestCase(unittest.TestCase):
    def test_something(self):
        demo_game_info = DrawingInformation(800, 600, [3, 2, 1])
        bubble_sort = BubbleSort(demo_game_info, True)
        self.assertEqual([2, 3, 1], bubble_sort.__next__())  # Check the state after one iteration
        self.assertEqual([2, 1, 3], bubble_sort.__next__())  # Check the state after another iteration
        self.assertEqual([1, 2, 3], bubble_sort.__next__())  # Check the final sorted state

if __name__ == '__main__':
    unittest.main()
