class RoutingStrategy:
    def route(self, source, destination):
        pass


class FastestRouteStrategy(RoutingStrategy):
    def route(self, source, destination):
        print(f"Calculating fastest route from {source} to {destination}")
        # Implementation of fastest route calculation algorithm goes here

class ShortestRouteStrategy(RoutingStrategy):
    def route(self, source, destination):
        print(f"Calculating shortest route from {source} to {destination}")
        # Implementation of shortest route calculation algorithm goes here

class TollAvoidanceStrategy(RoutingStrategy):
    def route(self, source, destination):
        print(f"Calculating route from {source} to {destination} avoiding tolls")
        # Implementation of toll avoidance route calculation algorithm goes here


class NavigationSystem:
    def __init__(self, routing_strategy):
        self.routing_strategy = routing_strategy

    def set_routing_strategy(self, routing_strategy):
        self.routing_strategy = routing_strategy

    def get_directions(self, source, destination):
        self.routing_strategy.route(source, destination)

#client 
source = "A"
destination = "B"


# Create the NavigationSystem object
navigation_system = NavigationSystem(FastestRouteStrategy())
navigation_system.get_directions(source, destination) 


# Change the strategy to Shortest Route
navigation_system.set_routing_strategy(ShortestRouteStrategy())
navigation_system.get_directions(source, destination) 


# Change the strategy to Toll Avoidance
navigation_system.set_routing_strategy(TollAvoidanceStrategy())
navigation_system.get_directions(source, destination)