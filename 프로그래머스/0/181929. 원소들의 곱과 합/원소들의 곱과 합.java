class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int prod = num_list[0];
        int sum = num_list[0];
        for (int i = 1; i < num_list.length; i++) {
            prod *= num_list[i];
            sum += num_list[i];
        }
        if (prod < (sum*sum)) {
            answer = 1;
        }
        return answer;
    }
}