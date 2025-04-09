package InterviewProgrames;

public class swapTowNumbers {
	public static void main(String[] args) {
		int a = 10;
		int b = 20;
		System.out.println("Value of a is "+a+" and value of b is "+b);
		
		int temp = a;
		a = b;
		b = temp;
		System.out.println("Value of a is "+a+" and value of b is "+b);
		
		swapTowNumbers obj = new swapTowNumbers();
		obj.swapWithoutTemp();
	}
	
	void swapWithoutTemp() {
		
		System.out.println("Swaping without temprory variable");
		int a = 10;
		int b = 20;
		System.out.println("Value of a is "+a+" and value of b is "+b);
		
		a = a + b;
		b = a - b;
		a = a - b;
		System.out.println("Value of a is "+a+" and value of b is "+b);
	}

}
