class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = "";
        String first = my_string.substring(0, s);
        String before = my_string.substring(s, e + 1);
        String last = my_string.substring(e + 1);
        
        String after = new StringBuilder(before).reverse().toString();
        
        answer = first + after + last;
        return answer;
    }
}