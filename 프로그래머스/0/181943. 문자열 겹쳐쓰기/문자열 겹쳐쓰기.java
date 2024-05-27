class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        String[] stringSplit = my_string.split("");
        for (int i = 0; i < stringSplit.length; i++) {
            if (i == s) {
                answer += overwrite_string;
                i += overwrite_string.length();
                if (i >= stringSplit.length) {
                    break;
                }
            }
            answer += stringSplit[i];
        }
        
        return answer;
    }
}