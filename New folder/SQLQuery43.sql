SELECT ContactName,
       dbo.fn_GetFirstName(ContactName) AS FirstName,
       dbo.fn_GetLastName(ContactName) AS LastName
FROM dbo.t_w3_schools_customers;