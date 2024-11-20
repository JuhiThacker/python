import re
text = """
John Doe (john.doe@example.com) purchased 3 items for a total of $29.99 on 2024-10-14. 
His phone number is (555) 123-4567. He also has 100 reward points. The office address is 200 Park Avenue, Suite 300, New York, NY 10166. 
His order number is 4567891230. He transferred $1,500 to his bank account.
"""

regx=r'\w@\w+'
email=re.findall(regx,text.lower())
print(email)
regx=r'\w+@\w+'
email=re.findall(regx,text.lower())
print(email)
regx = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email=re.findall(regx,text.lower())
print(email)