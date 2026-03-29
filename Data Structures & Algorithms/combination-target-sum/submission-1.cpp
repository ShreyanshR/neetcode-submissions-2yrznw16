class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        vector<int> cur;

        backtrack(0, nums, target, res, cur);

        return res;

    }

    void backtrack(int i, vector<int>& nums, int target, vector<vector<int>>& res, vector<int>& cur){
        if(target == 0){
            res.push_back(cur);
            return;
        }

        if(i >= nums.size() || target < 0){
            return;
        }

        cur.push_back(nums[i]);

        backtrack(i, nums, target - nums[i], res, cur);

        cur.pop_back();

        backtrack(i+1, nums, target, res, cur);

    }
};
