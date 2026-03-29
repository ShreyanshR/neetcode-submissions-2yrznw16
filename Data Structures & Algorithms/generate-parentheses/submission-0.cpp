class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string cur;

        backtrack(cur, res, 0, 0, n);

        return res;
        
    }

    void backtrack(string& cur, vector<string>& res, int open, int close, int n){
        if(open == n && close == n){
            res.push_back(cur);
            return;
        }

        if(open < n){
            cur.push_back('(');
            backtrack(cur, res, open+1, close, n);
            cur.pop_back();
        }

        if(close < open){
            cur.push_back(')');
            close += 1;
            backtrack(cur, res, open, close, n);
            cur.pop_back();
        }
        
    }
};
