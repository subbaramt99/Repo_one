package Subbu;
import Nivi.*;

public class Daddy extends Mummy{
	
    public static void main(String[] args) {
    	Daddy subbudaddy = new Daddy();
        //System.out.println("Subbu daddy Hello World");
        //Daddy.task1();
        Daddy.task2();
    }
	public static void task1() {
		System.out.println("Subbu Daddy is doing public work");
	}
	private static void task2() {
		System.out.println("Subbu Daddy is doing private work");
		Daddy.task1();
	}
	
}
