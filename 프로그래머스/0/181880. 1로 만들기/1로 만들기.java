class Solution {
    public int[] arr = new int[31];
    
    public int div (int n) {
        if (n > 1 && arr[n] != 0) {
            return arr[n];
        } else if (n == 1) {
            return 0;
        }
        int count;
        if (n % 2 == 0) {
            count = div(n / 2);
            arr[n] = count + 1;
            return arr[n];
        } else {
            count = div((n - 1) / 2);
            arr[n] = count + 1;
            return arr[n];
        }
    }
    
    public int solution(int[] num_list) {
        arr[2] = 1;
        int answer = 0;
        for (int i = 0; i < num_list.length; i++) {
            answer = answer + div(num_list[i]);
        }
        return answer;
    }
}