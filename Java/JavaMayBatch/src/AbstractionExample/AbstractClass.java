package AbstractionExample;

abstract class AbstractClass {
	
	abstract void Building();  // Abstract method
	
	abstract void Kitchen();  // Abstract method
	
	abstract void LivingRoom();  // Abstract method
	
	abstract void BedRoom();  // Abstract method
	
	
	void house() {  // Concrete method
		System.out.println("Welcome to my House");
	}

}
