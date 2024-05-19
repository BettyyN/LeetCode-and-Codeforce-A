class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]
        print(times)
        fleets = 0
        last_time = 0
        for time in times:
            if time > last_time:
                fleets += 1
                last_time = time
        
        return fleets
            
        
        
