/*Assignment 1:*/
SELECT * FROM tbl_habitat;

/*Assignment 2:*/
SELECT species_name FROM tbl_species WHERE species_order = 3;

/*Assignment 3:*/
SELECT nutrition_type FROM tbl_nutrition WHERE nutrition_cost <= 600;

/*Assignment 4:*/
SELECT species_name
FROM tbl_nutrition
INNER JOIN tbl_species ON tbl_species.species_nutrition = tbl_nutrition.nutrition_id
WHERE species_nutrition BETWEEN 2202 AND 2206;

SELECT species_name 
FROM tbl_species 
WHERE species_nutrition > 2202 AND species_nutrition < 2206
/*or*/
SELECT species_name FROM tbl_species 
WHERE species_nutrition BETWEEN 2203 AND 2205;
/*The following returns the right data but is not correct:*/

/*Assignment 5:*/
SELECT tbl_species.species_name AS 'Species Name',    tbl_nutrition.nutrition_type AS 'Nutrition Type' 
FROM tbl_species
INNER JOIN tbl_nutrition ON tbl_nutrition.nutrition_id = tbl_species.species_nutrition
/*Or something like*/
SELECT a1.species_name AS 'Species Name', a2.nutrition_type AS 'Nutrition Type'
FROM tbl_species a1
INNER JOIN tbl_nutrition a2 ON a2.nutrition_id = a1.species_nutrition

/*Assignment 6:*/
SELECT specialist_fname AS 'First Name', 
	  specialist_lname AS 'Last Name', 
	  specialist_contact AS 'Contact'
	FROM tbl_specialist
	INNER JOIN tbl_care ON tbl_care.care_specialist = tbl_specialist.specialist_id
	INNER JOIN tbl_species ON tbl_species.species_care = tbl_care.care_id
		WHERE species_name = 'penguin';

/*Assignment 7 - (Example):*/
CREATE DATABASE db_Movies

USE db_Movies

CREATE TABLE tbl_directors (
	director_id INT NOT NULL PRIMARY KEY IDENTITY (1,1),
	director_name VARCHAR(50),
	director_movie VARCHAR(30)
)

CREATE TABLE tbl_actors (
	actor_id INT NOT NULL PRIMARY KEY IDENTITY (1, 1),
	actor_name VARCHAR(50),
	actor_movie VARCHAR(30),
	actor_fk INT CONSTRAINT fk_actor FOREIGN KEY REFERENCES tbl_directors(director_id)
)

INSERT INTO tbl_directors
(director_name, director_movie)
VALUES
('Quentin Tarantino', 'Kill Bill: Volume 1'),
('Damien Chazelle', 'J.K. Simmons'),
('Peter Jackson', 'The Lord of the Rings'),
('Bong Joon Ho', 'Parasite'),
('Sam Mendes', '1917')

INSERT INTO tbl_actors
(actor_name, actor_movie, actor_fk)
VALUES
('Uma Thurman', 'Kill Bill: Volume 1', 1),
('David Carradine', 'Kill Bill: Volume 1', 1),
('John Travolta', 'Pulp Fiction', 1),
('Samuel L. Jackson', 'Pulp Fiction', 1),
('Leonardo DiCaprio', 'J.K. Simmons', 2),
('J.K. Simmons', 'J.K. Simmons', 2),
('Elijah Wood', 'The Lord of the Rings', 3),
('Viggo Mortensen', 'The Lord of the Rings', 3),
('Ian McKellen', 'The Lord of the Rings', 3),
('Song Kang-ho', 'Parasite', 4),
('Lee Sun-kyun', 'Parasite', 4),
('Cho Yeo-jeong', 'Parasite', 4),
('George MacKay', '1917', 5),
('Dean-Charles Chapman', '1917', 5),
('Daniel Mays', '1917', 5)

SELECT
    director_name,
    actor_name,
    actor_movie
FROM
    tbl_directors
INNER JOIN
    tbl_actors
ON
    tbl_directors.director_id = tbl_actors.actor_fk
