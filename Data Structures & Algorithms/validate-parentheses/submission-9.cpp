class Solution {
public:
    bool isValid(string s) {
        stack<char> store;

        if(s[0] == '}' || s[0] == ')' || s[0] == ']'){
            return false;
        }

        for(int i = 0; i < s.size(); i++){
            if(s[i] == '{' || s[i] == '(' || s[i] == '[' ){
                store.push(s[i]);
            }

            if(s[i] == '}'){
                if(store.empty() || store.top() != '{'){
                    return false;
                } else{
                    store.pop();
                }
            }

            if(s[i] == ')'){
                if(store.empty() || store.top() != '('){
                    return false;
                } else{
                    store.pop();
                }
            }

            if(s[i] == ']'){
                if(store.empty() || store.top() != '['){
                    return false;
                } else{
                    store.pop();
                }
        }
        
    }

    if(!store.empty()){
        return false;
    } 

    return true;
    }
};
