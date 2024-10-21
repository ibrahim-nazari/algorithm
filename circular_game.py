import math
def calculate_score(cordinate):
    x,y=cordinate
    # find distance from origin (0,0), using Euclidean distance
    distance= math.sqrt(x **2 + y **2)
    # circle radius is 5
    if distance < 5:
        # stone is inside circle
        return distance
    elif distance == 5:
        # stone is on the circle
        return 0
    else:
        # stone is outside circle
        return -1
    



def main():
    t=int(input())
    for _ in range(t):
        n=int(input())
        players=[]
        for i in range(n):
            first_round=map(int,input().split(","))
            second_round=map(int,input().split(","))
            score_first_round=calculate_score(first_round)
            score_second_round=calculate_score(second_round)
            score=score_first_round + score_second_round
            players.append(score)
        for score in players:
            score= int(score) if score.is_integer() else f"{score:.5f}"
            print(score)


if __name__ =="__main__":
    main()