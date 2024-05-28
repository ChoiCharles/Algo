class Solution {
    public int solution(int a, int b) {
        int answer;
        String str1 = String.valueOf(a);
        String str2 = String.valueOf(b);
        int result1 = Integer.parseInt(str1 + str2);
        int result2 = Integer.parseInt(str2 + str1);
        if (result1 >= result2) {
            answer = result1;
        } else {
            answer = result2;
        }
        return answer;
    }
}