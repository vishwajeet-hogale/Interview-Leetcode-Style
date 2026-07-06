class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> res;
        int i = 0;
        while(i < 2){
            for(auto x:nums){
                res.push_back(x);
            }
            i += 1;
        }
        return res;
    }
};