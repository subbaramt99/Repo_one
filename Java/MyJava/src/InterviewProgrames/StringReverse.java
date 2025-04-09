package InterviewProgrames;

public class StringReverse {
	public static void main(String[] args) {
		String str = "subbaram";
		String rev = "";
		
		for (int i=str.length()-1; i>=0; i--) {
			rev = rev + str.charAt(i);
		}
		System.out.println(rev);
		
		StringReverse obj = new StringReverse();
		System.out.print(obj.reverse(str));
	}
	
	public String reverse(String str) {
		//String rev = "";
		// Using string builder edit the string and use reverse method
		String rev1 = new StringBuilder(str).reverse().toString();
		return rev1;
	}

}
