package InterviewProgrames;
import java.util.*;

public class LargestWordInString {
	public static void main(String[] args) {
		String str = "an apple a keeps doctor away subbaram a";
		String[] words = str.split(" ");
		
		int largest_len = 0;
		String largest_word = "";
		
		for(String c: words) {
			if(c.length() > largest_len) {
				largest_len = c.length();
				largest_word = c;
			}
		}
		System.out.println(largest_len);
		System.out.println(largest_word);
		
	}

}
