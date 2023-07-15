# 못풀었음.다시 해야함.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            start = 0
            max_length = 0
            char_dict = {}

            # Iterate over the string using a sliding window
            for end in range(len(s)):
                print(char_dict, s[end])
                if s[end] in char_dict:
                    print(s[end],start, char_dict[s[end]], end, start)
                    # Update the start pointer to the next position after the repeated character
                    start = max(start, char_dict[s[end]] + 1)
               

                # Update the current character's position
                char_dict[s[end]] = end

                # Update the maximum length
                # print(end, start, max_length, s[end],s[start])
                print(max_length, end, start)
                max_length = max(max_length, end - start + 1)
                # print(char_dict, max_length, s[end])
                print(max_length)

            return max_length

## 오답임.
## 처음부터 끝까지 구해서 차이의 배열을 만들어서, 예를들어 pwwkew -> [6, 1, 3, 3, 2, 1] 이런식으로 만들고 index가 큰것중에 최대값을 구하려고했음. 하지만, abcabcbb의 경우에는 5번째 a가 커버려서 안됨. 즉 최대값 구하려는 공식이 잘못되었음. 
## 기록을 위해 아래와 같이 남기고 위와 같이 풀도록하자.
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_list = list(s)
        
        res_list = []

        print("a", "b", "a_index", "b_index", "len")
        for index, d in enumerate(s_list):
            
            find_index = 0
            
            for f_index, f_d in enumerate(s_list[index+1:]):
                if d == f_d:
                    find_index = f_index + 1
                    print(d, f_d, index, f_index+index+1, find_index,"------same")
                    break
                print(d, f_d, index, f_index+index+1, find_index)

            
            if find_index == 0:
                res_list.append(len(s_list)- index)
            else:
                res_list.append(find_index)
    
        print(res_list)

        result = 0

        max_value = 0
        max_index = 0

        for i, num in enumerate(res_list):
            if num >= max_value and i > max_index:
                max_value = num
                max_index = i

        print(max_index, max_value)
        return max_value
        
                

s = Solution()

s.lengthOfLongestSubstring("abcabcbb")
s.lengthOfLongestSubstring("pwwkew")


# str 을 하나씩 늘려가는데, 그럼 2중 포문이 되는데, ??  최대 O^2까지 되는데 괜츈?




