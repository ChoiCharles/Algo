class Solution {
    public int solution(String number) {
        int answer;
        int sum = 0;
        char charNum;
        int num;
        for (int i = 0; i < number.length(); i++) {
            charNum = number.charAt(i);
            num = charNum - '0';
            sum += num;
        }
        answer = sum % 9;
        return answer;
    }
}