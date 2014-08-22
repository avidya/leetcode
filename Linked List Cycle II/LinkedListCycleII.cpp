#include <iostream>
using namespace std;
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if(head == NULL){
            return NULL;
        }
        ListNode *now=head;
        while(now != NULL){
            if(now == now->next){
                return now->next;
            }
            ListNode *p=head;
            while(p != now){
                if(p == now->next){
                    return now->next;
                }
                p=p->next;
            }
            now=now->next;
        }
        return NULL;
    }
};
