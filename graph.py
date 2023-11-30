class SocialGraph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        # Implement logic to add a user to the graph
        self.graph[user] = set()

    def remove_user(self, user):
        # Implement logic to remove a user from the graph
        if user in self.graph:
            del self.graph[user]
            # Remove any relationships involving the user
            for other_user in self.graph:
                self.graph[other_user].discard(user)

    def add_relationship(self, user1, user2):
        # Implement logic to add a relationship between users
        if user1 in self.graph and user2 in self.graph:
            self.graph[user1].add(user2)
            self.graph[user2].add(user1)

    def is_empty(self):
        # Check if the graph is empty
        return not bool(self.graph)

    def __len__(self):
        # Return the number of users in the graph
        return len(self.graph)

    def __eq__(self, other):
        # Check if two SocialGraph instances are equal
        return self.graph == other.graph

    def __str__(self):
        # Return a string representation of the graph
        users = list(self.graph.keys())
        matrix = [[0] * len(users) for _ in range(len(users))]

        for i, user1 in enumerate(users):
            for j, user2 in enumerate(users):
                if user2 in self.graph[user1]:
                    matrix[i][j] = 1

        result = "Relationship Matrix:\n"
        result += "    " + " ".join(users) + "\n"

        for i, row in enumerate(matrix):
            result += users[i] + "   " + " ".join(map(str, row)) + "\n"

        return result

    def clear(self):
        # Clear the graph by removing all users and relationships
        self.graph = {}