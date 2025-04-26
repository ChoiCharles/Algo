import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static boolean visited[];
	static ArrayList<Integer>[] a;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int start = Integer.parseInt(st.nextToken());
	
		a = new ArrayList[n + 1];
		
		for (int i = 1; i < n + 1; i++) {
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
		
		for (int i = 1; i < n + 1; i++) {
			Collections.sort(a[i]);
		}
		
		visited = new boolean[n + 1];
		DFS(start);
		System.out.println();
		
		visited = new boolean[n + 1];
		BFS(start);
		System.out.println();
	}
	
	public static void DFS(int node) {
		System.out.print(node + " ");
		visited[node] = true;
		
		for (int i : a[node]) {
			if (!visited[i]) {
				DFS(i);
			}
		}
	}
	
	private static void BFS(int node) {
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.add(node);
		visited[node] = true;
		
		int now;
		while (!queue.isEmpty()) {
			now = queue.poll();
			System.out.print(now + " ");
			
			for (int i : a[now]) {
				if (!visited[i]) {
					visited[i] = true;
					queue.add(i);
				}
			}
		}
	}
}