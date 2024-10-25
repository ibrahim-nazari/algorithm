

def find_min_cost_k_stop(flights,cities,k,src,dst):
    prices={city:float("inf") for city in cities}
    prices[src]=0

    for i in range(k+1):
        tempPrice=prices.copy()
        for s,d,c in flights:
            if prices[s] !=float("inf") and prices[s] +c < prices[d]:
                tempPrice[d]=prices[s] + c
        prices=tempPrice
    return prices[dst] if prices[dst] !=float("inf") else -1






def main():
   
    flights=[("A","B",4),("A","D",8),("B","D",8),("B","C",3),("C","E",2),("D","E",10)]
    cities=["A","B","C","D","E"]
    k=1
    src="A"
    dst="E"
    result=find_min_cost_k_stop(flights,cities,k,src,dst)
    print(result)

if __name__ =="__main__":
    main()