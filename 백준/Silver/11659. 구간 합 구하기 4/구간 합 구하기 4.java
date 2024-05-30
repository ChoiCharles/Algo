import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		long array[] = new long[n];
		array[0] = sc.nextInt();
		for (int i = 1; i < n; i++) {
			array[i] = sc.nextInt() + array[i - 1];
		}
		int start;
		int end;
		for (int i = 0; i < m; i++) {
			start = sc.nextInt() - 1;
			end = sc.nextInt() - 1;
			if (start == 0) {
				System.out.println(array[end]);
			} else {
				System.out.println(array[end] - array[start - 1]);
			}
		}
	}
}