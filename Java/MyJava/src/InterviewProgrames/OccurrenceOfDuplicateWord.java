package InterviewProgrames;

import java.util.HashMap;
import java.util.Map;

public class OccurrenceOfDuplicateWord {
	public static void main(String[] args) {
		String str = "all is well if your plan is well";
		String[] words = str.split(" ");
		
		Map<String, Integer> mp = new HashMap<>();
		
		for(String word : words) {
			if(mp.containsKey(word)) {
				int count = mp.get(word);
				//System.out.println("before count " + count);
				mp.put(word, count+1);
				//System.out.println("second tym added " + word);
				//System.out.println("Af count " + word);
			}else {
				mp.put(word, 1);
			}
		}
		System.out.println(mp);
	}
}
