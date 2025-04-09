package InterviewProgrames;

import java.util.*;

// Character occurrence in the string
public class StringOccurrence {
	public static void main(String[] args) {
		String str = "subbaram";
		char[] charArray = str.toCharArray();
		Map<Character, Integer> mp = new HashMap<>();
		
		for(char charater:charArray) {
			//System.out.println(c);
			if(mp.containsKey(charater)) {
				int count = mp.get(charater);
				mp.put(charater, count+1);
			}
			else {
				mp.put(charater, 1);
			}
		}
		
		System.out.println(mp);
		//System.out.println(c);
		//System.out.println(str);
	}
}
