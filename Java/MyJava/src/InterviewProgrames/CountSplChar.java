package InterviewProgrames;

public class CountSplChar {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "AbCD#eF";
		int upper = 0, lower = 0, special = 0;
		char[] c = str.toCharArray();
		
		System.out.println(c);
		
		for(char ch:c) {
			if(Character.isUpperCase(ch)) {
				upper++;
			}
			else if(Character.isLowerCase(ch)) {
				lower++;
			}else {
				special++;
			}
		}
		System.out.println("upper = "+upper);
		System.out.println("lower = "+lower);
		System.out.println("special = "+special);
	}

}
