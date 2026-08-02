class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<string> store;

        for(int i = 0; i < tokens.size(); i++){
            if(tokens[i] == "+"){
                int a = stoi(store.top());
                store.pop();
                int b = stoi(store.top());
                store.pop();
                store.push(std::to_string(a + b));
            }

            else if(tokens[i] == "-"){
                int a = stoi(store.top());
                store.pop();
                int b = stoi(store.top());
                std::swap(a,b);
                store.pop();
                store.push(std::to_string(a - b));
            }

            else if(tokens[i] == "*"){
                int a = stoi(store.top());
                store.pop();
                int b = stoi(store.top());

                store.pop();
                store.push(std::to_string(a * b));
            }

            else if(tokens[i] == "/"){
                int a = stoi(store.top());
                store.pop();
                int b = stoi(store.top());
                std::swap(a,b);
                store.pop();
                store.push(std::to_string(a / b));
            } else{
                store.push(tokens[i]);
            }
        }

        return stoi(store.top());


        
    }
};
