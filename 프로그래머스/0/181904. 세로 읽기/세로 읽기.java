class Solution {
    public String solution(String my_string, int m, int c) {
        String answer = "";
        int leng = my_string.length();
        int n = leng / m;
        String lst[] = new String[n];
        for (int i = 0; i < n; i++) {
            lst[i] = my_string.substring(i * m, (i + 1) * m);
        }
        for (int i = 0; i < lst.length; i++) {
            try {
                answer = answer + lst[i].substring(c - 1, c);
            } catch(StringIndexOutOfBoundsException e) {
                
            }
        }
        return answer;
    }
}