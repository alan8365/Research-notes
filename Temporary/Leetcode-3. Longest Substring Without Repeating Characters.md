## 直覺解
```c
bool isStringRepeat(char *s){
    int i;
    int j;
    int size = strlen(s);
    
    for(i = 0;i < size - 1;i++){
        for(j = i + 1;j < size;j++){
            if(s[i] == s[j]){
                return true;
            }
        }
    }
    
    return false;
}

int lengthOfLongestSubstring(char *s){
    int size = strlen(s);
    if(size < 2){
        return size;
    }
    
    int head = 0;
    int tail = 1;
    int result = 0;
    int subSize;
    char subString[size + 1];
    
    while(tail <= size){
        subSize = tail - head;
        memcpy(subString, &s[head], subSize);
        subString[subSize] = '\0';
        
        if(isStringRepeat(subString)){            
            head += 1;
        }else{
            result = result < subSize ? subSize : result;
            
            tail += 1;
        }      
    }
    
    return result;
}
```

## Sliding window
```c
int lengthOfLongestSubstring(char *s){
    if(s[0] == '\0')
        return 0;
    if(s[1] == '\0')
        return 1;
    
    int result = 0;
    int str = 0;
    int end;
    int pos;
    char *sub[strlen(s) + 1];

	# end是substring的結尾，簡單往後移動
    for(end = 1; s[end] != '\0'; end++){
	    # str是substring的開頭，pos是substring從頭檢查的指標
        for(pos = str; pos < end; pos++){
	        # 假如pos找到重複的部分則str往pos後一步
            if(s[pos] == s[end]){
                str = pos + 1;
                break;
            }
        }
        result = fmax(result, (end-str+1));
    }
    
    return result;
}
```