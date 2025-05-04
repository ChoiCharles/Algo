import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			if (a == 10) {
				System.out.println(10);
				continue;
			}
			int now = a % 10;
			for (int j = 1; j < b; j++) {
				now = now * a;
				now = now % 10;
			}
			if (now == 0) {
				System.out.println(10);
			} else {
				System.out.println(now);				
			}
		}
	}
}