class Solution {
    public String[] solution(String[] str_list) {
        int len = str_list.length;
        for (int i = 0; i < len; i++) {
            if (str_list[i].equals("l")) {
                String[] answer = new String[i];
                for (int j = 0; j < i; j++) {
                    answer[j] = str_list[j];
                }
                return answer;
            } else if (str_list[i].equals("r")) {
                String[] answer = new String[len - i - 1];
                int now = 0;
                for (int j = i + 1; j < len; j++) {
                    answer[now] = str_list[j];
                    now++;
                }
                return answer;
            }
        }
        String[] ans = new String[0];
        return ans;
    }
}