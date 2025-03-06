package Java_Day2;
//object creation
import Java_Day1.Helloworld; // import PackageName.ClassName <Syntex of import>
import Java_Day1.*;


public class Main {
	
	
	
	public static void main(String[] args) {
		MyClass obj = new MyClass(); //object creation
		//Helloworld obj1 = new Helloworld();
		
		System.out.println(obj.x); // Accessing the property
		
		//System.out.println(obj1.str);
		
		Helloworld.main(args);
		Java_Day1.Helloworld.main(args);
		
		//Helloworld obj1 = new Helloworld();
		
		//System.out.print(obj1.Greeting);
	}

}
