# Testing
*Note: may want to discuss testing tools available?*

## What the interviewer is looking for
+ *Big Picture Understanding* - prioritizing test cases
+ *Knowing How the Pieces Fit Together* - what does the software interact with
+ *Organization* - approach the problem in a structured manner instead of spouting anything off
+ *Practicality* - create reasonable testing plans

## Testing a Real World Object
### STEPS
1. Who will use it and why?
2. What are the use cases?
3. What are the bounds of use?
4. What are the stress/failure conditions?
5. How would you perform the testing?

## Testing a Piece of Software (more emphasis on details of performance)
### Two Core aspects
+ *Manual vs. Automated Testing*
+ *Black Box Testing vs. White Box Testing*

### STEPS
1. Are we doing Black Box Testing or White Box Testing?
2. Who will use it and why?
3. What are the use cases?
4. What are the bounds of use?
5. What are the stress conditions/failure conditions?
6. What are the test cases? How would you perform the testing? (NOTE: be structured here)

## Testing a Function (typically limited to validating input & output)
### STEPS
1. Define the test cases
  + Normal Case
  + Extremes (e.g. empty)
  + Nulls and "illegal" input (e.g. Fibonacci with negative n)
  + Strange input (e.g. pre-sorted array)
2. Define the expected result (and inputs haven't changed)
3. Write the code

## Troubleshooting Questions
### STEPS
1. Understand the Scenario
  + How long has the user been experiencing this issue?
  + What version of the software is it?
  + Which Operating System?
  + Does the issue happen consistently, or how often does it happen? When does it happen?
  + Is there an error that is reported?
2. Break Down the Problem (imagine flow (steps) of situation and test each of these elements in order)
3. Create Specific, Manageable Tests (ask user to do certain replication steps)
