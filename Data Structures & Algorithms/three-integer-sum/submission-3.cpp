class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int l = 0;
        int r = nums.size() - 1;
        vector<vector<int>> res;

        for(int i = 0; i < nums.size(); i++){
            while(i >=1 && nums[i] == nums[i-1]){
                i += 1;
            }
            l = i + 1;
            r = nums.size() - 1;

            while(l < r){
                if(nums[i] + nums[l] + nums[r] > 0){
                r -= 1;
            } else if(nums[i] + nums[l] + nums[r] < 0){
                l += 1;
            }else{
                res.push_back({nums[i], nums[l], nums[r]});
                while(l + 1 < nums.size() && nums[l] == nums[l+1]){
                    l += 1;
                }
                while( r - 1 >= 0 && nums[r] == nums[r-1]){
                    r -=1;
                }
                l += 1;
                r -= 1;
            }

            }            
        }
        return res;
        
    }
};
