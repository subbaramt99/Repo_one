package Arrays;

public class arraysExample {
	public static void main(String[] args) {
		
		int a;    // default value of data type
		
		int arr[] = new int[5];  // empty array
		
		int arr1[] = {1, 2, 4, 6, 2, 1, 5, 7, 8, 0, 2};
		
		System.out.println(arr[4]);
		
//		System.out.println(arr1[0]);
//		System.out.println(arr1[1]);
//		System.out.println(arr1[2]);
//		System.out.println(arr1[3]);
		
		int len = arr1.length;
		
		String str = arr1.toString();
		
		System.out.println("Length of arr1 is " + arr1.length);
		
		System.out.println("Length of arr1 is " + len);
		System.out.println("Length of arr1 is " + str);
		
		for(int index = 0; index <= 10; index++)
		{
			System.out.println(arr1[index]);
		}
		
		//********************* MUltidimentional array *************************
		
		int[][] arr2 = new int[2][2];  // empty array
		
		int[][] arr3 = {
				{1, 2, 3, 4},
				{5, 6, 7, 8},
				{9, 10, 11, 12},
				{13, 14, 15, 16}
		};
		
		System.out.println("I'm multi dimentioanl array " + arr2[0][0]);
		System.out.println("I'm multi dimentioanl array " + arr3[1][3]);
		
		System.out.println("length is " + arr3.length);
		
		
		for(int i=0; i<arr3.length; i++) {
			
			for(int j=0; j<arr3.length; j++) {
				
				System.out.println(arr3[i][j]);
				
			}
		}
		
		//****************************** for each loop *************************
		
		System.out.println("For each is running");
		
		//int arr1[] = {1, 2, 4, 6, 2, 1, 5, 7, 8, 0, 2};
		
		for(int c:arr) {            // i is value of the place 
			System.out.println(c);
		}
		
		// **************************** char array ******************************
		
		char[] ch = {'a', 'f', 'r', 'g', 'g'};  // Character array
		
		for(char c : ch) {
			System.out.println(c);
		}
		
		
	}
	


}
