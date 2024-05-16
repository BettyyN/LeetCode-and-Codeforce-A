class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passanger=[0]*1001
        for num_passanger, initial, final in trips:
            passanger[initial]+=num_passanger
            passanger[final]-=num_passanger
        max_passanger=0
        for num_passanger in passanger:
            max_passanger+=num_passanger
            if max_passanger>capacity:
                return False
        return True
        
