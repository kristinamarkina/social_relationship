import copy
import json
import numpy as np
from pandas import DataFrame


class SocialGraph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        if not isinstance(user, str) or not user:
            raise ValueError("Invalid user name. User name must be a non-empty string.")
        if user in self.graph:
            raise ValueError("User already exists in the graph.")
        self.graph[user] = set()

    def remove_user(self, user):
        if user not in self.graph:
            raise ValueError("User does not exist in the graph.")
        del self.graph[user]
        # Remove any relationships involving the user
        for other_user in self.graph:
            self.graph[other_user].discard(user)

    def add_relationship(self, user1, user2):
        if user1 not in self.graph or user2 not in self.graph:
            raise ValueError("Both users must exist in the graph.")
        if user1 == user2:
            raise ValueError("Cannot create a relationship with the same user.")
        if user2 in self.graph[user1] or user1 in self.graph[user2]:
            raise ValueError("Relationship already exists.")
        self.graph[user1].add(user2)
        self.graph[user2].add(user1)

    def remove_relationship(self, user1, user2):
        if user1 in self.graph and user2 in self.graph[user1]:
            self.graph[user1].remove(user2)
            self.graph[user2].remove(user1)

    def generate_matrix(self, str_=False):
        # create dataframe filled with 0's
        # columns and rows named with users names
        matrix = DataFrame({user: np.zeros(len(self), dtype=int) for user in self.graph},
                           index=[user for user in self.graph])

        # add 1's in appropriate cells to signify a connection
        for user in self.graph:
            for user1 in self.graph[user]:
                matrix[user][user1] = 1

        # return matrix
        if matrix.empty and str_:
            return '[]'

        if str_:
            return str(matrix)

        return matrix

    def is_empty(self):
        return not bool(self.graph)

    def __len__(self):
        return len(self.graph)

    def __eq__(self, other):
        return self.graph == other.graph

    def clear(self):
        self.graph = {}

    def to_json(self):
        # copy graph so changes can be made
        graph = copy.deepcopy(self.graph)

        # add a label for the relationships to the copy graph
        for user in graph:
            graph[user] = {'relationships': list(self.graph[user])}
        return json.dumps(graph, indent=4)

    def __str__(self):
        return self.graph
