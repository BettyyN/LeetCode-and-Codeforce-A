class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}        
        for winner, loser in matches:
            loss_count[winner] = loss_count.get(winner, 0) 
            loss_count[loser] = loss_count.get(loser, 0) + 1
        zero_loss_players = []
        one_loss_players = []
        for player, losses in loss_count.items():
            if losses == 0:
                zero_loss_players.append(player)
            elif losses == 1:
                one_loss_players.append(player)
        zero_loss_players.sort()
        one_loss_players.sort()
        return [zero_loss_players, one_loss_players]
        
        
        
