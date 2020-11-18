"""
course_schedule

https://leetcode.com/problems/course-schedule/

"""

#dfs 구조로 순환 구조 판별
import collections
def dfs_canFinish(numCourse, prerequisites):
	graph = collections.defaultdict(list)
	# make graph
	for x, y in prerequisites:
		graph[x].append(y)
	traced = set()

	def dfs(i):
		# if it has cycle return False
		if i in traced:
			return False
		
		traced.add(i)
		for y in graph[i]:
			if not dfs(y):
				return False
		# if search end flush traced
		traced.remove()
		return True
	
	for x in list(graph):
		if not dfs(x):
			return False
	return True

# dfs 방법으로 가지치기를 사용 using prunning 
# 방문했던 노드는(확인해 보았던 노드는 다시 보지 않는다.)
def enhanced(numCourse, prerequisites):
	# set graph
	graph = collections.defaultdict(list)
	for x, y in prerequisites:
		graph[x].append(y)
	
	traced = set()
	visited = set()

	def dfs(i):
		# check it is in trace
		if i in traced:
			return False
		# check it has been checked
		if i in visited:
			return True
		
		# dfs
		for y in graph[i]:
			if not dfs(y):
				return False
		
		# flush traced
		traced.remove()
		# add visited node
		visited.add(i)

		return True
	
	for x in list(graph):
		if not dfs(x):
			return False
	return True

