import unittest
import os
from src.visualizer import TrafficVisualizer

class TestTrafficVisualizer(unittest.TestCase):
    def test_plot_protocol_distribution(self):
        protocol_count = {1: 100, 6: 200, 17: 150}
        TrafficVisualizer.plot_protocol_distribution(protocol_count)
        self.assertTrue(os.path.exists('protocol_distribution.png'))

    def test_plot_top_talkers(self):
        top_talkers = [('192.168.1.1', 500), ('10.0.0.1', 300), ('172.16.0.1', 200)]
        TrafficVisualizer.plot_top_talkers(top_talkers)
        self.assertTrue(os.path.exists('top_talkers.png'))

if __name__ == '__main__':
    unittest.main()