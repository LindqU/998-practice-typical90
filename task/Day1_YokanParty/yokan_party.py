"""毎日競プロ Day1"""
from sys import stdin


def main():
    N, L= map(int, stdin.readline().split())
    K = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))

    A.insert(0,0)
    A.append(L)
    maxLen = L//(K+1)
    minLen = 0

    def check(halfLen):
        cnt = 0
        work_a = 0
        for a in A:
            if a - work_a < halfLen:
                continue
            else:
                work_a = a
                cnt += 1
        if cnt >= K+1:
            return True
        else:
            return False

    while minLen != maxLen:
        halfLen = ((minLen+maxLen)//2) + 1
        if check(halfLen):
            minLen = halfLen
        else:
            maxLen = halfLen -1 

    print(minLen)




if __name__ == "__main__":
    main()