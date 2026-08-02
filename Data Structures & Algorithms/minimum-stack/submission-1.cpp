class MinStack {
private: 
    std::stack<int> minStack; 
    std::stack<int> valStack;

public:
    MinStack() {
        
    }
    
    void push(int val) {
        valStack.push(val);
        if(minStack.empty() || val <= minStack.top()){
            minStack.push(val);
        } else{
            minStack.push(minStack.top());
        }     
    }
    
    void pop() {
        if(!valStack.empty()){
            valStack.pop();
        }
        if(!minStack.empty()){
            minStack.pop();
        }
        
    }
    
    int top() {
        if(!valStack.empty()){
            return valStack.top();
        }
        
    }
    
    int getMin() {
        if(!minStack.empty()){
            return minStack.top();
        }
        
    }
}
;
