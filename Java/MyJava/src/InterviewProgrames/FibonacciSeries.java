package InterviewProgrames;

public class FibonacciSeries {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num = 10;
		int a = 0, b=1;
		
		System.out.println(a);
		System.out.println(b);
		
		for(int i=2; i<=num; i++) {
			int nxt = a + b;
			System.out.println(nxt);
			a = b;
			b = nxt;
		}
	}

}
