import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int result = 1;
		int sum = 1;
		int start = 1;
		int end = 1;
		while (end != n) {
			if (sum == n) {
				result++;
				end++;
				sum += end;
			} else if (sum > n) {
				sum -= start;
				start++;
			} else if (sum < n) {
				end++;
				sum += end;
			}
		}
		System.out.println(result);
	}
}