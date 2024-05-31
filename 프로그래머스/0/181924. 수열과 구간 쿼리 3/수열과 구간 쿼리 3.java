class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = arr;
        int n = queries.length;
        int tempI;
        int tempJ;
        for (int i = 0; i < n; i++) {
            tempI = answer[queries[i][0]];
            tempJ = answer[queries[i][1]];
            answer[queries[i][0]] = tempJ;
            answer[queries[i][1]] = tempI;
        }
        return answer;
    }
}