class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret=[]
        candidates.sort()
        def dfs(idx,target,path):
            if target<0:
                return
            if target==0:
                ret.append(path)
                return
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                dfs(i+1,target-candidates[i],path+[candidates[i]])
        dfs(0,target,[])
        return ret
