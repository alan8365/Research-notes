## 題目
Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.
## I. 直覺解
找出nums中哪兩個數字合起來是target，底下的程式碼就是把每個可能都試一次，i從0找到n，j從i+1開始找到n。假如i+j是target就直接回傳。
```c=
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i = 0;
    int j = 0;
    int* result;
    
    result = malloc(2 * sizeof(int));
    *returnSize = 2;
    
    while (i < numsSize){
        j = i + 1;
        while (j < numsSize){
            if(nums[i] + nums[j] == target){
                result[0] = i;
                result[1] = j;
                
                return result;
            }
            j++;
        }
        i++;
    }
        
    return result;
}
```

C會希望你自己想辦法優化array的取用，優化後長這樣，大概優化了60ms。
```c=
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize = 2;
    int *returnValues = (int*)malloc((*returnSize) * sizeof(int));
    int i;
    int j;
    
    for(i = 0;i < numsSize - 1;i++){
        for(j = i + 1;j < numsSize;j++){
            if(*(nums+i) + *(nums+j) == target){
                *returnValues = i;
                *(returnValues + 1) = j;
                return returnValues;
            }
        }
    }
    
    return returnValues;
}
```

## II.Hash解
```c=
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#define SIZE 50000

int hash(int key) {
	# 用mod來hash，把100存到100，50100存到101
    int r = key % SIZE;
    return r < 0 ? r + SIZE : r;
}

void insert(int *keys, int *values, int key, int value) {
    int index = hash(key);
    while (values[index]) {
		# 如果碰撞就往前一格，再碰撞就再往前
        index = (index + 1) % SIZE;
    }
	# 存兩個array確保key跟value是對應的，才不會因為碰撞歪掉
    keys[index] = key;
    values[index] = value;
}

int search(int *keys, int *values, int key) {
    int index = hash(key);
    while (values[index]) {
		# 確認key跟value對應
        if (keys[index] == key) {
            return values[index];
        }
        index = (index + 1) % SIZE;
    }
    return 0;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize = 2;
    int keys[SIZE];
    int values[SIZE] = {0};
    for (int i = 0; i < numsSize; i++) {
		# 算出目前數字所缺少的另一半
        int complements = target - nums[i];
		# 檢查另一半是否出現過
        int value = search(keys, values, complements);
        if (value) {
            int *indices = (int *) malloc(sizeof(int) * 2);
            indices[0] = value - 1;
            indices[1] = i;
            return indices;
        }
		# 沒出現過就把目前數字放進hash array中
        insert(keys, values, nums[i], i + 1);
    }
    return NULL;
}
```