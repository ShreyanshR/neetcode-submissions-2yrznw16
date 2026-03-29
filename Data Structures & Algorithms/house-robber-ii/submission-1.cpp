class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        if(nums.size() == 1){
            return nums[0];
        }
        
        int n1 = helper(vector<int> (nums.begin(), nums.end() - 1));
        int n2 = helper(vector<int> (nums.begin() + 1, nums.end()));

        return max(n1,n2);
    }

    int helper(vector<int>&& nums){
        int r1{};
        int r2{};

        for(auto num: nums){
            int temp = max(r2 + num, r1);
            r2 = r1;
            r1 = temp;
        }

        return r1;
    }
};
