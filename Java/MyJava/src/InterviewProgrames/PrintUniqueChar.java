package InterviewProgrames;
import java.util.*;

public class PrintUniqueChar {
	public static void main(String[] args) {
		String str = "Hello World";
		char[] c = str.toCharArray();
		
		Set<Character> unique = new LinkedHashSet<>();
		
		for(char ch:c) {
			unique.add(Character.toUpperCase(ch));
		}
		System.out.println(unique);
		
		for(char c1:unique) {
			System.out.print(c1+", ");
		}
	}

}
