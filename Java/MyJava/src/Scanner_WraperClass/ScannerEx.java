package Scanner_WraperClass;

import java.util.Scanner;

public class ScannerEx {
	public static void main(String[] args) {
		
		Scanner name = new Scanner(System.in);
		
		try {
			
			System.out.println("Please enter your name");
			String firstname = name.nextLine(); // it consider a entire line with space or without space
			System.out.println("Your name is " +firstname);
		
			System.out.println("Please enter your full name");
			String fullname = name.next(); // next method will not consider a text after 1st space
			System.out.println("Your ful name is " +fullname);
		}
		catch(Exception e) {
			System.out.println("Please enter valid input");
			
		}
		//name.close(); // closing the scanner is good to close after we used 
		
		
		System.out.print("Enter the alphabet");
		Scanner alp = new Scanner(System.in);
		
		String s = alp.next();
		
		name.close();
		
		switch(s){
		
		case "a":
			System.out.println(s+ "is a vovels");
			break;
		case "e":
			System.out.println(s+ "is a vovels");
			break;
		case "i":
			System.out.println(s+ "is a vovels");
			break;
		case "o":
			System.out.println(s+ "is a vovels");
			break;
		case "u":
			System.out.println(s+ "is a vovels");
			break;
			
			default:
				System.out.println(s+ "is a Consonent");
		
		}
	}

}
