class Solution {
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<char, string> mapping{
			{'2', "abc"},
			{'3',"def"},
			{'4', "ghi"},
			{'5', "jkl"},
			{'6', "mno"},
			{'7', "pqrs"},
			{'8', "tuv"},
			{'9', "wxyz"}
	};

    vector<string> res;

    if(!digits.empty()){
        dfs(0, "", digits, mapping, res);
    }
    return res;    
    }

    void dfs(int i, string curStr, string& digits, unordered_map<char, string>& charToDigits, vector<string>& res){
        //base case
        if(curStr.size() == digits.size()){
            res.push_back(curStr);
            return;
        }

        for(auto& c: charToDigits[digits[i]]){
            dfs(i+1, curStr + c, digits, charToDigits, res);
        }
    }
};
