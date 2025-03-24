import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

//import io.github.bonigarcia.wdm.WebDriverManager;

public class Introduction {
	public static void main(String[] args) {
		// Invoke Browser
		// Chrome -> ChromeDriver -> Method close
		// ChromeDriver is implementation 
		//ChromeDriver driver = new ChromeDriver(); // It might not work in other browser
		
		// WebDriver is a interface
		// So we want to use WebDriver implemented methods -> WebDriver methods + Class methods
		System.setProperty("webdriver.chrome.driver", "C:\\SUBBARAM T\\chrome webdriver\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		
		driver.get("https://ragulshettyacademy.com");
		
		// Chromedriver.exe -> chrome browser
		/* Step to invoke the chrome driver 
		1) System.setProperty("WebDriver.chrome.driver", "C:\SUBBARAM T\chrome webdriver\chromedriver_win32/chromedriver.exe")
		2) Selenium manager --> If we not set the chromedriver path it will automatically taken by selenium manager
		*/
		//System.setProperty("webdriver.chrome.driver", "C:\SUBBARAM T\chrome webdriver\chromedriver_win32/chromedriver.exe");


		  ChromeOptions options = new ChromeOptions();

		  options.addArguments("--remote-allow-origins=*");

		System.setProperty("webdriver.chrome.driver", "C:\\SUBBARAM T\\chrome webdriver\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe");

		WebDriver driver3 = new ChromeDriver(options);




		//Firefox

		System.setProperty("webdriver.gecko.driver", "/Users/rahulshetty/Documents/geckodriver");

		WebDriver driver1 = new FirefoxDriver();



		//Microsoft Edge

		System.setProperty("webdriver.edge.driver", "/Users/rahulshetty/Documents/msedgedriver");

		WebDriver driver2 = new EdgeDriver();






		driver.get("https://rahulshettyacademy.com");
		driver1.get("https://rahulshettyacademy.com");

		System.out.println(driver.getTitle());

		System.out.println(driver.getCurrentUrl());

		driver.close();

		//driver.quit();

	}

}
