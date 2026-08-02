#include <string>
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<string> store;

        for(int i = 0; i < tokens.size(); i++){
             if (tokens[i] == "+"){
                int a = stoi(store.top());
                store.pop();
                int b = stoi(store.top());
                store.pop();
               store.push(to_string(a + b));

            }

            else if (tokens[i] == "-"){
                int a = stoi(store.top());
                store.pop();
                int b = stoi(store.top());
                store.pop();
                std::swap(a, b);
                store.push(to_string(a - b));

            }

            else if (tokens[i] == "*"){
                int a = stoi(store.top());
                store.pop();
                int b = stoi(store.top());
                store.pop();
               store.push(to_string(a * b));

            }

            else if (tokens[i] == "/"){
                int a = stoi(store.top());
                store.pop();
                int b = stoi(store.top());
                store.pop();
                std::swap(a, b);
               store.push(to_string(a / b));

            }
            
            else{
                store.push(tokens[i]);
            }
        }
        
        int return_val = std::stoi(store.top());
        return return_val;
        
    }
};
