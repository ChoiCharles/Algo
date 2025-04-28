import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static boolean visited[];
	static int[] distance;
	static ArrayList<Edge>[] a;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		a = new ArrayList[n + 1];
		
		for (int i = 1; i <= n; i++) {
			a[i] = new ArrayList<Edge>();
		}
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			
			while (true) {
				int e = Integer.parseInt(st.nextToken());
				if (e == -1) break;
				
				int v = Integer.parseInt(st.nextToken());
				a[s].add(new Edge(e, v));
			}
		}
		
		distance = new int[n + 1];
		visited = new boolean[n + 1];
		BFS(1);
		
		int max = 1;
		for (int i = 2; i <= n; i++) {
			if (distance[max] < distance[i]) max = i;
		}
		
		distance = new int[n + 1];
		visited = new boolean[n + 1];
		BFS(max);
		Arrays.sort(distance);
		System.out.println(distance[n]);
	}
	
	public static void BFS(int index) {
		Queue<Integer> queue = new LinkedList<Integer>();
		queue.add(index);
		visited[index] = true;
		while (!queue.isEmpty()) {
			int now = queue.poll();
			for (Edge i : a[now]) {
				int e = i.e;
				int v = i.value;
				if (!visited[e]) {
					visited[e] = true;
					queue.add(e);
					distance[e] = distance[now] + v;
				}
			}
		}
	}
}

class Edge {
	int e;
	int value;
	public Edge(int e, int value) {
		this.e = e;
		this.value = value;
	}
}