class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        int l = 0;
        int r = numbers.size() - 1;

        for (int i = 0; i < numbers.size(); i++){
            if(numbers[l] + numbers[r] > target){
                r -= 1;
            } else if(numbers[l] + numbers[r] < target){
                l += 1;
            } else{
                res.push_back(l+1);
                res.push_back(r+1);

                return res;
            }
        }
        
    }
};
