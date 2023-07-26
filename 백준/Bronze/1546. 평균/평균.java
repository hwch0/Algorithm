import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = Integer.parseInt(sc.nextLine()); // 과목의 수를 입력 받아 int로 변환
		String m = sc.nextLine(); // 성적을 문자열로 한번에 입력 받음
		int max = 0; // 최댓값을 담을 변수
		
		String[] str = m.split(" "); // 입력 받은 문자열을 " " 기준으로 잘라서 문자열타입의 배열에 넣음
		
		double total = 0; // 소숫점 이하까지 출력해주기 위해 double로 선언
		
		for(String s : str) { 
			
			if(max<Integer.parseInt(s)) { // 문자열 타입의 배열에서 문자열을 하나씩 가져와 정수로 변환뒤 max값과 대소 관계 판별
				max = Integer.parseInt(s);
			}
			total += Integer.parseInt(s); // 총 점수를 누적해서 합산
		}

		System.out.println( (total / (max * str.length)) *100);

	}

}
