package Scanner_WraperClass;

public class ChainConstructorEx {

	public ChainConstructorEx() {
		this("subbu");
		System.out.println("Default constructor");	
	}

	public ChainConstructorEx(int a, float b) {
		this.display();
		System.out.println("Integer and float constructor");
	}
	
	public ChainConstructorEx(String s) {		
		this(12, 33.4f);
		System.out.println("String constructor");
		System.out.println(s);
	}
	
	void display() {
		System.out.println("this normal method");
	}
	
	public static void main(String[] args) {
		ChainConstructorEx A = new ChainConstructorEx();

	}

}
