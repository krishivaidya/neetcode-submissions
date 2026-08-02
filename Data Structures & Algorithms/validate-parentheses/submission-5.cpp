class Solution {
public:
    bool isValid(string s) {
        stack <int> store; 
        if(s.size() %2 != 0){
            return false;
        }
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '(' || s[i] == '{' || s[i] == '['){
                store.push(s[i]);
            }
            
            else if(store.empty() && (s[i] == ')' || s[i] == '}' || s[i] == ']')){
                return false;

            }

            else if(s[i] == ')'){
                if(store.top() != '(' ){
                    return false;
                } else{
                    store.pop();
                 }
            }

            else if(s[i] == '}'){
                if(store.top() != '{'){
                    return false;
                 } else{
                    store.pop();
                 }
            }

            else if(s[i] == ']'){
                if(store.top() != '['){
                    return false;
                }  else{
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
