import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] a = new int[n];
		int[] s = new int[n];

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(st.nextToken());
		}
		
		int insert_point;
		int insert_value;
		for (int i = 1; i < n; i++) {
			insert_point = i;
			insert_value = a[i];
			for (int j = i - 1; j >= 0; j--) {
				if (a[j] < a[i]) {
					insert_point = j + 1;
					break;
				}
				
				if (j == 0) {
					insert_point = 0;
				}
			}
			
			for (int j = i; j > insert_point; j--) {
				a[j] = a[j - 1];
			}
			
			a[insert_point] = insert_value;
		}
		
		s[0] = a[0];
		for (int i = 1; i < n; i++) {
			s[i] = s[i - 1] + a[i];
		}
		int sum = 0;
		for (int i = 0; i < n; i++) {
			sum += s[i];
		}
		
		System.out.println(sum);
	}
}