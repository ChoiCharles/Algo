class Solution {
    public int[] solution(int[] num_list, int n) {
        int len = num_list.length;
        int m;
        if (len % n == 0) {
            m = len / n;
        } else {
            m = (len / n) + 1;
        }
        int[] answer = new int[m];
        int now = 0;
        for (int i = 0; i < len; i = i + n) {
            answer[now] = num_list[i];
            now++;
        }
        return answer;
    }
}