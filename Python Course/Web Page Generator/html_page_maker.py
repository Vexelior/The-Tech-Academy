#Creates the file 'main.html', will return error if the file already exists.
html_page = open("main.html", "x")
#Adds content to the file.
html_page.write("<html> <body> <h1> Stay tuned for our amazing summer sale! </h1> </body> </html>")
html_page.close()

#open and read the file after the appending:
html_page = open("main.html", "r")
print(html_page.read())
