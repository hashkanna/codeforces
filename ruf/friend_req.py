class Solution:
    """
    @param ages: The ages
    @return: The answer
    """
    def friendRequest(self, ages):
        # Write your code here
        count=0
        n=len(ages)
        for i in range(n):
            for j in range(i+1,n):
                if ages[j] <= (ages[i]/2)+7:
                    print("1111")
                    break
                elif ages[j]>ages[i]:
                    print("2222")
                    break
                elif ages[j] < 100 and ages[i] > 100:
                    print("3333")
                    break
                else:
                    count+=1
        return count

sol=Solution()
ages=[10,39,50]
print(sol.friendRequest(ages=ages))
