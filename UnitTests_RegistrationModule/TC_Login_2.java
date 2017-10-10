package External_portal;

import java.util.Random;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.Test;

public class Home {
	
	
	@Test
	public void go_Home() throws Exception
	{
		
		url="https://www.upsrtconline.co.in";
		
		
		
		
		
		//Loading the Chrome
		System.setProperty("webdriver.chrome.driver", "C:\\Chromedriver\\chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		WebDriverWait wait= new WebDriverWait(driver, 120);
		driver.manage().window().maximize();
		
		//Enter the URL
		driver.get(url);
		Thread.sleep(2000);
		
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//a[text()='Login/Register']"))).isDisplayed();
		driver.findElement(By.xpath("//a[text()='Login/Register']")).click();
System.out.println("Home Page Successfully loaded, hence TC_Home_1 passed");

wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//a[text()='Create an Account']"))).isDisplayed();
		driver.findElement(By.xpath("//a[text()='Create an Account']")).click();
System.out.println("Login Page Successfully loaded, hence TC_Login_1 passed");

wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//a[text()='create']"))).isDisplayed();
		driver.findElement(By.xpath("//a[text()='create']")).click();
System.out.println("Registration Page Successfully loaded, hence TC_Login_2 passed");



		

		
	}
	
	
	
	
	
	
}

