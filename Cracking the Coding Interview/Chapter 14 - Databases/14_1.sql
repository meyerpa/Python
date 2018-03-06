/*
14.1 Multiple Apartments
Write a SQL query to get a list of tenants who are renting more than one
apartment
*/

SELECT TenantName
FROM (
  SELECT TenantID, count(AptTenants.AptID) as [NumApts]
  FROM AptTenants
  GROUP BY TenantID
) T INNER JOIN Tenants
ON Tenants.TenantID = T.TenantID
WHERE T.NumApts > 1
