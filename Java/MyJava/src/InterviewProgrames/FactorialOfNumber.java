package InterviewProgrames;

public class FactorialOfNumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num = 5;
		int fac = 1;
		
		for(int i=1; i<=num; i++) {
			fac = fac * i;
		}
		System.out.println("Factorial of " + num + " is " + fac);
		
	}

}
