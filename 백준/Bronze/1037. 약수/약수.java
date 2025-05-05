import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int x = Integer.parseInt(st.nextToken());
		int max = x;
		int min = x;
		for (int i = 1; i < n; i++) {
			int now = Integer.parseInt(st.nextToken());
			if (now < min) {
				min = now;
			} else if (now > max) {
				max = now;
			}
		}
		System.out.println(max * min);
	}
}