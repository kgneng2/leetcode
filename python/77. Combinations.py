from itertools import combinations

class Solution:
    def combine(self, n: int, k: int):
        d = [i for i in range(1,n+1)]
        res = list(combinations(d,k))
        return res


# combinations 를 사용했지만, 재귀 문제였음.. https://velog.io/@eddy_song/you-can-solve-recursion#1%EB%8B%A8%EA%B3%84-%EC%9E%AC%EA%B7%80%EB%A5%BC-%EA%BC%AD-%EC%8D%A8%EC%95%BC%ED%95%98%EB%8A%94%EA%B0%80-1 
# 재귀 풀이에 익숙해지도록
