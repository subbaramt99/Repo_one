package controlStatement;

public class Loops {
	public static void main(String[] args) {
		// For loop
		// a = a + 1 or a += 1 or a++
		int b = 0;
		int c = 20;
		
		//************************************** For loop *************************************
		
		for(int a = 0; a<=10; a += 1) {    // a = a + 1
			
			if(a<5)continue;
			
			System.out.println(a + "*" + 5 + "=" + a*5);
		}
		
		//****************************** while *******************************
		
		while(b<=10) {
			System.out.println(b);
			b++;
			if(b>5) break;
		}
		
		//**************************** do while *******************************
		// int c = 20;
		
		do {
			System.out.println("do while loop is running");
			System.out.println(c);
			c-=5;
			
		}while(c>10);
		
		//break;
		
	}

}
