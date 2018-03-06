/*
14.2 Open Requests
Write a sQL query to get a list of all buildings and the number of open
requests (Requests in which status equals 'Open').
*/

SELECT Buildings.BuildingName, isNull(OpenRequests, 0) as [OpenRequests]
FROM Buildings LEFT JOIN
(
  SELECT Apartment.BuildingID count(*) as [OpenRequests]
  FROM Requests INNER JOIN Apartments
  ON Requests.AptID = Apartments.AptID
  WHERE Status = 'Open'
  GROUPBY Apartment.BuildingID
) RequestCount
ON Buildings.BuildingID = RequestCount.BuildingID
GROUPBY Buildings.BuildingID
