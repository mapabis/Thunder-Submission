"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""
from collections import defaultdict
from datetime import datetime

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:

	#setting initial points of data entry
	qualified_games = defaultdict(set)
	game_dates = {}
	
	#collect information for player in said game
	for entry in game_data: 
		gameID = entry['gameID']
		player_ID = entry['playerID']
		dateofGame = entry['gameDate']
		fga = entry['fieldGoal2Attempted']
		fgm = entry['fieldGoal2Made']
		fta = entry['freeThrowAttempted']
		ftm = entry['freeThrowMade']
		threes_attempted = entry['fieldGoal3Attempted']
		threes_made = entry['fieldGoal3Made']

	#points scored by the player
	points = ((2 * fgm) + (3 * threes_made) + ftm)

	#calculate true shooting
	def true_shooting_percentage(fgm, fga, threes_made, threes_attempted, ftm, fta, total_points):
   		 if fga + threes_attempted + fta == 0:
        		return 0  
   		 total_attempts = fga + threes_attempted + (fta * 0.44)  # FT weighted
    			return total_points / (total_attempts * 2)  # TS% formula

	#apply the TS calculation to value of entry
	ts_percentage = true_shooting_percentage(fgm, fga, threes_made, threes_attempted, ftm, fta, points)

	#checks if player's TS applies, and if so, adds the performance to qualified games array
	if true_shooting >= true_shooting_cutoff:
		qualified_games[game_id].add(player_id)

	#store game date for later
	game_dates[game_id] = dateofGame

	#finds where the number of players meeting the cutoff surpasses that of the true shooting cutoff
	qualified_game_ids = [game_id for game_id, players in qualified_games.items() if len(players) >= player_count]

	#returns date of qualified games in reverse order, so the most recent appears first
	qualified_game_ids.sort(key=lambda x: datetime.strptime(game_dates[x], '%m/%d/%Y'), reverse=True)
	
	return qualified_game_ids
	
