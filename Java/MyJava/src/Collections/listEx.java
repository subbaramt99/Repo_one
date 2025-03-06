package Collections;

import java.util.ArrayList; // importing Arraylist alone
import java.util.HashMap; // importing list 
import java.util.*; // importing all the packages under java.util
import java.util.LinkedList;

public class listEx {
	public static void main(String[] args) {
		List<Integer> li = new ArrayList<>();
		LinkedList<Integer> li1 = new LinkedList<Integer>();
		List<Integer> li2 = new Vector<Integer>();
		
		li.add(10); // Index 0
		li.add(20); // Index 1 ......
		li.add(30);
		li.add(50);
		li.add(40);
		
		li1.add(10);
		li1.add(20);
		li1.add(30);
		li1.add(50);
		li1.add(40);
		
		li2.add(10);
		li2.add(20);
		li2.add(30);
		//li1.add("sam"); it will not allow string as it is decleared as int
		
		System.out.println(li);
		System.out.println(li1);
		System.out.println(li2);
		
		// To print size of list
		int size = li.size();
		System.out.println(size);
		System.out.println(li.get(2));
		System.out.println(li.remove(3));
		System.out.println(li);
		
		
	}

}
