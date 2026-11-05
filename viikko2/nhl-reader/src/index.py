import requests
from player import Player
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorer_by_nationality(self, nationality):
        found_players = []

        for player in self.players:
            if player.nationality == nationality:
                found_players.append(player)

        found_players.sort(key=lambda player: player.points, reverse=True)
        
        return found_players

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    season = Prompt.ask("Choose season", 
        choices=["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"],
        default="2024-25")
    nation = input("Enter nationality (FIN/SWE/CAN/RUS/USA/CZE/FRA/GBR/SVK/LAT/DEN/GET/SUI/NOR): ").upper()
    players = stats.top_scorer_by_nationality(nation)

    console = Console()

    table = Table(title=f"NHL Players from {nation}")

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
