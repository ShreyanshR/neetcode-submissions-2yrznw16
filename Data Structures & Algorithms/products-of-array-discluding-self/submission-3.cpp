class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product{1};
        int zero{0};

        for(auto& num: nums){
            if(num != 0){
                product *= num;
            } else{
                zero++;
            }
        }

        if(zero > 1){
            return vector<int>(nums.size(), 0);
        }

        vector<int> res(nums.size());
        for(int i=0; i < nums.size(); i++){
            if(zero > 0){
                res[i] = (nums[i]==0) ? product : 0;
            } else{
                res[i] = product / nums[i];
            }
        }
        return res;
    }
};
