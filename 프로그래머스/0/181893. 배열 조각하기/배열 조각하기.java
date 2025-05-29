class Solution {
    public int[] solution(int[] arr, int[] query) {
        int start = 0;
        int end = 0;
        for (int i = 0; i < query.length; i++) {
            if (i % 2 == 0) {
                end = start + query[i];
            } else {
                start = start + query[i];
            }
        }
        int len = end - start + 1;
        int[] answer = new int[len];
        for (int i = 0; i < len; i++) {
            answer[i] = arr[start];
            start++;
        }
        return answer;
    }
}