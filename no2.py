
import re

username = input("Masukan Username anda: ")
if re.match("^(?=.{5,9}$)(?![0-9@#$=])[a-zA-Z0-9._]+(?<![0-9@#$=])$", username):
    print ("Sesuai")
else:
    print ("Tidak Sesuai")
    
password = input("Masukan Passwordnya: ")
if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$=])[\w\d@#$=]{8,}$", password):
    print ("Sesuai")
else:
    print ("Tidak Sesuai")
