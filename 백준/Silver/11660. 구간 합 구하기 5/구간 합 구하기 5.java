import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int array[][] = new int[n + 1][n + 1];
		for (int i=1; i<=n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=1; j<=n; j++) {
				array[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int sumArray[][] = new int[n + 1][n + 1];
		for (int i=1; i<=n; i++) {
			for (int j=1; j<=n; j++) {
				sumArray[i][j] = sumArray[i - 1][j] + sumArray[i][j - 1] - sumArray[i- 1][j- 1] + array[i][j];
			}
		}
		for (int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			int result = sumArray[x2][y2] - sumArray[x1 - 1][y2] - sumArray[x2][y1 - 1] + sumArray[x1 - 1][y1 - 1];
			System.out.println(result);
		}
	}
}