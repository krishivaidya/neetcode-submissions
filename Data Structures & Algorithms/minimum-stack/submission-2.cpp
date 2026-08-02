class MinStack {
private: 
    stack<int> valS; 
    stack<int> minS;
public:
    MinStack() {
    }
    
    void push(int val) {
        valS.push(val);
        if(minS.empty() || val < minS.top()){
            minS.push(val);
        } else{
            minS.push(minS.top());
        }
        
    }
    
    void pop() {
        if(!valS.empty()){
            valS.pop();
        }
        if(!minS.empty()){
            minS.pop();
        }
        
    }
    
    int top() {
        if(!valS.empty()){
            return valS.top();
        }
        return -1;
        
    }
    
    int getMin() {
        if(!minS.empty()){
            return minS.top();
        }
        return -1;
        
    }
};
