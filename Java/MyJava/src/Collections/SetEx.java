package Collections;

import java.util.*;

public class SetEx {
	public static void main(String[] args) {
		//set<Integer> st = new HashSet<Integer>();
		Set<Integer> st=new HashSet<Integer>();
		
		st.add(10);
		st.add(20);
		st.add(30);
		st.add(40);
		st.add(50);
		st.add(60);
		System.out.println(st);
		
		int i=st.size();
		System.out.println(i);
		
		//enhance for loop
		
		for(int k:st) {
			System.out.println(k);
		
		}
		
		// LinkedHashSet - Insertion order
		
		Set<Integer> st1=new LinkedHashSet<Integer>();
		st1.add(10);
		st1.add(20);
		st1.add(30);
		st1.add(40);
		st1.add(50);
		st1.add(60);
		System.out.println(st1);
		
		// TreeSet -- Ascending order
		Set<Integer> st2=new TreeSet<Integer>();
		st2.add(10);
		st2.add(20);
		st2.add(30);
		st2.add(40);
		st2.add(50);
		st2.add(60);
		System.out.println(st2);
		
		//List to set
		
		//Set<String> ste = new ArrayList<String>();
		
		
		
	}

}
