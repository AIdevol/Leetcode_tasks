class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_count = max(task_counts.values())
        max_occurrences = list(task_counts.values()).count(max_count)
        
        cycles = (max_count - 1) * (n + 1) + max_occurrences
        
        return max(len(tasks), cycles)

