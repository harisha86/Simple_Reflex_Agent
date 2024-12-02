class ReflexAgent:
    def __init__(self):
        self.location = 0
        self.performance_score = 0

    def perceive(self, environment_state):
        """Process the current environment state and return a perception"""
        return {
            'current_location': self.location,
            'is_dirty': environment_state[self.location]
        }

    def think(self, perception):
        """Determine action based on perception"""
        if perception['is_dirty']:
            return 'CLEAN'
        elif self.location == 0:
            return 'MOVE_RIGHT'
        else:
            return 'MOVE_LEFT'

    def act(self, action, environment):
        """Execute the chosen action"""
        if action == 'CLEAN':
            environment.clean_location(self.location)
            self.performance_score += 1
        elif action == 'MOVE_RIGHT':
            self.location = 1
            self.performance_score -= 1
        elif action == 'MOVE_LEFT':
            self.location = 0
            self.performance_score -= 1
        
        return self.performance_score