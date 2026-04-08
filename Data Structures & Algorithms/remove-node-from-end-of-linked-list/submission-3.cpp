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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        auto dummy = make_unique<ListNode>(0, head);
        ListNode* right = head;
        ListNode* left = dummy.get();

        while(n > 0 && right){
            right = right->next;
            n -= 1;
        }

        while(right){
            right = right->next;
            left = left->next;
        }

        left->next = left->next->next;

        return dummy->next;
    }
};
