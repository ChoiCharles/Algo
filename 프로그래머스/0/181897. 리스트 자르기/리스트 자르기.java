class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int[] answer = {};
        if (n == 1) {
            answer = slicing(num_list, 0, slicer[1]);
        } else if (n == 2) {
            answer = slicing(num_list, slicer[0], num_list.length - 1);
        } else if (n == 3) {
            answer = slicing(num_list, slicer[0], slicer[1]);
        } else {
            answer = slicing(num_list, slicer[0], slicer[1], slicer[2]);
        }
        return answer;
    }
    
    public static int[] slicing(int[] lst, int start, int end) {
        int[] after = new int[end - start + 1];
        for (int i = 0; i <= end - start; i++) {
            after[i] = lst[start + i];
        }
        return after;
    }
    
    public static int[] slicing(int[] lst, int start, int end, int mid) {
        int[] after = new int[(end - start) / mid + 1];
        for (int i = 0; i < after.length; i++) {
            after[i] = lst[start + i * mid];
        }
        return after;
    }
}