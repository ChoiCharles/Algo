import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		long[] array = new long[n];
		for (int i = 0; i < n; i++) {
			array[i] = Long.parseLong(st.nextToken());
		}
		Arrays.sort(array);
		int result = 0;
		for (int i = 0; i < n; i++) {
			long find = array[i];
			int start = 0;
			int end = n - 1;
			while (start < end) {
				if (array[start] + array[end] == find) {
					if (start != i && end != i) {
						result++;
						break;
					} else if (start == i) {
						start++;
					} else if (end == i) {
						end--;
					}
				} else if (array[start] + array[end] < find) {
					start++;
				} else {
					end--;
				}
			}
		}
		System.out.println(result);
		br.close();
	}
}