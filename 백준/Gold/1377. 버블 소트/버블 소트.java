import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		data[] a = new data[n];
		for (int i = 0; i < n; i++) {
			a[i] = new data(Integer.parseInt(br.readLine()), i);
		}
		Arrays.sort(a);
		
		int max = 0;
		for (int i = 0; i < n; i++) {
			if (max < a[i].index - i) {
				max = a[i].index - i;
			}
		}
		
		System.out.println(max + 1);
	}
}

class data implements Comparable<data> {
	int value;
	int index;
	
	public data(int value, int index) {
		super();
		this.value = value;
		this.index = index;
	}
	
	@Override
	public int compareTo(data d) {
		return this.value - d.value;
	}
}