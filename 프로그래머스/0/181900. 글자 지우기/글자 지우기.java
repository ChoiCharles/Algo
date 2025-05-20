class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        int lst[] = new int[my_string.length()];
        for (int i = 0; i < indices.length; i++) {
            lst[indices[i]] = 1;
        }
        for (int i = 0; i < my_string.length(); i++) {
            if (lst[i] == 0) {
                answer = answer + my_string.charAt(i);
            }
        }
        return answer;
    }
}