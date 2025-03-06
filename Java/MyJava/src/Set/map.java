package Set;
//package Map:

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class map {
	public static void main(String[] args) {
		Map<Integer,String> map = new HashMap<Integer,String>();
		
		String str = null;
		
		//HashMap
		map.put(10, "java");
		map.put(20, "abc");
		map.put(30, "cde");
		map.put(40, "fgh");
		map.put(50, "ijk"); // Last insert will print 1st print
		map.put(null, null);
		map.put(60, null);
		
		System.out.println(map);
		
		// LinkedHashMap
		LinkedHashMap<Integer,String> Lmap = new LinkedHashMap<Integer,String>();
		
		Lmap.put(10, "java");
		Lmap.put(20, "abc");
		Lmap.put(30, "cde");
		Lmap.put(40, "fgh");
		Lmap.put(50, "ijk"); // Last insert will print 1st print
		Lmap.put(null, null);
		Lmap.put(60, null);
		
		System.out.println(Lmap); // It will print ascending order of key value
		
		// TreeMap
		
		TreeMap<Integer,String> Tmap = new TreeMap<Integer,String>();

		Tmap.put(10, "java");
		Tmap.put(20, "abc");
		Tmap.put(30, "cde");
		Tmap.put(40, "fgh");
		Tmap.put(50, "ijk"); // Last insert will print 1st print
		//Tmap.put(null, null); // TreeMap will not allow null key value
		Tmap.put(60, null);
		Tmap.put(50, "lmn"); // It will not allow duplicate key value and it take latest key value
		
		System.out.println(Tmap); // It will print ascending order of key value
		
		
		//HashTable
		
		Map<Integer,String> Hashtable = new Hashtable<Integer,String>();
		

		Hashtable.put(10, "java");
		Hashtable.put(20, "abc");
		Hashtable.put(30, "cde");
		Hashtable.put(40, "fgh");
		Hashtable.put(50, "ijk"); 
		Hashtable.put(null, null);
		Hashtable.put(60, null);
		
		System.out.println(Hashtable); 
		
		
		// ConcurrentHashTable
		
		Map<Integer,String> CHashtable = new ConcurrentHashMap<Integer,String>();
		

		CHashtable.put(10, "java");
		CHashtable.put(20, "abc");
		CHashtable.put(30, "cde");
		CHashtable.put(40, "fgh");
		CHashtable.put(50, "ijk"); 
		CHashtable.put(null, null);
		CHashtable.put(60, null);
		
		System.out.println(Hashtable); 
		
	}

}
