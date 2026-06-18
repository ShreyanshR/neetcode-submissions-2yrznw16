class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;

        for(auto& w: strs){
            vector<int> countW(26, 0);
            for(auto& c: w){
                countW[c - 'a']++;
            }

            auto key = to_string(countW[0]);
            for(int i = 1; i < 26; i++){
                key += ',' + to_string(countW[i]);
            }

            groups[key].push_back(w);
        }
        vector<vector<string>> res;
        for(auto& group: groups){
            res.push_back(group.second);
        }

        return res;
    }
};
