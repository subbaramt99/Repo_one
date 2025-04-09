package OOPs;

public class Person {
	public static void name() {  // Normal method it will execute when it called
		System.out.print("I'm Vignesh");
		city();
	}
	public static void age() {   // Normal method it will execute when it called 
		System.out.println("30");	
	}
	
	public static void city() {   // Normal method it will execute when it called
		//name();
		System.out.println("Chennai");
		age();
	}
	


}
