class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices)<=1):
            return 0
        if(len(prices)==2):
            if(prices[0]<prices[1]):
                return prices[1]-prices[0]
            else:
                return 0
        i=0
        mProfit = 0
        #for j in range (1,len(prices)-1):
        j=1
        while (j<=len(prices)-1):
            if prices[i] < prices[j]:
                    #special case we only have two numbers
                    #parse again after j to find a lower number
                    found=False

                    largestNumber=prices[j]
                    for k in range (j+1,len(prices)):
                        #Store largest number
                        if(largestNumber<prices[k]):
                            largestNumber=prices[k]
                        if prices[k] < prices[j]:
                            #this means we can use this value of j since we found a lower number
                            mProfit += prices[j] - prices[i]
                            i=k
                            j=k+1
                            found=True
                            break
                        else:
                            j=k
                    #This means we have a low number we can buy but there are no other low numbers
                    # We need to find the largest number and sell there.
                    if not found:
                        print("Not Found")
                        mProfit += largestNumber - prices[i]
                        #We are done
                        j=len(prices)

            else:
                i +=1
                j +=1
        return mProfit
        