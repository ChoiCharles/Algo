class Solution {
    public int[] solution(int[] num_list, int n) {
        int len = num_list.length;
        int[] answer = new int[len];
        int now = 0;
        for (int i = n; i < len; i++) {
            answer[now] = num_list[i];
            now++;
        }
        for (int i = 0; i < n; i++) {
            answer[now] = num_list[i];
            now++;
        }
        
        return answer;
    }
}