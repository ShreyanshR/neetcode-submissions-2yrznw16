class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> numSet(nums.begin(), nums.end());
        int k = numSet.size();

        return !(n==k);
    }
};