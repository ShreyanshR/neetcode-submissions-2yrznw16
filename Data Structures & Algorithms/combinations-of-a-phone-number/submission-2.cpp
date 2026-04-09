class Solution {
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<char, string> digits_to_char = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };

        vector<string> res;

        if(!digits.empty()){
            dfs(0, "", res, digits, digits_to_char);
        }
        
        return res;
    }

    void dfs(int i, string curStr, vector<string>& res, string& digits, unordered_map<char, string>& digits_to_char){
        if(curStr.size() == digits.size()){
            res.push_back(curStr);
            return;
        }

        for(auto& c: digits_to_char[digits[i]]){
            dfs(i+1, curStr + c, res, digits, digits_to_char);
        }
    }
};
