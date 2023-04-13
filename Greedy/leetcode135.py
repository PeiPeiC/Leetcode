class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i]>ratings[i+1] and candies[i] <= candies[i+1] :
                candies[i] = candies[i+1]+1
            if ratings[i]<ratings[i+1] and candies[i+1] <= candies[i] :
                candies[i+1] = candies[i]+1
        for i in range(len(ratings)-1,0,-1):
            if ratings[i]> ratings[i-1] and candies[i] <= candies[i-1] :
                candies[i] = candies[i-1]+1
            if ratings[i]<ratings[i-1] and candies[i-1] <= candies[i] :
                candies[i-1] = candies[i]+1
        #print(f'candies{candies}')
        candies_sum = 0
        for i in range(len(candies)):
            candies_sum += candies[i]
        return candies_sum
      
#Optimised version
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        # forward pass
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # backward pass
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
