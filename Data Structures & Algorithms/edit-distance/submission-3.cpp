class Solution {
public:
    int minDistance(string word1, string word2) {
        int M = word1.size();
        int N = word2.size();

        vector<vector<int>> dp(M+1, vector<int>(N+1,0));

        for(int i=0; i < M; i++){
            dp[i][N] = M - i;
        }

        for(int j=0; j < N; j++){
            dp[M][j] = N - j;
        }

        for(int i=M-1; i >=0; i--){
            for(int j = N-1; j >= 0; j--){
                if(word1[i] == word2[j]){
                    dp[i][j] = dp[i+1][j+1];
                }
                else{
                    dp[i][j] = 1 + min(dp[i+1][j+1], min(dp[i+1][j],dp[i][j+1]));
                }
            }
        }

        return dp[0][0];
        
    }
};
