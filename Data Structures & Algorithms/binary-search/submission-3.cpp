class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while(l<=r){
            int mid = (l+r)/2;
            if(target > nums[mid]){
                l++;
            } else if(target < nums[r]){
                r--;
            } else{
                return mid;
            }
        }

        return -1;
    }
};
