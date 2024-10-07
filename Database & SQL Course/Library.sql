CREATE DATABASE LibraryManagementSystem
 
USE LibraryManagementSystem
 
CREATE TABLE LIBRARY_BRANCH (
BranchID INT PRIMARY KEY NOT NULL IDENTITY (1,1),
BranchName VARCHAR(255) NOT NULL,
Address VARCHAR(255) NOT NULL
);
 
CREATE TABLE BORROWER (
CardNo INT PRIMARY KEY NOT NULL IDENTITY (1,1),
Name VARCHAR(255) NOT NULL,
Address VARCHAR(255) NOT NULL,
Phone VARCHAR(20) NOT NULL
);
 
CREATE TABLE PUBLISHER (
PublisherName VARCHAR(255) PRIMARY KEY NOT NULL,
Address VARCHAR(255) NOT NULL,
Phone VARCHAR(20) NOT NULL
);
 
CREATE TABLE BOOKS (
BookID INT PRIMARY KEY NOT NULL IDENTITY (1,1),
Title VARCHAR(255) NOT NULL,
PublisherName VARCHAR(255) NOT NULL
);
 
CREATE TABLE BOOK_AUTHORS (
BookID INT FOREIGN KEY REFERENCES BOOKS(Bookid),
AuthorName VARCHAR(255) NOT NULL
);
 
CREATE TABLE BOOK_COPIES (
BookID INT FOREIGN KEY REFERENCES BOOKS(Bookid) NOT NULL,
BranchID INT FOREIGN KEY REFERENCES LIBRARY_BRANCH(BranchID) NOT NULL,
Number_Of_Copies INT NOT NULL
);
 
CREATE TABLE BOOK_LOANS (
BookID INT FOREIGN KEY REFERENCES BOOKS(Bookid) NOT NULL,
BranchID INT FOREIGN KEY REFERENCES LIBRARY_BRANCH(BranchID) NOT NULL,
CardNo INT FOREIGN KEY REFERENCES BORROWER(CardNo) NOT NULL,
DateOut DATE NOT NULL,
DateDue DATE NOT NULL
);
 
INSERT INTO LIBRARY_BRANCH
(BranchName, Address)
VALUES
('Sharpstown', '7543 53rd Court'),
('UrbanRead', '7633 Holly Street'),
('NorthBay', '2 8th Court'),
('Merilyn', '128 South Magnolia Lane'),
('Virgon', '7067 Marvon Ave.'),
('BlueStone', '30 South Maiden Dr.')
;
 
SELECT * FROM LIBRARY_BRANCH
 
INSERT INTO BORROWER
(Name, Address, Phone)
VALUES
('Michael Naidu', '88272 Susan Gateway Suite 656', '446-726-6436'),
('Patricia King', '185 Marcus Rapids', '349-614-2826'),
('Matthew Martin', '7566 Roberts Road Suite 27', '615-148-3189'),
('Simone Williams', '87648 Jose Parkway', '639-120-5939'),
('Ricky Kwon', '42393 Mills Branch Apt. 716', '562-740-8815'),
('Fred Schuler', '939 Ferguson Heights', '344-314-0568'),
('Martha Sargent', '5955 Graves Camp', '690-807-0018'),
('Steffen HelmSchrott', '328 Zimmerman Harbor Apt. 885', '153-646-7082')
;
SELECT * FROM BORROWER
 
INSERT INTO PUBLISHER
(PublisherName, Address, Phone)
VALUES
('Pearson', 'Longon, England, UK', '621-522-6278'),
('RELX', 'London, England, UK', '253-586-4631'),
('Thomson Reuters', 'Toronto, Ontario, Canada', '397-614-3092'),
('Penguin Random House', 'New York City, USA', '757-948-4913'),
('Hachette Livre', 'Paris, France', '292-483-1100'),
('HarperCollins', 'New York, USA', '887-812-5803'),
('Macmillan Publishers', 'New York City, USA', '950-221-1061'),
('Bertelsmann', 'Gutersloh, Germany', '731-119-6048'),
('Scholastic Corporation', 'New York, USA', '974-691-1462'),
('McGraw-Hill Education', 'New York, USA', '393-668-6978')
;
SELECT * FROM PUBLISHER
 
INSERT INTO BOOKS
(Title, PublisherName)
VALUES
('The Lost Tribe', 'HarperCollins'),
('Pride and Prejudice', 'HarperCollins'),
('To Kill A Mockingbird', 'Bertelsmann'),
('The Great Gatsby', 'Bertelsmann'),
('One Hundred Years of Solitude', 'Hachette Livre'),
('In Cold Blood', 'Hachette Livre'),
('Wide Sargasso Sea', 'Macmillan Publishers'),
('Brave New World', 'Macmillan Publishers'),
('I Capture The Castle', 'McGraw-Hill Education'),
('Jane Eyre', 'McGraw-Hill Education'),
('Crime and Punishment', 'Pearson'),
('The Secret History', 'Pearson'),
('The Call of the Wild', 'Penguin Random House'),
('The Chrysalids', 'Penguin Random House'),
('Persuasion', 'RELX'),
('Moby-Dick', 'RELX'),
('The Lion, The Witch and the Wardrobe', 'Scholastic Corporation'),
('To the Lighthouse', 'Scholastic Corporation'),
('The Death of the Heart', 'Thomson Reuters'),
('Frankenstein', 'Thomson Reuters')
;
SELECT * FROM BOOKS
 
INSERT INTO BOOK_AUTHORS
(BookID, AuthorName)
VALUES
(1, 'Jane Austen'),
(20, 'Jane Austen'),
(2, 'Harper Lee'),
(19, 'Harper Lee'),
(3, 'F. Scott Fitzgerald'),
(18, 'F. Scott Fitzgerald'),
(4, 'Gabriel Garcia Marquez'),
(17, 'Gabrial Garcia Marquez'),
(5, 'Truman Capote'),
(16, 'Truman Capote'),
(6, 'Jean Rhys'),
(15, 'Jean Rhys'),
(7, 'Aldous Huxley'),
(14, 'Aldous Huxley'),
(8, 'Dodie Smith'),
(13, 'Dodie Smith'),
(9, 'Charlotte Bronte'),
(12, 'Charlotte Bronte'),
(10, 'Fyodor Dostoevksy'),
(11, 'Fyodor Dostoevksy')
;
 
 
INSERT INTO BOOK_COPIES
(Number_Of_Copies, BookID, BranchID)
VALUES
(2, 1, 6),
(4, 2, 6),
(3, 3, 5),
(2, 4, 5),
(4, 5, 4),
(3, 6, 4),
(2, 7, 3),
(2, 8, 3),
(3, 9, 2),
(4, 10, 2),
(2, 11, 1),
(3, 12, 1),
(4, 13, 1),
(3, 14, 2),
(4, 15, 3),
(2, 16, 4),
(3, 17, 5),
(2, 18, 6),
(3, 19, 4),
(4, 20, 2)
;
 
INSERT INTO BOOK_LOANS
(BookID, BranchID, CardNo, DateOut, DateDue)
VALUES
(1, 6, 1, '20220501', '20220522'),
(2, 6, 1, '20220502', '20220513'),
(13, 1, 2, '20220425', '20220511'),
(4, 5, 7, '20220501', '20220512'),
(15, 3, 3, '20220429', '20220505'),
(6, 4, 4, '20220430', '20220504'),
(17, 5, 7, '20220503', '20220511'),
(8, 3, 3, '20220501', '20220513'),
(19, 4, 5, '20220428', '20220504'),
(7, 3, 5, '20220429', '20220506')
;
