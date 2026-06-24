class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stk;
        unordered_map<char, char> closeToOpen{
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        for(auto& c:s){
            if(closeToOpen.count(c) && !stk.empty() && stk.top() == closeToOpen[c]){
                stk.pop();
            } else{
                stk.push(c);
            }
        }

        return stk.empty();
    }
};
