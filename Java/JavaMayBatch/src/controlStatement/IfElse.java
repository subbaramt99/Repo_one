package controlStatement;

public class IfElse {
	public static void main(String[] args) {
		int age = 0;
		
		if(age >= 18 && age <= 34) {
			if( age >= 21) {   // nested if conditions
				System.out.println("eleigible for election nomination");
			}
			System.out.println("Adult");
		}
		else if(age >= 35  && age <= 70) {
			System.out.println("Gentelman");
		}
		else if (age >= 71  && age <= 99) {
			System.out.println("Aged person");
		}
		else if (age < 18 && age >= 1) {
			System.out.println("child");
		}
		else  {
			System.out.println("Please enter valid age");
		}
		
	}

}
