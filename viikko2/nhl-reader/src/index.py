"""Read NHL player data and display filtered statistics."""

import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player import Player


class PlayerReader:  # pylint: disable=too-few-public-methods
    """Fetch player data and convert it into Player objects."""

    def __init__(self, url):
        """Store the API URL used to retrieve player data."""
        self.url = url

    def get_players(self):
        """Fetch and return all players from the configured API URL."""
        response = requests.get(self.url, timeout=None).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players


class PlayerStats:
    """Provide filtering and sorting operations for NHL players."""

    def __init__(self, reader):
        """Load players from the given reader."""
        self.players = reader.get_players()

    def top_scorer_by_nationality(self, nationality):
        """Return players of the given nationality, sorted by points."""
        found_players = []

        for player in self.players:
            if player.nationality == nationality:
                found_players.append(player)

        found_players.sort(key=lambda player: player.points, reverse=True)

        return found_players

    def top_scorers_by_team(self, team):
        """Return players on the given team, sorted by points."""
        team_players = []

        for player in self.players:
            if player.team == team:
                team_players.append(player)

        team_players.sort(key=lambda player: player.points, reverse=True)

        return team_players

    def players_by_team(self, team):
        """Return players on the given team in descending point order."""
        return self.top_scorers_by_team(team)


def main():
    """Prompt for a filter and display matching players in a Rich table."""
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    _season = Prompt.ask(
        "Choose season",
        choices=[
            "2018-19",
            "2019-20",
            "2020-21",
            "2021-22",
            "2022-23",
            "2023-24",
            "2024-25",
            "2025-26",
        ],
        default="2024-25",
    )

    filter_choice = input("Filter by nationality (N) or team (T)? ").strip().upper()

    if filter_choice == "T":
        team = input("Enter team abbreviation (for example TOR, BOS, FLA): ").upper()
        players = stats.top_scorers_by_team(team)
        title = f"NHL Players from {team}"
    else:
        nation_prompt = (
            "Enter nationality "
            "(FIN/SWE/CAN/RUS/USA/CZE/FRA/GBR/SVK/LAT/DEN/GET/SUI/NOR): "
        )
        nation = input(nation_prompt).upper()
        players = stats.top_scorer_by_nationality(nation)
        title = f"NHL Players from {nation}"

    console = Console()

    table = Table(title=title)

    table.add_column("Player", style="cyan")
    table.add_column("Team", style="magenta")
    table.add_column("Goals", style="green", justify="right")
    table.add_column("Assists", style="green", justify="right")
    table.add_column("Points", style="bold green", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points))

    console.print(table)


if __name__ == "__main__":
    main()
