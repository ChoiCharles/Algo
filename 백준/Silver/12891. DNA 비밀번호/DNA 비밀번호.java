import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
	static int checkNum = 0;
	static int[] now = new int[4];
	static int[] checkArr = new int[4];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int result = 0;
		int s = Integer.parseInt(st.nextToken());
		int p = Integer.parseInt(st.nextToken());
		char array[] = new char[s];
		array = br.readLine().toCharArray();
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 4; i++) {
			checkArr[i] = Integer.parseInt(st.nextToken());
			if (checkArr[i] == 0) checkNum++;
		}
		
		for (int i = 0; i < p; i++) {
			Add(array[i]);
		}
		
		if (checkNum == 4) result++;
		
		for (int i = p; i < s; i++) {
			int j = i - p;
			Add(array[i]);
			Remove(array[j]);
			if (checkNum == 4) result++;
		}
		
		System.out.println(result);
		br.close();
	}
	
	private static void Add(char c) {
		switch(c) {
		case 'A':
			now[0]++;
			if (now[0] == checkArr[0]) checkNum++;
			break;
		case 'C':
			now[1]++;
			if (now[1] == checkArr[1]) checkNum++;
			break;
		case 'G':
			now[2]++;
			if (now[2] == checkArr[2]) checkNum++;
			break;
		case 'T':
			now[3]++;
			if (now[3] == checkArr[3]) checkNum++;
			break;
		}
	}
	
	private static void Remove(char c) {
		switch(c) {
		case 'A':
			if (now[0] == checkArr[0]) checkNum--;
			now[0]--;
			break;
		case 'C':
			if (now[1] == checkArr[1]) checkNum--;
			now[1]--;
			break;
		case 'G':
			if (now[2] == checkArr[2]) checkNum--;
			now[2]--;
			break;
		case 'T':
			if (now[3] == checkArr[3]) checkNum--;
			now[3]--;
			break;
		}
	}
}