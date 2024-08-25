import java.util.ArrayList;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < photo.length; i++) {
            int score = 0;
            for (int j = 0; j < photo[i].length; j++) {
                for (int k = 0; k < name.length; k++) {
                    if (photo[i][j].equals(name[k])) {
                        score += yearning[k];
                    }
                }
            }
            answer.add(score);
        }
        int[] result = answer.stream().mapToInt(Integer::intValue).toArray();
        return result;
    }
}