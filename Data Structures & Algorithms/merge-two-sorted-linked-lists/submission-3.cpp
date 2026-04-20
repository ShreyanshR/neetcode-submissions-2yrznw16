/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        auto final = make_unique<ListNode>(0);
        ListNode* curr = final.get();

        while(list1 && list2){
            if(list1->val <= list2->val){
                curr->next = list1;
                list1 = list1->next;
                //list2 = list2->next; 
            } else if(list2->val < list1->val){
                curr->next = list2;
                //list1 = list1->next;
                list2 = list2->next; 
            }

            curr = curr->next;
        }

        curr->next = list1 ? list1 : list2;

        return final->next;
    }
};
