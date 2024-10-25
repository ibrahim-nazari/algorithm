

def find_valid_palates(plates):
    result=[]
    for plate in plates:
        valid=True
        if len(plate) !=8:
            valid=False
        if plate[0] !=plate[1] or plate[0].isalpha() or plate[1].isalpha():
            valid=False
        if plate[2].isalpha() or plate[3].isalpha():
            valid=False
        if plate[4].isnumeric() or plate[4].islower() :
            valid=False
        if plate[5:].isalpha():
            valid=False
        if valid:
            result.append(plate)
    return result
        
def main():
    t=int(input())
    for _ in range(t):
        plates=[]
        N=int(input())
        for i in range(N):
            plates.append(input())
        result=find_valid_palates(plates)
        for rs in result:
            print(rs)



if __name__ =="__main__":
    main()