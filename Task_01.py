import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client
import random


# Twilio configuration
ACCOUNT_SID = 'AC_____________________________693f0'
AUTH_TOKEN = '0_____________________________f'
TWILIO_PHONE_NUMBER = '_____________'

# Create a Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

class OTPVerification:
    def __init__(self, master):
        self.master = master
        master.title('OTP Verification')

        # Create GUI elements
        self.phone_number_label = tk.Label(master, text='Phone Number:')
        self.phone_number_label.pack()

        self.phone_number_entry = tk.Entry(master, width=20)
        self.phone_number_entry.pack()

        self.generate_otp_button = tk.Button(master, text='Generate OTP', command=self.generate_otp)
        self.generate_otp_button.pack()

        self.otp_label = tk.Label(master, text='OTP:')
        self.otp_label.pack()

        self.otp_entry = tk.Entry(master, width=20)
        self.otp_entry.pack()

        self.verify_otp_button = tk.Button(master, text='Verify OTP', command=self.verify_otp)
        self.verify_otp_button.pack()

    def generate_otp(self):
        # Generate a random OTP
        otp = ''.join(str(random.randint(0, 9)) for _ in range(6))

        # Send the OTP to the user's phone number using Twilio
        message = client.messages.create(
            body=f'Your OTP is: {otp}',
            from_=TWILIO_PHONE_NUMBER,
            to=self.phone_number_entry.get()
        )

        # Store the OTP for verification
        self.otp = otp
        return random 

    def verify_otp(self):
        # Get the user's input OTP
        user_otp = self.otp_entry.get()

        # Verify the OTP
        if user_otp == self.otp:
            messagebox.showinfo('Success', 'OTP verification successful!')
        else:
            messagebox.showerror('Error', 'Invalid OTP. Please try again.')

root = tk.Tk()
my_gui = OTPVerification(root)
root.mainloop()
