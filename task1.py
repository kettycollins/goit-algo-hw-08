import heapq

def min_connection_cost(network_cables):
    heapq.heapify(network_cables)

    total_cost = 0
    while len(network_cables) > 1:
        network_cable1 = heapq.heappop(network_cables)
        network_cable2 = heapq.heappop(network_cables)
        combined_network_cables = network_cable1 + network_cable2
        total_cost += combined_network_cables

        heapq.heappush(network_cables, combined_network_cables)

    return total_cost