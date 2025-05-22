package PolymorphisumExample;

public class Admin {
	
	public static void main(String[] args) {
		Polymorphisum obj10 = new Polymorphisum();
		
		
		System.out.println(obj10.add(5, 10, 20));
		
		System.out.println(obj10.add(5, 10.50f));
		
		System.out.println(obj10.add(5.5f, 10));
		
		//return ?;
	}

}
