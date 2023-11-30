from graph import SocialGraph

def main():
    # Create an instance of the SocialGraph class
    social_graph1 = SocialGraph()
    social_graph2 = SocialGraph()

    # Check if the graph is empty initially
    print(f"Is the graph empty? {social_graph1.is_empty()}")  # Should print: Is the graph empty? True

    # Test adding users
    social_graph1.add_user("Alice")
    social_graph1.add_user("Bob")

    # Test adding relationships
    social_graph1.add_relationship("Alice", "Bob")

    # Print the graph before clearing
    print(f"Graph 1 after creation: {social_graph1}")

    # Check if the graph is empty after adding users and relationships
    print(f"Is the graph empty? {social_graph1.is_empty()}")  # Should print: Is the graph empty? False

    # Add users and relationships to the second graph
    social_graph2.add_user("Alice")
    social_graph2.add_user("Bob")
    social_graph2.add_relationship("Alice", "Bob")

    # Check if the two graphs are equal
    print(f"Are the two graphs equal? {social_graph1 == social_graph2}")  # Should print: Are the two graphs equal? True

    # Test removing a user
    social_graph1.remove_user("Alice")

    # Check if the two graphs are equal after alterating graph1
    print(f"Are the two graphs equal after alterating graph1? {social_graph1 == social_graph2}")  # Should print: Are the two graphs equal? True

    # Check if the graph is empty after removing users
    print(
        f"Is the graph empty? {social_graph1.is_empty()}")  # Should print: Is the graph empty? False (if there are remaining users)

    # Print the graph before clearing
    print(f"Graph before clearing: {social_graph1}")

    # Clear the graph
    social_graph1.clear()

    # Print the graph after clearing
    print(f"Graph after clearing: {social_graph1}")  # Should print: Graph after clearing: {}


if __name__ == "__main__":
    main()