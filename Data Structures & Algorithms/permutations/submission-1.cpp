class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> cur;

        dfs(cur, res, nums);

        return res;
    }

    void dfs(vector<int>& cur, vector<vector<int>>& res, vector<int>& nums){
        if(cur.size() == nums.size()){
            res.push_back(cur);
            return;
        }

        for(auto &num: nums){
            if(!(std::find(cur.begin(), cur.end(), num) != cur.end())){
                cur.push_back(num);
                dfs(cur, res, nums);
                cur.pop_back();
            }
        }
    }
};
