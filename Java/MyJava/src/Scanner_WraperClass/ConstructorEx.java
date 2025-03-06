package Scanner_WraperClass;

import java.util.HashSet;
import java.util.Set;

public class ConstructorEx {
	// Default constructor or non parameterized constructor, no return type, it will execute when class is used
	public ConstructorEx() {
		System.out.println("I'm constructor");
	}
	
	// Parameterized constructor
	public void ConstructorEx(int a) {
		System.out.println("I'm Parameterized constructor");
	}
	
	// Parameterized constructor
	public void ConstructorEx(String a, double b) {
		System.out.println("I'm Parameterized constructor");
	}
	
	public void method (int id) {
		System.out.println(id);
	}
	public static void main(String[] args) {
		ConstructorEx A = new ConstructorEx();
		//ConstructorEx A1 = new ConstructorEx(10);
		//ConstructorEx A2 = new ConstructorEx("subu", 6.8);
		
		A.method(10);
	}

}
