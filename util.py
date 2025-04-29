
class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:
    def __init__(self):
        self.frontier = []
        self.states = set()  # <- Add a set to track node states

    def add(self, node):
        self.frontier.append(node)
        self.states.add(node.state)  # <- Track state

    def contains_state(self, state):
        return state in self.states  # <- Much faster

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            self.states.remove(node.state)  # <- Remove from set too
            return node


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            self.states.remove(node.state)  # <- Same here
            return node
