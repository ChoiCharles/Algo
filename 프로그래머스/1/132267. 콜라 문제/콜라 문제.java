class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        int now = n;
        int remain;
        int exchange;
        while (now >= a) {
            exchange = now / a;
            remain = now % a;
            answer += exchange * b;
            now = (exchange * b) + remain;
        }
        return answer;
    }
}