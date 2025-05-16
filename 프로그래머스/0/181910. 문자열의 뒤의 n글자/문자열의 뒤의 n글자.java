class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        answer = answer.concat(my_string.substring(my_string.length() - n));
        return answer;
    }
}