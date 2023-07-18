# 엉망임. 시간복잡도 공간복잡도 모두 문제인 문제
# 2차 메트릭스를 만들고 거기에 값을 집어넣으면서 풀려고했음.
# 하지만 row만 쓰고, 인덱스안에 바로 집어넣는 방법을 쓰면 더 쉽게 가능해보임.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        len_s = len(s)
        
        if numRows == 1:
            return s

        repeat_cnt = int(len_s / (numRows + numRows - 2))
        remain = len_s % (numRows + numRows - 2) 
        al = 1 if remain != 0 else 0

        col = (1 + numRows - 2) * repeat_cnt + al+ 1000

        print(numRows, col)

        mat = [["" for j in range(col)] for i in range(numRows)]

        p = 0
        q = 0
        step = 1
        move_flag = False

        for index in range(len(s)):
            dd = numRows - 2  # 6
            rr = numRows + dd  # 2
            re = index % rr  # 4, 5 
            
            if re >= rr - dd -1 and re < rr:
                move_flag = True
            else :
                move_flag = False

            mat[p][q] = s[index]
            print("[",p,",",q,"]", re, move_flag)

            if move_flag:    
                q = q + 1
                p = p - 1
            else:
                p = p + 1
        
        res = []
        for col in mat:
            res = res + ["".join(col)]

        return "".join(res)

            
