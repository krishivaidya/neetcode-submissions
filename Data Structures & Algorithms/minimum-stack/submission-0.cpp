class MinStack {
private:
        std::stack<int> valstack;
        std::stack<int> minStack;
public:
    MinStack() {
    }
    void push(int val) {
        valstack.push(val);
        if (minStack.empty() || val <= minStack.top()) {
        minStack.push(val);
    } else {
        minStack.push(minStack.top());
    }
}
    
    void pop() {
        if(!valstack.empty()){
        valstack.pop();
        }
        if(!minStack.empty()){
            minStack.pop();
        }
        
     
    }
    
    int top() {
        if(!valstack.empty()){
             return valstack.top();
        } else{
            return -1;
        }   
    }
    
    int getMin() {
        if(!minStack.empty()){
            return minStack.top();
        } else{
            return -1;
        }

        
    }
};
