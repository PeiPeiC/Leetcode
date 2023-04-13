 """
 860. Lemonade Change
 
 ● Intuition:
   pay ＄5-> no change needed
   pay ＄10-> change ＄5
   pay ＄20-> change ＄15
   
 ● Time complexity of O(N)
 ● Space complexity of O(1)
   
  """
 #Original version
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0,10:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                change[5]+=1
            if bills[i]== 10:
                if change[5] > 0:
                    change[10]+=1
                    change[5]-=1
                else : 
                    return False

            if bills[i]== 20:
                if change[10]> 0 and change[5]>0:
                    change[5]-=1
                    change[10]-=1
                elif change[5]>=3:
                    change[5]-=3
                else: 
                    return False 
        return True

#Optimised version
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
