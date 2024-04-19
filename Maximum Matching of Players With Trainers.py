class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        max_matchings = 0
        player_index = 0
        trainer_index = 0
        while player_index < len(players) and trainer_index < len(trainers):
            if players[player_index] <= trainers[trainer_index]:
                max_matchings += 1
                player_index += 1
                trainer_index += 1
            else:
                trainer_index += 1

        return max_matchings
        
