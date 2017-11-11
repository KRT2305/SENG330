package WEBAPI;

import org.springframework.context.ApplicationContext;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.tutorialspoint.HelloWorld;

public class MainApp {
	 public static void main(String[] args) {
	      ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");
	      
	      Vehicle objTruck = (Vehicle) context.getBean("test");
	      Vehicle objCompact = (Vehicle) context.getBean("test2");
	      
	      //Create a toString
	      System.out.println("Vehicle Type : " + objTruck.getType());
	      System.out.println("Vehicle License : " + objTruck.getLicense());
	      System.out.println("Vehicle Status : " + objTruck.getStatus());
	      
	      System.out.println("Vehicle Type : " + objCompact.getType());
	      System.out.println("Vehicle License : " + objCompact.getLicense());
	      System.out.println("Vehicle Status : " + objCompact.getStatus());
	      
	      
	      objTruck.setLicense(objCompact.getLicense());
	      
	      
	      System.out.println("Vehicle Type : " + objTruck.getType());
	      System.out.println("Vehicle License : " + objTruck.getLicense());
	      System.out.println("Vehicle Status : " + objTruck.getStatus());
	      
	      ((ConfigurableApplicationContext)context).close();
	 }
}
