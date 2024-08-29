class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        int attack;
        for (int i = 1; i <= number; i++) {
            attack = divisors(i);
            if (attack > limit) {
                answer += power;
            } else {
                answer += attack;
            }
        } 
        return answer;
    }
    
    public static int divisors(int n) {
        int count = 0;
        int sqrt = (int) Math.sqrt(n);
        for (int i = 1; i <= sqrt; i++) {
            if (n % i == 0) {
                count++;
                if (i != n / i) {
                    count++;
                }
            }
        }
        return count;
    }
}