import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        Integer[] sorting = Arrays.stream(score).boxed().toArray(Integer[]::new);
        Arrays.sort(sorting, Collections.reverseOrder());
        int flag = 0;
        for (int i = 0; i < score.length; i++) {
            flag++;
            if (flag % m == 0) {
                answer += sorting[i] * m;
                flag = 0;
            }
        }
        return answer;
    }
}