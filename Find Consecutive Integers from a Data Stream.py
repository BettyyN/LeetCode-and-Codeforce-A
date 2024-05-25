class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value = value
        self.k = k
        self.stream = []
        self.count = 0

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        self.stream.append(num)
        if num == self.value:
            self.count += 1
        if len(self.stream) > self.k:
            removed = self.stream.pop(0)
            if removed == self.value:
                self.count -= 1
        return self.count == self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
