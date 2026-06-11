class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> groups;

        for(auto& s: strs){
            vector<int> count(26, 0);
            for(auto& c: s){
                count[c - 'a']++;
            }

            //okay we did for each word we mapped 1 or 0
            auto key = to_string(count[0]);
            for(int i=1; i < 26; i++){
                key += ',' + to_string(count[i]);
            }
            groups[key].push_back(s);
        }

        vector<vector<string>> res;
        for(auto& pairs: groups){
            res.push_back(pairs.second);
        }

        return res;

    }
};
