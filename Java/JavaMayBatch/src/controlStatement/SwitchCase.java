package controlStatement;

public class SwitchCase {
	public static void main(String[] args) {
		int day = 15;
		
		switch (day) {  // true
			case 1:
				System.out.println("Monday");
			case 2:
				System.out.println("Tuesday");
			case 3:
				System.out.println("Wdnesday");
				break;
			case 4:
				System.out.println("Thursday");
				break;
			case 5:
				System.out.println("Friday");
			default:
				System.out.println("Please enter valid day");
		}
		
		String W_day = "hello";
		
		switch (W_day) {  // true
			default:
				System.out.println("Please enter valid w_day");
				break;
			case "Monday":
				System.out.println(1);
				break;
			case "Tuesday":
				System.out.println(2);
				break;
			case "Wednesday":
				System.out.println(3);
				break;

			
		}
				
	}

}
