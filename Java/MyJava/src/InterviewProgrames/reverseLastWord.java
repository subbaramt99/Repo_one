package InterviewProgrames;

import java.util.Arrays;
import java.util.List;

public class reverseLastWord {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "This is java";
		String[] words = str.split(" "); // Split the sentence and store it in string array
		
		//System.out.println(words);
		
		// Converting array into list using Array.aslist
		List<String> wordsList = Arrays.asList(words);
		
		System.out.println(wordsList.get(1));
		
		String lastword = words[words.length-1];
		String rev = "";
		
		System.out.println("Last word of the statement is " + lastword);
		
		for(int i = lastword.length()-1; i >= 0; i--) {
			//System.out.println(lastword.charAt(i));
			rev = rev + lastword.charAt(i);
		}
		System.out.println("Reverse of the last word is "+rev);
	}

}
