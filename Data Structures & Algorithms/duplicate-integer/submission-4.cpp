class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> seen(nums.begin(), nums.end());
        int k = seen.size();

        return n != k;
    }
};