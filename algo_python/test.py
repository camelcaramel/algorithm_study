import collections
def removedup(s):
	for char in sorted(set(s)):
		suffix = s[s.index(char):]

		if set(s) == set(suffix):
			return char + removedup(suffix.replace(char, ''))
		
	return ''

def removedup_stack(s):
	counter, seen, stack = collections.Counter(s), set(), []

	for char in s:
		counter[char] -= 1
		if char in seen:
			continue
		while stack and char < stack[-1] and counter[stack[-1]] > 0:
			seen.remove(stack.pop())
		stack.append(char)
		seen.add(char)
	
	return ''.join(stack)

def dailytemp(T):
	answer = [0] * len(T)
	stack = []

	for i, cur in enumerate(T):
		while stack and cur > T[stack[-1]]:
			last = stack.pop()
			answer[last] = i - last
		stack.append(i)
	return answer

import heapq
