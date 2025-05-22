package PolymorphisumExample;

public class Polymorphisum {
	private String name;  // default value of string is Null
	private int mobileNo; // default value of integer is 0
	public String name1 = "Ram";
	
	public String getName() {
		return name;
	}
	
	public int getMobileNo() {
		return mobileNo;
	}
	
	public void setName(String txt) {
		 name = txt;
	}
	
	public void setMobileNo(int number) {
		mobileNo = number;
	}
	
	public static void main(String[] args){
		System.out.println("Hello all");
	}
	
	// ****************************Method overloading *************************************
	
	int add(int a, int b) {    // a=5, b=10;
		return a-b;
	}
	
	int add(int a, int b, int c) {    // a=5, b=10;
		return a+b+c;
	}
	
	int add(int a, float b) {    // a=5, b=10.50;
		System.out.println(a+b);
		return (int) (a+b);
	}
	
	int add(float a, int b) {    // a=5.5, b=10;
		System.out.println(a+b);
		return (int) (a*b);
	}
	
	
	int add(int a) {    // a=5, b=10;
		return a;
	}
	

	
	//**********************************************************************************
	
	
	float floatingPoint() {
		return 10.05f;
	}
	

	char character() {
		return 'h';
	}
	
	boolean Boolean() {
		return true;
	}
	
	String string(String a) {     // a = Anandh;
		System.out.println(a);
		return "Nisha";
	}
	
	Polymorphisum classes() {
		Polymorphisum obj = new Polymorphisum();
		return obj;
	}
	
	
}
