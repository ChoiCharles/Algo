class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 0;
        int leng = my_string.length();
        for (int i = leng; i > 0; i--) {
            String str = my_string.substring(0, i);
            if (is_prefix.equals(str)) answer = 1;
        }
        return answer;
    }
}