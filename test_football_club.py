import pytest
from football_club import Player, MatchResult, FootballClub


@pytest.fixture
def football_club() -> FootballClub: 
    """
    Create object FootballClub.

    @return:
        football_club (FootballClub): The FootballClub instance
    """
    return FootballClub("FC Test")

@pytest.fixture
def player():
    """
    Create object Player.

    @return:
        player (Player): The Player instance.
    """
    return Player("Test Player", "Forward", 10)

def test_add_player(football_club, player: Player) -> None:
    """
    Test adding a player to the FootballClub.
    
    @param:
        football_club (FootballClub): The FootballClub instance.
        player (Player): The player to add.

    @return:
        bool: True if the player was added, False if the player's number is already taken.
    """
    result = football_club.add_player(player)
    assert result is True

    assert player in football_club.players
    
def test_remove_player(football_club) -> None:
    """
    Test removing a player from the FootballClub.
    
    @param:
        football_club (FootballClub): The FootballClub instance.
    """
    player = Player("Test Player", "Forward", 10)
    football_club.add_player(player)
    
    football_club.remove_player("Test Player")
    assert len(football_club.players) == 0

def test_record_match_result(football_club) -> None:
    """
    Test recording a match result in the FootballClub.
    
    @param:
        football_club (FootballClub): The FootballClub instance.
    """
    match_result = MatchResult("2023-01-01", "Win", "3-1", "Opponent")
    
    football_club.record_match_result(match_result)
    assert "2023-01-01" in football_club.match_results

def test_get_player_info(football_club) -> None:
    """
    Test getting player information from the FootballClub.
    
    @param:
        football_club (FootballClub): The FootballClub instance.
    """
    player = Player("Test Player", "Forward", 10)
    football_club.add_player(player)
    
    player_info = football_club.get_player_info("Test Player")
    assert "Name: Test Player" in player_info

@pytest.mark.parametrize("finances, expected_result", [(100000, True)])
def test_transfer_player(football_club, finances: float, expected_result: bool):
    """
    Test transferring a player to another club in the FootballClub.
    
    @param:
        football_club (FootballClub): The FootballClub instance.
        finances (float): The initial finances of the club.
        expected_result (bool): The expected result of the transfer.
    """
    football_club.finances = finances
    
    club2 = FootballClub("FC Test 2")
    player = Player("Test Player", "Forward", 10)
    football_club.add_player(player)
    
    result = football_club.transfer_player("Test Player", club2, 50000)
    
    assert player not in football_club.players

    assert player in club2.players
    
    if expected_result:
        assert football_club.finances == finances - 50000
        assert club2.finances == 50000
    else:
        assert football_club.finances == finances
        assert club2.finances == 0

def test_update_finances(football_club) -> None:
    """
    Test updating finances in the FootballClub.
    
    @param:
        football_club (FootballClub): The FootballClub instance.
    """
    football_club._update_finances(10000)
    assert football_club.finances == 10000

@pytest.mark.parametrize("finances, expected_result", [(10000, True), (-5000, False)])
def test_is_financial_transaction_valid(football_club, finances: int, expected_result: bool) -> None:
    """
    Test the validity of a financial transaction in the FootballClub.
    
    @param:
        football_club (FootballClub): The FootballClub instance.
        finances (int): The financial transaction amount.
        expected_result (bool): The expected result of the transaction validity.
    """
    football_club.finances = finances
    
    result = football_club._is_financial_transaction_valid(-5000)
    assert result == expected_result

if __name__ == "__main__":
    pytest.main()