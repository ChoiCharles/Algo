class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuilder result = new StringBuilder(my_string);
        int s;
        int e;
        for (int i = 0; i < queries.length; i++) {
            s = queries[i][0];
            e = queries[i][1];
            while (s < e) {
                char temp = result.charAt(s);
                result.setCharAt(s, result.charAt(e));
                result.setCharAt(e, temp);
                s++;
                e--;
            }
        }
        return result.toString();
    }
}