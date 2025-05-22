package AbstractionExample;

public class Admin{

	public static void main(String[] args) {
		InterfaceHome obj = new InterfaceHome();
		
		//obj.house();   // Concrete method
		obj.BedRoom();  // abstract method
		obj.Kitchen();  // abstract method
		obj.Building();  // abstract method
		obj.MasterBedRoom();
}
	
	

}
