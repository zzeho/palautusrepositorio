"""Unit tests for PlayerStats using a local reader stub."""

import pytest

from index import PlayerStats
from player import Player


class PlayerReaderStub:  # pylint: disable=too-few-public-methods
    """Return a predefined set of players instead of making an API request."""

    def __init__(self, players):
        """Store the players to return from get_players."""
        self._players = players

    def get_players(self):
        """Return the predefined players."""
        return self._players


@pytest.fixture(name="stats")
def player_stats_fixture():
    """Build PlayerStats from a fixed set of test players."""
    players = [
        Player(
            {
                "name": "Finn A",
                "team": "DAL",
                "nationality": "FIN",
                "goals": 10,
                "assists": 20,
            }
        ),
        Player(
            {
                "name": "Finn B",
                "team": "BOS",
                "nationality": "FIN",
                "goals": 20,
                "assists": 5,
            }
        ),
        Player(
            {
                "name": "American",
                "team": "DAL",
                "nationality": "USA",
                "goals": 25,
                "assists": 10,
            }
        ),
        Player(
            {
                "name": "Swede",
                "team": "DAL",
                "nationality": "SWE",
                "goals": 5,
                "assists": 7,
            }
        ),
        Player(
            {
                "name": "Finn C",
                "team": "DAL",
                "nationality": "FIN",
                "goals": 0,
                "assists": 8,
            }
        ),
    ]

    return PlayerStats(PlayerReaderStub(players))


def test_nationality_filter_returns_only_matching_players_and_count(stats):
    """Check nationality filtering and the number of matching players."""
    players = stats.top_scorer_by_nationality("FIN")

    assert len(players) == 3
    assert all(player.nationality == "FIN" for player in players)


def test_nationality_results_are_sorted_by_points_descending(stats):
    """Check nationality results are sorted from most to fewest points."""
    players = stats.top_scorer_by_nationality("FIN")

    assert [player.points for player in players] == [30, 25, 8]


def test_nationality_filter_returns_empty_list_when_no_players_match(stats):
    """Check a nationality with no matches returns an empty list."""
    assert stats.top_scorer_by_nationality("CAN") == []


def test_team_filter_returns_only_matching_players_and_count(stats):
    """Check team filtering and the number of matching players."""
    players = stats.top_scorers_by_team("DAL")

    assert len(players) == 4
    assert all(player.team == "DAL" for player in players)


def test_team_results_are_sorted_by_points_descending(stats):
    """Check team results are sorted from most to fewest points."""
    players = stats.top_scorers_by_team("DAL")

    assert [player.points for player in players] == [35, 30, 12, 8]


def test_players_by_team_returns_the_team_scorers(stats):
    """Check the players_by_team alias returns the same sorted team list."""
    assert stats.players_by_team("DAL") == stats.top_scorers_by_team("DAL")
