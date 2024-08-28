class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        int cards1Length = cards1.length;
        int cards2Length = cards2.length;
        int goalLength = goal.length;
        int pointer1 = 0;
        int pointer2 = 0;
        int now = 0;
        while (now < goalLength) {
            if (pointer1 < cards1Length && goal[now].equals(cards1[pointer1])) {
                pointer1++;
                now++;
            } else if (pointer2 < cards2Length && goal[now].equals(cards2[pointer2])) {
                pointer2++;
                now++;
            } else {
                return "No";
            }
        }
        return "Yes";
    }
}