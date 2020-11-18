"""
매일 온도 리스트 T 를 입력 받아서 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.

input:
T = [73, 74, 75, 71, 69, 72, 76, 73]

output:
[1,1,4,2,1,1,0,0]

leetcode => daily-temperatures
"""

# 스택을 이용한 풀이
def answer_stack(T):
	answer = [0] * len(T)
	stack = []
	for i, cur in enumerate(T):
		while stack and cur > T[stack[-1]]:
			last = stack.pop()
			answer[last] = i - last
		stack.append(i)
	return stack