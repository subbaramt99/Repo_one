package Robot;
import java.awt.Robot;
import java.awt.event.InputEvent;
import java.awt.event.KeyEvent;
import java.awt.AWTException;
import java.awt.event.*;


public class RobotClass {
	public static void main(String[] args) throws AWTException, Exception {
		
		Robot robot = new Robot();
		
		System.out.println("Hii");
		// Move the mouse to the coordinates (500, 500)
		robot.mouseMove(500, 500);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		
		//Thread.sleep(1000);
		
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		
		robot.delay(2000);
		String txt = "Hello World";
		//robot.keyPress(KeyEvent.VK_SHIFT);
		
		for (char c : txt.toCharArray()) {
			if(Character.isLowerCase(c)) {
				//System.out.println("Printing Uppercase ");
				//robot.keyPress(KeyEvent.VK_SHIFT);
				robot.keyPress(KeyEvent.getExtendedKeyCodeForChar(c));
				robot.keyRelease(KeyEvent.getExtendedKeyCodeForChar(c));
				//robot.keyRelease(KeyEvent.VK_SHIFT);
			}

			
		}
		
	}

}
