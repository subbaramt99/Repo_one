package Collections;

import java.util.ArrayList;
import java.util.List;

public class ArrayListExample {
	public static void main(String[] args) {
		List ls = new ArrayList();
		List<String> ls1 = new ArrayList<String>();
		
		ls.add("A");
		ls.add("B");
		
		ls1.add("C");
		ls1.add("D");
		ls1.add("E");
		
		System.out.println(ls.size());
		System.out.println(ls1.get(0));
		System.out.println(ls1.set(2, "F"));
		System.out.println(ls1.remove(0)); // if we deleted or insert one index value after all index is move to forward or backword
		System.out.println(ls1);
		System.out.println(ls1.get(0));
		
		
	}

}
