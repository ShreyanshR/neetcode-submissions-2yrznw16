class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();

        //vector<int> dp(n+1);
        int twoStep = 0;
        int oneStep = 0;
        //dp[0] = dp[1] = 0;

        for(int i = 2; i <= n; i++){
            //dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]);
            int curr = min(oneStep + cost[i-1], twoStep + cost[i-2]);
            twoStep = oneStep;
            oneStep = curr;
            
        }

        //return dp[n]; 
        return oneStep;
    }   
};
