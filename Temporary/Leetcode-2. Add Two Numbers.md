```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode result;
    struct ListNode* temp = &result;
    
    result.val = 0; 
    result.next = NULL;
    
    int t1;
    int t2;
    int carry = 0;
    int sum;
    while (l1 || l2 || carry) {
        t1 = l1 ? l1->val : 0;
        t2 = l2 ? l2->val : 0;
        
        sum = carry + t1 + t2;
        carry = sum / 10;
        sum %= 10;
        
        temp->next = malloc(sizeof(struct ListNode));
        temp = temp->next;
        
        temp->next = NULL;
        temp->val = sum;
        
        l1 = (l1 ? l1->next : 0);
        l2 = (l2 ? l2->next : 0);
    }
    return result.next;
}
```