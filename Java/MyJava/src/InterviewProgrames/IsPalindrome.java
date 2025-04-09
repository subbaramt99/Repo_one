package InterviewProgrames;

public class IsPalindrome {
	public static void main(String[] args) {
		String str = "subbaram";
		String rev = "";
		
		for (int i=str.length()-1; i>=0; i--) {
			rev = rev + str.charAt(i);
		}
		if(str.equals(rev)) {
			System.out.println("Given string is palindrome");
		}else {
			System.out.println("Given string is not palindrome");
		}
	}

}
