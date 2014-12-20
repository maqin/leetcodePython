# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        res = 0
        for i in range(0,len(points)):
            large = 0
            t = 0
            dict = {}
            same = 0
            dia = 0
            for j in range(i,len(points)):
                if points[i].x==points[j].x and points[i].y==points[j].y:
                    same += 1
                elif points[i].x == points[j].x:
                    dia += 1
                else:
                    p = 1.0*(points[i].y-points[j].y)/(points[i].x-points[j].x)
                    if p in dict:
                        dict[p] += 1
                    else:
                        dict[p] = 1
                    if dict[p]>t:
                        t = dict[p]
            if t>dia:
                large = t+same
            else:
                large = dia+same
            if res<large:
                res = large
        return res
        
