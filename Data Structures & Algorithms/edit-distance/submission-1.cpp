class Solution {
public:
    int minDistance(string word1, string word2) {
        int N = word1.size();
        int M = word2.size();

        vector<vector<int>> dp(N+1, vector<int>(M+1, 0));

        for(int j = 0; j < M; j++){
            dp[N][j] = M - j;
        }

        for(int i = 0; i < N; i++){
            dp[i][M] = N - i;
        }

        for(int i = N - 1; i >= 0; i--){
            for(int j = M - 1; j >= 0; j--){
                if(word1[i] == word2[j]){
                    dp[i][j] = dp[i+1][j+1];
                }
                else{
                    dp[i][j] = 1 + min(dp[i+1][j], min(dp[i][j+1], dp[i+1][j+1]));
                }
            }
        }

        return dp[0][0];
    }
};
