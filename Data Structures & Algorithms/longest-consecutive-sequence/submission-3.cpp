class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numS(nums.begin(), nums.end());
        int longest{0};

        for(auto& num: numS){
            if(!numS.contains(num - 1)){
                int count = 1;
                while(numS.contains(num + count)){
                    count++;
                }

                longest = longest > count ? longest : count;
            }
        }

        return longest;
    }
};
