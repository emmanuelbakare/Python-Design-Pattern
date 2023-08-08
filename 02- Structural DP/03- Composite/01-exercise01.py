''' 
COMPOSITE
    - component
    - component
    - COMPOSITE 
        - component
        - component
        - COMPOSITE
            - component
'''

class Component:
    def __init__(self, name):
        self.name = name

    def operation(self):
        print(f'{self.name}: Performing operation')

class Composite:
    def __init__(self, name):
        self.name = name
        self.children = [] 
    
    def add(self, component):
        self.children.append(component)

    def remove(self,component):
        self.children.remove(component)

    def operation(self):
        print(f'{self.name}: Performing operation')
        for child in self.children:
            child.operation()


leaf1 = Component('Leaf 1')
leaf2 = Component('Leaf 2')

composite1 = Composite('Composite 1')
composite1.add(leaf1)
composite1.add(leaf2)

composite2 = Composite('Composite 2')
leaf3 = Component('Leaf 3')
leaf4 = Component('Leaf 4')
leaf5 = Component('Leaf 5')

composite2.add(leaf3)
composite2.add(leaf4)
composite2.add(leaf5)

composite1.add(composite2)

composite1.operation()