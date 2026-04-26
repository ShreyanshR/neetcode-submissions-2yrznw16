class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stk;

        std::unordered_map<char,char> closeToOpen = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        for(auto& c: s){
            if(closeToOpen.count(c) && !stk.empty() && closeToOpen[c] == stk.top()){
                stk.pop();
            } else{
                stk.push(c);
            }
        }

        return stk.empty();
    }
};
