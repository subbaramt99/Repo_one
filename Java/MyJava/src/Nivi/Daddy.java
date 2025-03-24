package Nivi;
//import Subbu.Mummy;

public class Daddy {
	
    public static void main(String[] args) {
    	Daddy nividaddy = new Daddy();
    	nividaddy.task2();
    }
	public static void task1() {
		System.out.println("Nivi Daddy is doing public work");
        Subbu.Mummy.task1();
	}
	private static void task2() {
		System.out.println("Nivi Daddy is doing private work");
		Daddy.task1();
		//nividaddy.main(null);
	}
	//static Daddy nividaddy = new Daddy();
}
