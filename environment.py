class Environment:
    def __init__(self):
        # Initialize a two-room environment
        # True means dirty, False means clean
        self.state = [True, True]
    
    def get_state(self):
        """Return the current state of the environment"""
        return self.state
    
    def clean_location(self, location):
        """Clean the specified location"""
        self.state[location] = False
    
    def is_clean(self):
        """Check if all locations are clean"""
        return not any(self.state)
    
    def print_state(self):
        """Display the current state of the environment"""
        state_repr = []
        for i, is_dirty in enumerate(self.state):
            status = "Dirty" if is_dirty else "Clean"
            state_repr.append(f"Room {i}: {status}")
        print(" | ".join(state_repr))