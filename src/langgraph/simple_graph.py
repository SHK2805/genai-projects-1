from typing_extensions import TypedDict

class State(TypedDict):
    graph_state: str

class FirstNode:
    def __init__(self, node_state: State):
        self.name = self.__class__.__name__
        self.state = node_state

    def print_state(self):
        print(f"Node Name: {self.name}")
        print(f"Node State: {self.state['graph_state']}")

    def get(self):
        return self.state['graph_state'] + " I am playing"

    def set(self, state: str):
        self.state['graph_state'] = state
        print(f"State set to: {self.state['graph_state']}")

class SecondNode:
    def __init__(self, node_state: State):
        self.name = self.__class__.__name__
        self.state = node_state

    def print_state(self):
        print(f"Node Name: {self.name}")
        print(f"Node State: {self.state['graph_state']}")

    def get(self):
        return self.state['graph_state'] + " Cricket"

    def set(self, state: str):
        self.state['graph_state'] = state
        print(f"State set to: {self.state['graph_state']}")

class ThirdNode:
    def __init__(self, node_state: State):
        self.name = self.__class__.__name__
        self.state = node_state

    def print_state(self):
        print(f"Node Name: {self.name}")
        print(f"Node State: {self.state['graph_state']}")

    def get(self):
        return self.state['graph_state'] + " Tennis"

    def set(self, state: str):
        self.state['graph_state'] = state
        print(f"State set to: {self.state['graph_state']}")