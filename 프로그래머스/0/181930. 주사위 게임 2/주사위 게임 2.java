class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        int flag = 0;
        if (a == b) {
            flag += 1;
        }
        if (b == c) {
            flag += 1;
        }
        if (a == c) {
            flag += 1;
        }
        if (flag == 0) {
            answer = a + b + c;
        } else if (flag == 1) {
            answer = (a + b + c) * (a*a + b*b + c*c);
        } else {
            answer = (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c);
        }
        return answer;
    }
}