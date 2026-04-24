class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int top = 0;
        int rows = matrix.size();
        int cols = matrix[0].size();
        int bottom = rows * cols - 1;
        

        while(top <= bottom){
            int mid = (top + bottom) / 2;
            int r = mid / cols;
            int c = mid % cols;
            if(target > matrix[r][c]){
                top = mid + 1;
            } else if(target < matrix[r][c]) {
                bottom = mid - 1;
            } else{
                return true;
            }
        }

        return false;
    }
};
