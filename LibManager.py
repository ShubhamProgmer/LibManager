import time

#LibManeger By ShubhamProgmer

class Library:
	def __init__(self, listOfBooks, libraryName):
		self.listOfBooks = listOfBooks
		self.libraryName = libraryName
		self.lendPerson = {}
		for book in self.listOfBooks:
			self.lendPerson[book] = None
			
	def addBook(self, bookNameAdd):
		self.listOfBooks.append(bookNameAdd)
		print(f"\'{bookNameAdd}\' added to \'{self.libraryName}\'")
		
	def lendBook(self, bookNameLend, person):
		try:
			if self.lendPerson[bookNameLend] == None:
				self.lendPerson[bookNameLend] = person
				print(f"\'{bookNameLend}\' lend by \'{person}\'")
				self.listOfBooks.remove(bookNameLend)
			else:
				print(f"Sorry this book is lend by {self.lendPerson[bookNameLend]}")	
		except Exception as z:
			print("Sorry! wrong book name")
	
	def displayBook(self):
		i = 1
		for books in self.listOfBooks:
			print(f"{i}. {books}")
			i += 1
	
	def deleteBook(self, bookName):
		try:
			self.listOfBooks.remove(bookName)
			print(f"\'{bookName}\' deleted from \'{self.libraryName}\'")
		except Exception as e:
			print(f"Sorry no book named \'{bookName}\'")
			
	def returnBook(self, bookNameReturn):
		try:
			if self.lendPerson[bookNameReturn] != None:
				self.lendPerson[bookNameReturn] = None
				self.listOfBooks.append(bookNameReturn)
				print("Book returned!")
			else:
				print("Book is not lend yet by anyone!")
		except Exception as e:
			print("Sorry you entered wrong book name!")
			
					
									
ShubhamLib  = Library(["Java for professional by Anurarthi Gopal", "Python course for beigners by Navendra Rao Chakravarti", "Learn C++ in easiest way by Naval Kishor"], "ShubhamLib")


def main():
	print("Welcome to LibManager\nBy ShubhamProgmer - https://github.com/ShubhamProgmer\n\nWhat do you want to do?\n1. Display books\n2. Add Book\n3. Lend Book\n4. Return Book\n5. Delete Book\n6. Quit")
	while True:
		print()
		x = input("Enter your choice using serial number as option: ")
					
		if x == "1":
			ShubhamLib.displayBook()
			continue
		
		elif x == "2":
			bookNameAdd = input("Please enter the name of book to add: ")
			ShubhamLib.addBook(bookNameAdd)	
			continue
			
		elif x == "3":
			bookNameLend = input("Please Enter the name of book you want to lend: ")
			person = input("Please enter your name: ")
			ShubhamLib.lendBook(bookNameLend, person)
			continue
			
		elif x == "4":
			bookNameReturn = input("Please enter the name of book you want to return: ")
			ShubhamLib.returnBook(bookNameReturn)
			continue
			
		elif x == "5":
			secretCode = input("Please enter the password of Library management to delete book: ")
			if secretCode == "1212":
				bookName = input("Please enter the name of book to delete: ")
				ShubhamLib.deleteBook(bookName)			
			else:
				print("Wrong password!")
			continue
			
		elif x == "6":
			print()
			print("Thank You for using LibManager!")
			print("Exiting....")
			time.sleep(3)		
			exit()
			
		else:
			print("Please enter a valid option!")							
main()
				