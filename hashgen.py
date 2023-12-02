#this project was done by Anyalogbu Ernest Chinualum Henry Jnr.
#importing the hash library
import hashlib
#taking the string to be hashed
word = input("Enter string:  ")
#making room for the user to select hash type
print("select one of the following hash types")
#prints the available hash types
print("1	 ==>> 	md5")
print("2	 ==>>	 sha1")
print("3	 ==>>	 sha256")
#taking the type of hash selected/needed
hash_type = input("Enter the hash type:   ")
#encoding the string 
enc_wrd = word.encode('utf-8')
#using if else statement to check the hash type
#checking if hash type is md5
if hash_type == "1":
#creating and digesting the md5 hash code
	digest = hashlib.md5 (enc_wrd.strip()).hexdigest()
#checking if hash type is sha1
elif hash_type == "2":
#creating and digesting the sha1 hash code
	digest = hashlib.sha1 (enc_wrd.strip()).hexdigest()
#checking if hash type is sha256
elif hash_type == "3":
#creating and digesting the sha256 hash code
	digest = hashlib.sha256 (enc_wrd.strip()).hexdigest()
#this get printed if the hash type can be resolved
else:
	print("\n\n\nyour hash can't be generated ")
	print("try new string and hash type")
#using if statement to check hash type selected for printing the hashes
if hash_type =="1" or hash_type == "2" or hash_type == "3":
	#prints the first broder design
	print("*" * 67)
	#prints out the string 
	print(word)
	#prints out the digest
	print(" ==> " + digest)
	#calculate the length of the hash
	hashCounter = str(len(digest))
	#prints the hash length
	print("The hash has " + hashCounter + " characters")
	#prints the last broder design
	print("*" * 67)