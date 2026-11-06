"""Model an NHL player and their scoring statistics."""


class Player:  # pylint: disable=too-few-public-methods
    """Store a player's identity and scoring information."""

    def __init__(self, dict):  # pylint: disable=redefined-builtin
        """Initialize a player from one API response dictionary."""
        self.name = dict['name']
        self.team = dict['team']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists

    def __str__(self):
        """Return the player's statistics as a formatted line."""
        return f"{self.name:<25}{self.team:<17} {self.goals} + {self.assists} = {self.points}"
