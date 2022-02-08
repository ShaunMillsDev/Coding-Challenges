## Some fun coding challenges I have worked on


### Calendars
Source: https://youtu.be/3Q_oYDQ2whs

**The Challenge:** Given two people's calendars, daily bounds, and a meeting duration, return free slots of time during which these two people could have a meeting. The daily bounds specify the time they start their day and the time they end their day. They are not available outside these bounds.

Example:
  
```
Input:
        Person 1 calendar: [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
        Person 1 bounds:   ['9:00', '20:00']
       
        Person 2 calendar: [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
        Person 2 bounds:   ['10:00', '18:30']
        
        Meeting duration: 30
```
```       
Output: 
        [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
```
