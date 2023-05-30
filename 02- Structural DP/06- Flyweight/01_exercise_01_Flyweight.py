class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

class FlyweightFactory:
    _flyweights = {}
    _created = 0

    @staticmethod
    def get_flyweight(shared_state):
        if shared_state not in FlyweightFactory._flyweights:
            FlyweightFactory._flyweights[shared_state]= Flyweight(shared_state)
            FlyweightFactory._created += 1
        return FlyweightFactory._flyweights[shared_state]
        




objs = [
    FlyweightFactory.get_flyweight(1),
    FlyweightFactory.get_flyweight(1),
    FlyweightFactory.get_flyweight(2),
    FlyweightFactory.get_flyweight(1),
    FlyweightFactory.get_flyweight(4),
    FlyweightFactory.get_flyweight(1),
    FlyweightFactory.get_flyweight(16),
    FlyweightFactory.get_flyweight(12),
    FlyweightFactory.get_flyweight(12),
    FlyweightFactory.get_flyweight(121),
    FlyweightFactory.get_flyweight(12),
    FlyweightFactory.get_flyweight(12),
    FlyweightFactory.get_flyweight(12),
]

print("Created Objects", FlyweightFactory._created)
print("Available Flyweight", len(objs))
