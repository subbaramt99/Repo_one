package InterviewProgrames;
import java.util.*;

public class NoOfTimeCharReapeat {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String str = "xaacbaxxxb";
		char[] c = str.toCharArray();
		
		Map<Character, Integer> mp = new LinkedHashMap<>();
		
		for(char ch: c) {
			if(mp.containsKey(ch)) {
				int count = mp.get(ch);
				mp.put(ch, count+1);	
			}
			else {
				mp.put(ch, 1);
			}
		}
		System.out.println(mp);
		
		for(Map.Entry<Character, Integer> entry : mp.entrySet()) {
			System.out.print(entry.getKey());
			System.out.print(entry.getValue());
		}

	}

}
