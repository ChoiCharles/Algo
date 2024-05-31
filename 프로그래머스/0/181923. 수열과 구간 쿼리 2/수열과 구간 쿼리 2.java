class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int n = queries.length;
        int[] answer = new int[n];
        int min;
        int s;
        int e;
        int k;
        for (int i = 0; i < n; i++) {
            s = queries[i][0];
            e = queries[i][1];
            k = queries[i][2];
            min = 1000001;
            for (int j = s; j <= e; j++) {
                if (arr[j] > k && arr[j] < min) {
                    min = arr[j];
                }
            }
            if (min == 1000001) {
                min = -1;
            }
            answer[i] = min;
        }
        return answer;
    }
}