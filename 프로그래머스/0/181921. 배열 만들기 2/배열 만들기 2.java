import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        int[] answer = {};
        ArrayList<Integer> result = new ArrayList<>();
        int flag;
        for (int i = l; i <= r; i++) {
            String num = String.valueOf(i);
            String[] numList = num.split("");
            int numLength = numList.length;
            flag = 0;
            for (int j = 0; j < numLength; j++) {
                if (numList[j].equals("0") || numList[j].equals("5")) {
                    flag++;
                }
            }
            if (flag == numLength) {
                result.add(i);
            }
        }
        answer = result.stream().mapToInt(Integer::intValue).toArray();
        if (answer.length == 0) {
            answer = new int[] {-1};
        }
        
        return answer;
    }
}