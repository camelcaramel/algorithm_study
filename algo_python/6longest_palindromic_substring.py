"""
가장 긴 팰린드롬 문자열을 출력하라

Longest Palindrome Substring

input:
"babad"
output:
"bab"

https://leetcode.com/problems/longest-palimdromic-substring/
"""

"""
최장 공통 부분 문자열 (longest common substring) 문제가 있다. 
전형적인 다이나믹 프로그래밍 문제이다.
하지만 이 문제의 경우 다르게 접근할 수 있다.
"""

"""
투포인터 방식과 슬라이딩 윈도우 방식을 사용한다. 
팰린드롬이 홀수개인 경우와 짝수개인 경우를 판단하기 위해서 두칸짜리 윈도우와 
세칸짜리 윈도우를 왼쪽으로 움직이고 윈도우의 양쪽을 살펴 팰린드롬이라면 
양쪽 포인터를 하나씩 확장해나간다.
결과는 가장 긴 문자열을 출력한다.
"""

def longest_palindrome(s):
	# 팰린드롬 판별 및 투 포인터 확장
	def expand(left, right):
		while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
			left -= 1
			right += 1
		return s[left + 1: right - 1]
	# 해당 사항이 없을 때 빠르게 리턴
	if len(s) < 2 or s == s[::-1]:
		return s
	result  = ''
	# 슬라이딩 윈도우 우측으로 이동
	for i in range(len(s) - 1):
		result = max(result, expand(i, i + 1), expand(i, i + 2),key=len)
	
	return result