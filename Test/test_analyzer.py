import unittest
from src.analyzer import NetworkAnalyzer

class TestNetworkAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = NetworkAnalyzer('data/sample_traffic.pcap')

    def test_analyze_protocols(self):
        protocol_count = self.analyzer.analyze_protocols()
        self.assertIsInstance(protocol_count, dict)
        self.assertTrue(len(protocol_count) > 0)

    def test_get_top_talkers(self):
        top_talkers = self.analyzer.get_top_talkers()
        self.assertIsInstance(top_talkers, list)
        self.assertEqual(len(top_talkers), 5)

if __name__ == '__main__':
    unittest.main()