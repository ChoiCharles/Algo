class Solution {
    public int[] solution(String my_string) {
        int[] answer = new int[52];
        for (int i = 0; i < my_string.length(); i++) {
            int now = my_string.charAt(i);
            if (now <= 90) {
                answer[now - 65]++;
            } else {
                answer[now - 97 + 26]++;
            }
        }
        return answer;
    }
}