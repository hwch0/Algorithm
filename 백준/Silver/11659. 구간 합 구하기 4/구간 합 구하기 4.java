import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc  = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int[] arr = new int[N+1];
		int[] result = new int[M];
		arr[0] = 0;
		
		for(int i =1; i<=N; i++) {
			arr[i] = arr[i-1] + sc.nextInt();
		}
		
		for (int n =0; n<M; n++) {
			int i = sc.nextInt();
			int j = sc.nextInt();
			result[n] = arr[j] - arr[i-1];
		}
		
		for(int i : result) {
			System.out.println(i);
		}
		
	}

}
