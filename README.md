# DABOTICS_T02
Repository contain the Second task of DABOTICS India Pvt. Ltd. Python Intern 
# OTP Verification is the process of verifying a user by sending a unique password so that the user can be verified before completing a registration or payment process. Most of the time, we get an OTP when we make an online payment, or when we forget our password, or when creating an account on any online platform. Thus, the sole purpose of an OTP is to verify the identity of a user by sending a unique password. 

# Explanation:

The main objectives that need to be fulfilled while making this projects are:
Creating a GUI for this project.
Generating a random number as OTP.
Sending the OTP to the stated Mobile number.
Checking whether the OTP is valid or not.
Resending the OTP.

First of all, creating a GUI for our project will make use of the “tkinter” module, from “future. moves” we will import the module. The most major step is to create the instance of the tkinter frame i.e. tk(). This will help to display the window and manage all the components of the tkinter application. In addition to this, with the help of “.title()” & “.geometry()” we will set the title and dimensions for the window. With this, we will also draw the Canvas for OTP Verification with the help of “.canvas()” and by using “.place()” we will provide the dimensions as parameters for placing our canvas.

We will create a submit button and resend button with the help of “.Buttons()”  to trigger the submit and resend command. With the help of this module, we will create the label widget stating OTP verification and an entry widget to provide space for the user to write.

After doing so we will see that our GUI will get ready for the project. Now, to provide the actual functionality we will use API i.e. Twilio.

In this, firstly we will use the “random. randint()” of the random module to generate the random number which will later be considered as OTP.

The next step is to send the OTP. For this process, firstly you have to make a Twilio account

After this, you will be provided with an account sid and auth token. With the help of “twilio.rest.Client(account sid, auth token)” you will first allow your query to metadata. For sending the message we will use “client. messages.create(to=[“”], from_=” “, body=” “)” . And all of this functionality is stated under UDF resendOTP()

The next step is to check the OTP. For this, firstly we will store the user input and now will run a try and except block in which under the try block we will compare that if user input is the same as the generated random number then a message box will appear stating login successfully and the random number stored variable will get updated. And again if the user entered the same OTP then the message box will say that the user has already logged in and finally when the user will enter the wrong OTP then the message box will throw the message of invalid OTP. The syntax for the message box is “messagebox. showinfo ()”. All of this is covered under UDF checkOTP().

After entering the OTP the user can click the submit button and if he/she wants the OTP again then the one can click on the Resend OTP button. In the end, we will run a mainloop for all the functionalities to get executed.
