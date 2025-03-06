package Day17_ExceptionalHandling;

public class ExceptionalHandling {
	
	static void ageCheck(int Age) throws MyException {
		
		if(Age < 18) {
			throw new MyException ("You are minor");
		}
		else {
			System.out.println("Eligble to vote");
		}
	}
	
	public static void main(String[] args) throws MyException {
		int num = 10;
		System.out.println(num);
		
		ageCheck(12);
		//int div = 10/0;   // It will not go next
		
		//System.out.println(num);
		//System.out.println(div);
		
		try {
			int div = 10/2;
			System.out.println(div);
		}
		catch(ArithmeticException e){
			System.out.println(e);
			System.out.println("Cannot divided by Zero");	
		}
		finally {
			System.out.println("It will be the final block to executed");
		}
		
	}
	

}
