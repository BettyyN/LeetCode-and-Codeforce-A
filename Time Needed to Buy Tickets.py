class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:  
        n=len(tickets)
        ticketQueue=deque(enumerate(tickets))
        time=0
        while ticketQueue:
            index,curr_ticket=ticketQueue.popleft()
            curr_ticket-=1
            time+=1
            if curr_ticket>0:
                ticketQueue.append((index,curr_ticket))
            if index==k and curr_ticket==0:
                return time
            
                
        

    
        
        
