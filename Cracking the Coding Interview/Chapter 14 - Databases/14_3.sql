/*
14.3 Close All Requests
Building #11 is undergoing a major renovation. Implement a query to close all
requests from apartments in this building.
*/

UPDATE Requests
Status = 'Closed'
WHERE AptID in (
  SELECT ApartmentID
  FROM Apartments
  WHERE BuildingID = 11
)
