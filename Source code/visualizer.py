import matplotlib.pyplot as plt

class TrafficVisualizer:
    @staticmethod
    def plot_protocol_distribution(protocol_count):
        plt.figure(figsize=(10, 6))
        plt.bar(protocol_count.keys(), protocol_count.values())
        plt.title('Protocol Distribution')
        plt.xlabel('Protocol')
        plt.ylabel('Count')
        plt.savefig('protocol_distribution.png')
        plt.close()

    @staticmethod
    def plot_top_talkers(top_talkers):
        ips, counts = zip(*top_talkers)
        plt.figure(figsize=(10, 6))
        plt.bar(ips, counts)
        plt.title('Top Talkers')
        plt.xlabel('IP Address')
        plt.ylabel('Packet Count')
        plt.xticks(rotation=45)
        plt.savefig('top_talkers.png')
        plt.close()