import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int maxScore = 0;
		int sum = 0;
		int n = sc.nextInt();
		int scoreArray[] = new int[n];
		for (int i = 0; i < n; i++) {
			scoreArray[i] = sc.nextInt();
		}
		for (int i = 0; i < n; i++) {
			if (scoreArray[i] > maxScore) maxScore = scoreArray[i];
			sum += scoreArray[i];
		}
		System.out.print(sum * 100.0 / maxScore / n);
	}
}