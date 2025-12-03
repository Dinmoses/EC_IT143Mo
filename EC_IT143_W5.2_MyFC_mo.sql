/*
EC_IT143_W5.2_MyFC_mo.sql
Author: Moses Okello
Date: 2025-11-27
Assignment 5.2 – My Communities Analysis: Create Answers
Community: MyFC
*/

-- Question 1 (Author: Moses Okello)
-- How many members are in the MyFC community?
SELECT COUNT(*) AS TotalMembers
FROM Members;

-- Question 2 (Author: Another Student)
-- What is the average age of members in MyFC?
SELECT AVG(Age) AS AverageAge
FROM Members;

-- Question 3 (Author: Moses Okello)
-- Which city has the highest number of members?
SELECT City, COUNT(*) AS MemberCount
FROM Members
GROUP BY City
ORDER BY MemberCount DESC;

-- Question 4 (Author: Another Student)
-- How many members joined in 2025?
SELECT COUNT(*) AS MembersJoined2025
FROM Members
WHERE YEAR(JoinDate) = 2025;