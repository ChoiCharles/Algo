import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String st = sc.next();
		int l = st.length();
		int[] a = new int[l];
		
		for (int i = 0; i < l; i++) {
			a[i] = Integer.parseInt(st.substring(i, i + 1));
		}
		
		int max;
		for (int i = 0; i < l; i++) {
			max = i;
			for (int j = i + 1; j < l; j++) {
				if (a[j] > a[max]) {
					max = j;
				}
			}
			
			if (a[i] < a[max]) {
				int temp = a[i];
				a[i] = a[max];
				a[max] = temp;
			}
		}
		
		for (int i = 0; i < l; i++) {
			System.out.print(a[i]);
		}
	}
}