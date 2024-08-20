class Solution {
    public String solution(String my_string, int[] index_list) {
        String answer = "";
        int indexLength = index_list.length;
        for (int i = 0; i < indexLength; i++) {
            answer += my_string.charAt(index_list[i]);
        }
        return answer;
    }
}