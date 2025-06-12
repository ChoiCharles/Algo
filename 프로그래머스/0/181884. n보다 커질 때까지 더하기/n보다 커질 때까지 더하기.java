class Solution {
    public int solution(int[] numbers, int n) {
        int answer = 0;
        int res = 0;
        for (int i = 0; i < numbers.length; i++) {
            res = res + numbers[i];
            if (res > n) {
                return res;
            }
        }
        return answer;
    }
}