import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> que = new PriorityQueue<>((o1, o2) -> {
			int first_abs = Math.abs(o1);
			int sec_abs = Math.abs(o2);
			if (first_abs == sec_abs) {
				return o1 > o2 ? 1 : -1;
			} else {
				return first_abs - sec_abs;
			}
		});
		
		int req;
		for (int i = 0; i < n; i++) {
			req = Integer.parseInt(br.readLine());
			if (req == 0) {
				if (que.isEmpty()) {
					System.out.println("0");
				} else {
					System.out.println(que.poll());
				}
			} else {
				que.add(req);
			}
		}
	}
}