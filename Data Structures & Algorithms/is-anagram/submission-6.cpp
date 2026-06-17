class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        unordered_map<char, int> countS;
        unordered_map<char, int> countP;

        for(int i = 0; i < s.size(); i++){
            countS[s[i]]++;
            countP[t[i]]++;
        }

        return countS == countP;
        
        
    }
};
