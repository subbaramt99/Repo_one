package InterviewProgrames;

public class PrimeNumberCheck {
	public static void main(String[] args) {
		int num = 23;
		boolean isPrime = true;
		
		if(num > 2) {
			for(int i = 2; i<num; i++) {
				if(num % i == 0) {
					isPrime = false;
					System.out.println("Number is divisible by " + i);
					break;
				}
			}
		}
		
		
		if(isPrime) {
			System.out.print("Given numberi is prime");
		}else {
			System.out.print("Given numberi is not prime");
		}
		
	}

}
