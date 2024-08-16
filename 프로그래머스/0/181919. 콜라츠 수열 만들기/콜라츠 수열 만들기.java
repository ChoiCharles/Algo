import java.util.*;

class Solution {
    public int[] solution(int n) {
        int[] answer = {};
        ArrayList<Integer> result = new ArrayList<>();
        result.add(n);
        while (n > 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
            result.add(n);
        }
        answer = result.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}