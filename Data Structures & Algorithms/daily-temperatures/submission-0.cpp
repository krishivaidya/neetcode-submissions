class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> result(temperatures.size(), 0); 
        stack<pair<int, int>> store; 

        for(int i = 0; i < temperatures.size(); i++){
            while(!store.empty() && store.top().first < temperatures[i]){
                pair<int, int> cur = store.top();
                result[cur.second] = i - cur.second;
                store.pop();
            }
            store.push({temperatures[i], i});
        }

        return result;  
    }
};
