class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for(int num: nums){
            count[num]++;
        }

        vector<vector<int>> arr(nums.size() + 1);

        for(const auto& [num, cnt]: count){
            arr[cnt].push_back(num);
        }

        //sort(arr.rbegin(), arr.rend());

        vector<int> res;

        for(int i = arr.size() - 1; i >= 0 && res.size() < k; --i){
            for(int num : arr[i]){
                res.push_back(num);
                if(res.size() == k) return res;
            }
        }

        return res;
        
    }
};
