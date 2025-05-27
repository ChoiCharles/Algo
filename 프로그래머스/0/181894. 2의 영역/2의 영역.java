class Solution {
    public int[] solution(int[] arr) {
        int start = 0;
        int end = arr.length - 1;
        
        while (start <= end) {
            if (arr[start] == 2 && arr[end] == 2) {
                int[] res = new int[end - start + 1];
                for (int i = 0; i < res.length; i++) {
                    res[i] = arr[start];
                    start++;
                }
                return res;
            }
            if (arr[start] != 2) start++;
            if (arr[end] != 2) end--;
        }
        
        int[] answer = new int[1];
        answer[0] = -1;
        return answer;
    }
}