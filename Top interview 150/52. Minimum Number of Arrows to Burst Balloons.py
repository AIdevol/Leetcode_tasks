class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        # sort the points from x
        n_arrow, arrow = 1, points[-1][0]
        for i in range(len(points)-2, -1, -1):
            if not points[i][0]<=arrow<=points[i][1]:
                arrow = points[i][0]
                n_arrow += 1
        return n_arro
