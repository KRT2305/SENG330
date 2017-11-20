
# Marking Guide    22 / 30


## Structural design 7/10
- add labels to your associations, so it is clear what dependency you are creating.
- would like to see some indication of where Spring fits in with the system. What is it doing?
- is getSchedule really a part of Vehicle? Or do you ask the Schedule object for a particular Vehicle?
- a lot of objects use a Schedule. Does that mean Schedule is complex and should be refactored? What exactly is a Schedule object?

## Runtime design 2/5
- Are you really using two servers? 
- Add some aspects from the Spring architecture to your diagram. Pretend you want to onboard a new teammate and you need to hand her this diagram. How would she know what to do?
- It leaves a little to be desired as a helpful view on the system. It is so generic it could describe many different apps.


## Allocation views 5/5
- Delineates the mapping to requirements; each use case is captured by a design element.

## Rationale  8/10
- "authentication token" is not really part of the domain language. Most business types won't care about this.
- would be helpful to your team if more discussion was spent on how Spring worked in your app

## Comments
