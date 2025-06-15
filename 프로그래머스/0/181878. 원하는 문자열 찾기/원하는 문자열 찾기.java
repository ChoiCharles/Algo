class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String my = myString.toLowerCase();
        String pa = pat.toLowerCase();
        int len = pa.length();
        
        int now = 0;
        int flag = 0;
        while (true) {
            if (flag >= len) return 1;
            if (now >= my.length()) break;
            if (my.charAt(now) == pa.charAt(flag)) {
                flag++;
                now++;
            } else {
                now++;
                flag = 0;
            }
        }
        
        return answer;
    }
}