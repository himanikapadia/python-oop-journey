from abc import ABC, abstractmethod

# Abstract Class
class DocumentConverter(ABC):

    @abstractmethod
    def convert(self, filename):
        pass

    @abstractmethod
    def showFormat(self, filename):
        pass


# Child Class 1
class PDFConverter(DocumentConverter):

    def convert(self, filename):
        print("Converting document to PDF...")

    def showFormat(self,filename):
        print(f"Output File : {filename}.pdf")


# Child Class 2
class WordConverter(DocumentConverter):

    def convert(self, filename):
        print("Converting document to Docx...")

    def showFormat(self,filename):
            print(f"Output File : {filename}.docx")


# Child Class 3
class HTMLConverter(DocumentConverter):

    def convert(self, filename):
        print("Converting document to HTML...")

    def showFormat(self,filename):
            print(f"Output File : {filename}.html")


# Driver Code
filename = input("Enter document name: ")

print("\n======= Enter Format to convert =======")
print("1. PDF")
print("2. Word")
print("3. HTML")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    converter = PDFConverter()

elif choice == 2:
    converter = WordConverter()

elif choice == 3:
    converter = HTMLConverter()

else:
    print("Invalid Choice")
    exit()

converter.convert(filename)
converter.showFormat(filename)