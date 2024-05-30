import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String numString = sc.next();
		char[] numArray = numString.toCharArray();
		int result = 0;
		for (int i = 0; i < numArray.length; i++) {
			result += numArray[i] - '0';
		}
		System.out.print(result);
	}
}