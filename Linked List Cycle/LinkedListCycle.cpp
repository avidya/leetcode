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

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL){
            return false;
        }
        ListNode *now=head;
        while(now != NULL){
            if(now->next == now){
                return true;
            }
            ListNode *p=head;
            while(p != now){
                if(p == now->next){
                    return true;
                }
                p=p->next;
            }
            now=now->next;
        }
        return false;
    }
};

int main(void){
}

