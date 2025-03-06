package Scanner_WraperClass;

public class WraperEx {
	
	public static void main(String[] args) {
	int a = 10;
	// int.  --> will not work as it is primitive data type
	
	Integer i =20; // Auto boxing --> Converting primitive data type into Object
	//Interger. --> will have number of method it it
	
	System.out.println(i);
	
	int j = i.intValue(); // it will return a integer value
	
	String k ="123";  // Auto Unboxing
	System.out.println(k+10);
	
	int b = Integer.parseInt(k);
	System.out.println(b+10);
	
	}
}
