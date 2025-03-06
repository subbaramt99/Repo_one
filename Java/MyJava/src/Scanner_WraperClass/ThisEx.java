package Scanner_WraperClass;

public class ThisEx {
	int a = 10; // Instance variable it is class level
	
	void show() {
		int a = 20; // Local variable it is method level
		System.out.println("Local variable is "+a);
		System.out.println("Instance variable is "+ this.a); // this keyword is use for referring instance variable
	}
	
	public static void main(String[] arg) {
		ThisEx T = new ThisEx();
		
		T.show();
	}

}
