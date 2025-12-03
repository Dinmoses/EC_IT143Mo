/*
EC_IT143_W5.2_Simpsons_mo.sql
Author: Moses Okello
Date: 2025-11-27
Assignment 5.2 – My Communities Analysis: Create Answers
Community: Simpsons
*/

-- Question 1 (Author: Moses Okello)
-- How many episodes are in the Simpsons dataset?
SELECT COUNT(*) AS TotalEpisodes
FROM Episodes;

-- Question 2 (Author: Another Student)
-- What is the average rating of episodes?
SELECT AVG(Rating) AS AverageRating
FROM Episodes;

-- Question 3 (Author: Moses Okello)
-- Which season has the most episodes?
SELECT Season, COUNT(*) AS EpisodeCount
FROM Episodes
GROUP BY Season
ORDER BY EpisodeCount DESC;

-- Question 4 (Author: Another Student)
-- How many episodes aired in 2020?
SELECT COUNT(*) AS Episodes2020
FROM Episodes
WHERE YEAR(AirDate) = 2020;