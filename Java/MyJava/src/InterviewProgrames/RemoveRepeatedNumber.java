package InterviewProgrames;
import java.util.*;
public class RemoveRepeatedNumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Integer[] a = {11, 2, 3, 6, 2, 0};
		
		List<Integer> names = Arrays.asList(a);
		
		for(int l : names) {
			System.out.println(l);
		}
	

		int[] b = {2, 3, 4, 5, 22, 0};
		int[] rm = new int[8];  // creating empty array
		boolean com = false;
		
		for(int i=0; i<=a.length-1; i++) {
			for(int j=0; j<=b.length-1; j++) {
				if(a[i] == b[j]) {
					//System.out.println(a[i]);
					rm[i] = a[i];
				}
			}
		}
		
		for(int k=0; k <= rm.length - 1; k++) {
		System.out.println(rm[k]);
		}
		

	}
	}