class Solution {
    public int[] solution(int n, int k) {
        int[] answer = new int[n / k];
        int i = 0;
        while (true) {
            if (k * (i + 1) > n) break;
            answer[i] = k * (i + 1);
            i++;
        }
        return answer;
    }
}