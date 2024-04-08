class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        preference_count = {0: 0, 1: 0}

        for preference in students:
            preference_count[preference] += 1

        for sandwich in sandwiches:
            if preference_count[sandwich] == 0:
                break
            preference_count[sandwich] -= 1

        return preference_count[0] + preference_count[1]