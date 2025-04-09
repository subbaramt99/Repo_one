package InterviewProgrames;
import java.util.*;

public class UniqueCharacter {
	public static void main(String[] args) {
		String str = "subbaram";
		char[] charArray = str.toCharArray();
		
		Map<Character, Integer> mp = new HashMap<>();
		
		for(char character:charArray) {
			if(mp.containsKey(character)) {
				int count = mp.get(character);
				//mp.put(character, count+1);
					
				}else {
					mp.put(character, 1);
				}	
		}
		System.out.println(mp.keySet()); // In map key wil not duplicate i am printing keyset
		System.out.println(mp);
	}

}
