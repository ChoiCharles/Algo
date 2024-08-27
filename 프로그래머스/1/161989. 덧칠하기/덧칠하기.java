class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int secLength = section.length;
        int start = 0;
        int end = 1;
        int paint;
        if (m == 1) {
            return secLength;
        }
        while (secLength > start) {
            if (secLength <= end) {
                answer++;
                break;
            }
            paint = section[end] - section[start] + 1;
            if (paint > m) {
                answer++;
                start = end;
                end = start + 1;
            } else if (paint == m) {
                answer++;
                start = end + 1;
                end = start + 1;
            } else {
                end++;
            }
        }
        return answer;
    }
}