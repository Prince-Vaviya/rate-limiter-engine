class StateManager:

    def __init__(self):
        self.states = {}

    def create_state(self, client_id, resource_id, limiter):
        key = (client_id, resource_id)

        if key in self.states:
            raise ValueError("State already exists")

        self.states[key] = limiter

    def get_state(self, client_id, resource_id):
        key = (client_id, resource_id)

        if key not in self.states:
            raise ValueError("State not found")

        return self.states[key]

    def remove_state(self, client_id, resource_id):
        key = (client_id, resource_id)

        if key not in self.states:
            raise ValueError("State not found")

        del self.states[key]

    def has_state(self, client_id, resource_id):
        key = (client_id, resource_id)

        return key in self.states