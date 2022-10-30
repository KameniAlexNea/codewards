/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) return false;
        ListNode behind = head;
        ListNode front = head;
        while ((behind.next != null) && (front.next.next != null)) {
            behind = behind.next;
            front = front.next.next;
            if (behind == front) return true;
            if ((front == null) || (front.next == null)) return false;
        }
        return false;
    }
}