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
            for j in range(n):
                if i!=j:
                    if ages[j] <= (ages[i]//2)+7:
                        #print("1111")
                        pass
                    elif ages[j]>ages[i]:
                        # print("2222")
                        pass
                    elif ages[j] < 100 and ages[i] > 100:
                        #print("3333")
                        pass
                    else:
                        count+=1
                        print(ages[i], ages[j])
        return count

sol=Solution()
ages=[101,79,102]
print(sol.friendRequest(ages=ages))
