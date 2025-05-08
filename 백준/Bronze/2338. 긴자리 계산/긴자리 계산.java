import java.util.Scanner;
import java.math.BigInteger;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		BigInteger x = new BigInteger(sc.next());
		BigInteger y = new BigInteger(sc.next());
		System.out.println(x.add(y));
		System.out.println(x.subtract(y));
		System.out.println(x.multiply(y));
	}
}