# Sample text
text = """
John Doe (john.doe@example.com) purchased 3 items for a total of $29.99 on 2024-10-14. 
His phone number is (555) 123-4567. He also has 100 reward points. The office address is 200 Park Avenue, Suite 300, New York, NY 10166. 
His order number is 456789123. He transferred $1,500 to his bank account.
"""

# Basic function to find email-like patterns (just a demo without regex)
def find_emails(text):
    results = []
    words = text.split()
    for word in words:
        if "@" in word and "." in word:
            results.append(word.strip(",."))
    return results

# Basic function to find numbers (won't handle complex cases)
def find_numbers(text):
    results = []
    words = text.split()
    for word in words:
        if word.replace(",", "").replace(".", "").isdigit():
            results.append(word.strip(",."))
    return results

# Example of usage
emails = find_emails(text)
numbers = find_numbers(text)

print("Emails found:", emails)
print("Numbers found:", numbers)