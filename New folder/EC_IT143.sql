CREATE TRIGGER trg_UpdateLastModifiedDate
ON dbo.t_w3_schools_customers
AFTER UPDATE
AS
BEGIN
    UPDATE dbo.t_w3_schools_customers
    SET LastModifiedDate = GETDATE()
    FROM Inserted i
    WHERE dbo.t_w3_schools_customers.CustomerID = i.CustomerID;
END;