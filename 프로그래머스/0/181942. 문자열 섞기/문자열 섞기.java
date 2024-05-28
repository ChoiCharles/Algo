class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        String[] strSplit1 = str1.split("");
        String[] strSplit2 = str2.split("");
        int j = 0;
        for (int i = 0; i < strSplit1.length * 2; i++) {
            if (i % 2 == 0) {
                answer += strSplit1[j];
            } else {
                answer += strSplit2[j];
                j += 1;
            }
        }
        return answer;
    }
}