import java.util.ArrayList;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        ArrayList<Integer> result = new ArrayList<>();
        String str;
        int num;
        for (int i = 0; i < intStrs.length; i++) {
            str = intStrs[i].substring(s, s + l);
            num = Integer.parseInt(str);
            if (num > k) {
                result.add(num);
            }
        }
        int[] answer = result.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}