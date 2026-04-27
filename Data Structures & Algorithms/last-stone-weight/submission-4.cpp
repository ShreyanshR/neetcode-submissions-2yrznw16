class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> hp(stones.begin(), stones.end());

        while (hp.size() > 1){
            int first = hp.top();
            hp.pop();
            int second = hp.top();    
            hp.pop();

            if(first > second){
                hp.push(first - second);
            }    
            
        }

        return hp.empty() ? 0 : hp.top();
        
    }
};
