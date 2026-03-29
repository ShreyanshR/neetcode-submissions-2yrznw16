class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int M = text1.size();
        int N = text2.size();

        vector<vector<int>> cache(M, vector<int>(N, -1));

        return memoHelper(text1, text2, cache, 0, 0);

    }

    int memoHelper(string& s1, string& s2, vector<vector<int>>&cache, int i1, int i2){
        if(i1 == s1.size() || i2 == s2.size()){
            return 0;
        }

        if(cache[i1][i2] != -1){
            return cache[i1][i2];
        }

        if(s1[i1] == s2[i2]){
            cache[i1][i2] = 1 + memoHelper(s1, s2, cache, i1 + 1, i2 + 1);
        }
        else{
            cache[i1][i2] =  max(memoHelper(s1, s2, cache, i1 + 1, i2),
                                memoHelper(s1, s2, cache, i1, i2+1));
        }

        return cache[i1][i2];
    }
};
