class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;

        for(int num: numSet){
            if(numSet.find(num - 1) == numSet.end()){
                //we check if it's teh start of the seq by checking if the left element is in set
                int length = 1;
                while(numSet.find(num + length) != numSet.end()){
                    length++;
                }
                longest = max(longest, length);
            }

        }

        return longest;
    }
};
