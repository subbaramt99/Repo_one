package InterviewProgrames;

public class LargestNumberInArray {
	public static void main(String[] args) {
		
		//int n = 10;
		//int[] arr1 = new int[n];
		
		int[] arr = {1,2,3,4,5,10,6,7,8,9};
		int max = arr[0];
		System.out.println(arr.length);
		
		for(int i=0; i<=arr.length-1; i++) {
			if(arr[i] > max) {
				 max = arr[i];
				 //System.out.println(max);
			}
			
		}
		System.out.println(max);
	}

}
