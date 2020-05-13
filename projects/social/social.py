import sys
import random
from math import factorial

sys.path.append("../graph")

from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        # Used as id of new users (auto incremented in add_user)
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif (
            friend_id in self.friendships[user_id]
            or user_id in self.friendships[friend_id]
        ):
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def get_friends(self, user_id):
        """
        Returns direct friendships to user_id
        """
        if self.friendships.get(user_id):
            return self.friendships[user_id]
        else:
            return None

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Previously visited nodes
        visited = set()

        queue = Queue()

        # Enqueue starting vertex (start of search)
        queue.enqueue([starting_vertex])

        # Continue until queue is empty (meaning the destination wasn't found)
        # OR we return a valid path
        while queue.size() != 0:
            # Get path
            path = queue.dequeue()
            # We want to find neighbors of last appended vertex
            current_vertex = path[-1]

            # Check if destination reached
            if current_vertex == destination_vertex:
                # Return shortest path
                return path
            else:
                # Check if visited
                if current_vertex not in visited:
                    # Don't wanna get stuck in a forever looping cycle
                    visited.add(current_vertex)
                    # Go thru neighbors
                    for vertex in self.get_friends(current_vertex):
                        if vertex not in visited:
                            # Build a new path from previous path, and add this vertex
                            new_path = path.copy()
                            new_path.append(vertex)
                            # Add to queue for processing in next iteration
                            queue.enqueue(new_path)
        # No path found case
        return None

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # The number of users must be greater than the average number of friendships.
        if num_users <= avg_friendships:
            return None

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        friendship_combinations = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                friendship_combinations.append((user_id, friend_id))

        random.shuffle(friendship_combinations)

        for i in range(num_users * avg_friendships // 2):
            friendship = friendship_combinations[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        """

        queue = Queue()
        queue.enqueue([user_id])

        visited = {}

        while queue.size() > 0:
            path = queue.dequeue()

            # Get last node
            vertex = path[-1]

            # Do work if not already in visited dict
            if vertex not in visited:
                visited[vertex] = path

                for friend in self.get_friends(vertex):
                    # Build path for each friend at current path
                    new_path = path.copy()
                    new_path.append(friend)
                    # Enqueue this path
                    queue.enqueue(new_path)

        return visited


if __name__ == "__main__":
    sg = SocialGraph()
    sg.populate_graph(10, 3)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)