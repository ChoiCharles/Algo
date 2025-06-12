class Solution {
    public int solution(int[] num_list) {
        int answer;
        int a = 0;
        int b = 0;
        for (int i = 0; i < num_list.length; i++) {
            if ((i + 1) % 2 == 0) {
                a = a + num_list[i];
            } else {
                b = b + num_list[i];
            }
        }
        if (a > b) {
            answer = a;
        } else if (a < b) {
            answer = b;
        } else {
            answer = a;
        }
        return answer;
    }
}