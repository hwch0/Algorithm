import java.util.Iterator;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = Integer.parseInt(sc.nextLine());
		String m = sc.nextLine(); // 숫자 n개를 하나의 문자열로 입력 받는다
		int total = 0;
		// 하나의 문자열로 입력받은 숫자를 char 배열로 변환
		char[] chars = m.toCharArray();

		for(char c : chars) {
			total = total+ Character.getNumericValue(c);
		}
		
		
		System.out.println(total);
	}

}
