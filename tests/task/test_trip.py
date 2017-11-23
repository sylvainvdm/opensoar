import os
import unittest

import datetime

from OpenSoar.task.trip import Trip
from tests.task.helper_functions import get_race_task, get_trace


class TestTrip(unittest.TestCase):
    """
    This testcase covers a completed race task.
    """

    igc_path = os.path.join('tests', 'example.igc')
    race_task = get_race_task(igc_path)
    trace = get_trace(igc_path)
    trip = Trip(race_task, trace, list())

    def test_number_of_fixes(self):
        self.assertEqual(len(self.trip.fixes), 5)

    def test_distances(self):
        self.assertListEqual(self.trip.distances, self.race_task.distances)

    def test_outlanded(self):
        self.assertFalse(self.trip.outlanded())

    def test_start_time(self):
        # todo: confirm with seeyou that this is the incorrect start-time
        # todo: check why this value is different
        start_fix = self.trip.fixes[0]
        self.assertEqual(start_fix['time'], datetime.time(12, 12, 55))

    def test_finish_time(self):
        finish_fix = self.trip.fixes[-1]
        self.assertEqual(finish_fix['time'], datetime.time(13, 21, 58))