class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        vector<vector<int>> bucket(nums.size() + 1);
        for (auto& [x, c] : cnt) bucket[c].push_back(x);
        vector<int> res;
        for(int i = nums.size(); res.size() < k; i--)
            for (int x: bucket[i]) res.push_back(x);
        return res;
    }
};
