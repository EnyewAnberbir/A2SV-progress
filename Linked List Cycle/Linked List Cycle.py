public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode highSpeed = head;
        ListNode lowSpeed = head;
 
        while(highSpeed != null && highSpeed.next != null){
            lowSpeed = lowSpeed.next;
            highSpeed = highSpeed.next.next;
 
            if(lowSpeed == highSpeed)
                return true;
        }
 
        return false;
    }
}
