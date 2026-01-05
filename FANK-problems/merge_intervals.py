
class MergedIntervals:

    def solution(self,intervals):

        merged=[]

        merged.append(intervals[0])

        for  lst in intervals:

            if merged[-1][1]>=lst[0]:

                merged[-1][1]=lst[1]

            else:

                merged.append(lst)

        return merged

merged_lst =MergedIntervals()

print(merged_lst.solution([[1,3],[2,6],[5,9],[15,18]]))

    


