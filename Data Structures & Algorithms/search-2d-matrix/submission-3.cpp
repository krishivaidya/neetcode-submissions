class Solution {
private: 
bool secondhelper(vector<vector<int>>& matrix, int target,int mid, int start1, int end1){
        if(start1 > end1){
            return false;
        }

        

        int mid1 = start1+ (end1 - start1) / 2;

        if(target > matrix[mid][mid1]){
            start1 = mid1 + 1; 
            return secondhelper(matrix, target, mid, start1, end1);

        } 

        else if(target < matrix[mid][mid1]){

            end1 = mid1 - 1;
            return secondhelper(matrix, target, mid , start1, end1);

        }

        else{
            return true;
        }

        return false;
}

    bool firsthelper(vector<vector<int>>& matrix, int target, int start, int end){
        
        if(start > end){
            return false;
        }
        
        int mid = start + (end - start)/2;
        int length = matrix[mid].size() - 1;
        if(target >= matrix[mid][0] && target <= matrix[mid][length]){
            return secondhelper(matrix, target, mid , 0, length);
        } 
        else if(target > matrix[mid][length]){
            start = mid + 1;
            return firsthelper(matrix, target, start, end);
        } else{
            end = mid - 1;
            return firsthelper(matrix, target, start, end);
        }

        return false;
    }




public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        return firsthelper(matrix, target, 0, matrix.size() - 1);
        
    }
};
