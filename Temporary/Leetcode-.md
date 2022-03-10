## 直覺解
```c
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int numsSize = nums1Size + nums2Size;
    int nums[numsSize];
    int i = 0;
    int j = 0;
    int k = 0;
    int middle = numsSize / 2;
    int temp1 = 0;
    int temp2 = 0;
    
    while(i < nums1Size || j < nums2Size){
        temp1 = temp2;
        
        if(i >= nums1Size){
            temp2 = nums2[j];
            j++;
        }else if(j >= nums2Size){
            temp2 = nums1[i];
            i++;
        }else if(nums1[i] < nums2[j]){
            temp2 = nums1[i];
            i++;
        }else{
            temp2 = nums2[j];
            j++;
        }
        
        printf("%d,%d \n", temp1, temp2);
        
        k++;
        if(k > middle){            
            if(numsSize % 2){
                return temp2;
            }else{
                return (float)(temp1 + temp2) / 2;
            }
        }
    }
    
    return 0;
}
```