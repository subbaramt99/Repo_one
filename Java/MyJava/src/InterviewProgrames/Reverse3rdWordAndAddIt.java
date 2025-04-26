package InterviewProgrames;

import java.util.*;

// Reverse 3rd Word of given string and add it with same
public class Reverse3rdWordAndAddIt {
	public static void main(String[] args) {
		String str = "an apple a keeps doctor away subbaram a";
		String[] words = str.split(" ");
		String rev = "";
		
		for(int i=0; i<=words.length; i++) {
			//System.out.println(c);
			if(i == 3) {
				String word = words[i];
				//String[] c = word.toCharArray();
				
				for(int j=word.length()-1; j>=0; j--) {
					rev = rev + word.charAt(j);
					}
				}
		}
		words[3] = rev;
		
		System.out.println(rev);
		for(int k=0; k<=words.length-1; k++) {
			System.out.print(words[k] + " ");
		}
		
		//System.out.println(str);
	}
}
