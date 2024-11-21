<<<<<<< HEAD
# Network Traffic Analyzer

## Overview
Network Traffic Analyzer is a Python-based tool for analyzing and visualizing network traffic patterns. It provides insights into protocol distribution and identifies top talkers in a network.

## Features
- Analyze protocol distribution in network traffic
- Identify top talkers (most active IP addresses)
- Visualize results with charts and graphs

## Installation
1. Clone the repository:
git clone https://github.com/yourusername/network-traffic-analyzer.git
2. Navigate to the project directory:
cd network-traffic-analyzer
3. Install required dependencies:
pip install -r requirements.txt

## Usage
1. Place your PCAP file in the `data/` directory.
2. Run the analyzer:
```python
from src.analyzer import NetworkAnalyzer
from src.visualizer import TrafficVisualizer

analyzer = NetworkAnalyzer('data/your_traffic_file.pcap')
protocol_count = analyzer.analyze_protocols()
top_talkers = analyzer.get_top_talkers()

TrafficVisualizer.plot_protocol_distribution(protocol_count)
TrafficVisualizer.plot_top_talkers(top_talkers)
=======
# NetworkTrafficAnalyzer-
>>>>>>> origin/main
