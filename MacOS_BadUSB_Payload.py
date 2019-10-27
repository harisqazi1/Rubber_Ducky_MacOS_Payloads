#!/bin/python3

logo = """

   ___  _      _                   __     ___          ____  _________    ___            __             __  _____                      __          
  / _ \(_)__ _(_)__ ___  ___ _____/ /__  / _ )___ ____/ / / / / __/ _ )  / _ \___ ___ __/ /__  ___ ____/ / / ___/__ ___  ___ _______ _/ /____  ____
 / // / / _ `/ (_-</ _ \/ _ `/ __/  '_/ / _  / _ `/ _  / /_/ /\ \/ _  | / ___/ _ `/ // / / _ \/ _ `/ _  / / (_ / -_) _ \/ -_) __/ _ `/ __/ _ \/ __/
/____/_/\_, /_/___/ .__/\_,_/_/ /_/\_\ /____/\_,_/\_,_/\____/___/____/ /_/   \_,_/\_, /_/\___/\_,_/\_,_/  \___/\__/_//_/\__/_/  \_,_/\__/\___/_/   
       /___/     /_/                                                             /___/                                                             

       
"""
print(logo)

print("""Payload Options

	[1] WEBSITE: a payload which opens a webpage on a browser


	""")


def website_payload(website):
	payload1 = """

#include "DigiKeyboard.h"

boolean didRun = false;

void setup() {}

void loop() {
  while (didRun == false) {
    DigiKeyboard.sendKeyStroke(KEY_SPACE, MOD_GUI_LEFT);
    DigiKeyboard.delay(300);
    DigiKeyboard.println("terminal");
    DigiKeyboard.delay(300);
    DigiKeyboard.println("open https://github.com/harisqazi1");
    didRun = true;
  }
}
	"""
	payload1_replace = payload1.replace("https://github.com/harisqazi1", website)
	print("-" * 20 + "Copy Below" + "-" * 20)
	print(payload1_replace)
	print(payload1_replace, file=open("Website_Payload.ino", "a")) #outputs the file as a Arduino file
	return


Payload_Selection = int(input("Choose a Payload: "))

if Payload_Selection != 1:
	print("Choose a valid value for a Payload!")

if Payload_Selection == 1:
	website = input("Enter a website for Payload: ")
	website_payload(website)
	




