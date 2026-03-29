class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> cur;
        sort(candidates.begin(), candidates.end());

        backtrack(0, candidates, cur, res, 0, target);
        return res;
    }

    void backtrack(int i, vector<int>& candidates, vector<int>& cur, vector<vector<int>>& res, int total, int target){
        if(total == target){
            res.push_back(cur);
            return;
        }

        if(i >= candidates.size() || total > target){
            return;
        }

        cur.push_back(candidates[i]);

        backtrack(i+1, candidates, cur, res, total + candidates[i], target);

        cur.pop_back();

        while(i+1 < candidates.size() && candidates[i] == candidates[i+1]){
            i++;
        }
        backtrack(i+1, candidates, cur, res, total, target);

    }
};
