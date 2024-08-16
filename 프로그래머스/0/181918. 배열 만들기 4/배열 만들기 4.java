class Solution {
    public int[] solution(int[] arr) {
        int arrLength = arr.length;
        int[] result = new int[arrLength];
        int resultLength = 0;
        int i = 0;
        while (i < arrLength) {
            if (resultLength == 0) {
                result[0] = arr[i];
                resultLength++;
                i++;
            } else {
                if (result[resultLength - 1] < arr[i]) {
                    result[resultLength] = arr[i];
                    resultLength++;
                    i++;
                } else {
                    result[resultLength - 1] = 0;
                    resultLength--;
                }
            }
        }
        int[] stk = new int[resultLength];
        System.arraycopy(result, 0, stk, 0, resultLength);
        
        return stk;
    }
}