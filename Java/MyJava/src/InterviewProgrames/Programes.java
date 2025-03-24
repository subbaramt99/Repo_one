package InterviewProgrames;

public class Programes {
	
	public static String reverseOfString(String name) {
		//String str = "subbaram";
		String rev = "";
		
		for(int i=name.length()-1; i >=0; i--) {
			rev = rev + name.charAt(i);
		}
		return rev;
	}
	
	public static void findMissingNumber() {
		int[] num = {5, 3, 0, 1};
		//int n = num.length;
		
		/*for(int i=0; i<=num.length; i++) {
			if(num[i] != i) {
				System.out.println(i);
			}*/
		for(int n : num) {
			System.out.println(num[n]);
		}
			
		
		
			
	}
	
	public static void main(String[] args) {
		//int[] num = {5, 2, 0};
		System.out.println(reverseOfString("subbaram"));
		findMissingNumber();
	}

}
