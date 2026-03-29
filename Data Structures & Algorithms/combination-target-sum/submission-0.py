class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i , cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            #we will include the current element in the list
            dfs(i, cur, total + nums[i])

            #remove the element, as we don't want to include it, in the 2nd decison tree
            cur.pop()
            # i + 1 as we don't want to include i t
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res

        