class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        
        num = len(piles) // 3
        coins = 0

        for i in range(num):
            coins += piles[2*i+1]
        
        return coins
