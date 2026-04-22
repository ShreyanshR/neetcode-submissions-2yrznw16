class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        unordered_map<char, int> count_s;

        for(auto& a: s){
            count_s[a]++;
        }

        for(auto& b: t){
            if(!count_s.count(b) || count_s[b] == 0) return false;

            count_s[b]--;
        }

        return true;

    }
};
