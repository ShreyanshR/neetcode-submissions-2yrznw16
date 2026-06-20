class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;

        for(auto& num: nums){
            count[num]++;
        }

        vector<vector<int>> result(nums.size()+1);

        for(auto& [num, cnt]: count){
            result[cnt].push_back(num);
        }

        vector<int> res;

        for(int i = result.size() - 1; i > 0 && res.size() < k; i--){
            for(int num: result[i]){
                res.push_back(num);
                if(res.size() == k) return res;
            }
        }

        return res;
    }
};
