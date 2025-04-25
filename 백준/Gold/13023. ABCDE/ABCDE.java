import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static ArrayList<Integer>[] a;
	static boolean visited[];
	static boolean arrive;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		arrive = false;
		a = new ArrayList[n];
		visited = new boolean[n];
		
		for (int i = 0; i < n; i++) {
			a[i] = new ArrayList<Integer>();
		}
		
		int s;
		int e;
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			a[s].add(e);
			a[e].add(s);
		}
		
		for (int i = 0; i < n; i++) {
			DFS(i, 1);
			if (arrive) break;
		}
		
		if (arrive) System.out.println("1");
		else System.out.println("0");
	}
	
	public static void DFS(int now, int depth) {
		if (depth == 5 || arrive) {
			arrive = true;
			return;
		}
		
		visited[now] = true;
		for (int i : a[now]) {
			if (!visited[i]) {
				DFS(i, depth + 1);
			}
		}
		
		visited[now] = false;
	}
}