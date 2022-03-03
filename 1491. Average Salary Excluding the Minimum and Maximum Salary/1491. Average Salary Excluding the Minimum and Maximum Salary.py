class Solution:
    def average(self, salary: List[int]) -> float:
        mini = min(salary)
        maxx = max(salary)
        
        return (sum(salary)-(mini+maxx))/(len(salary)-2)