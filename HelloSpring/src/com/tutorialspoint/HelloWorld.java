package com.tutorialspoint;

public class HelloWorld {
   private String message;
   private String secret;

   public void setMessage(String message){
      this.message  = message;
   }
   public void getMessage(){
      System.out.println("Your Message : " + message);
   }
   
   public void setSecret(String secret) {
	   this.secret = secret;
   }
   public void getSecret() {
	   System.out.println("Secret Question : " + secret);
   }
   
   
}