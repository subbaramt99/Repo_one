package Strings;

public class Strings {
	public static void main(String[] args) {
		char c = 'a'; // Character
		
		String S = "A"; // String
		String T = new String("Hai");  // String
		String X = "Hai I am subbaram";
		
		int a[] = {1,2,3,4};
		
		System.out.println(S);
		System.out.println(T);
		
		//int Tlen = T.length();
		System.out.println("Length of T is " + T.length());
		System.out.println("Length of S is " + S.length());
		
		System.out.println(a[2]);
		
		//System.out.println(S.charAt(2));
		System.out.println(S.toLowerCase());
		System.out.println(S.concat("ji")); // Adding strings ==> Hello + Ji ==> Helloji
		System.out.println(S.compareTo("B")); 
		
	}
}
