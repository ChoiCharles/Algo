class Solution {
    public int solution(String my_string, String is_suffix) {
        int answer = 0;
        int leng = my_string.length();
        String[] lst = new String[leng];
        for (int i = 0; i < leng; i++) {
            String st = my_string.substring(i);
            if (st.equals(is_suffix)) {
                answer = 1;
            }
        }
        return answer;
    }
}