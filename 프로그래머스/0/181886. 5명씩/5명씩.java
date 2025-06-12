class Solution {
    public String[] solution(String[] names) {
        int len = names.length / 5;
        if (names.length % 5 != 0) {
            len++;
        }
        String[] answer = new String[len];
        int flag = 0;
        for (int i = 0; i < names.length; i = i + 5) {
            answer[flag] = names[i];
            flag++;
        }
        return answer;
    }
}