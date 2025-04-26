package InterviewProgrames;
import java.util.*;

public class PrintOnlyDuplicates {

	public static void main(String[] args) {
		String str = "i am working i am not coming";
		String[] words = str.split(" ");
		
		Map<String, Integer> mp = new HashMap<>();
		Map<String, Integer> mp1 = new HashMap<>();
		int count = 0;
		
		for(String word:words) {
			mp.put(word, count+1);
			mp1.put(word, mp1.getOrDefault(word, 0)+1);
			
		}
		System.out.println(mp);
		System.out.println(mp1);

	}

}
