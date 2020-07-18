#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) - the amount of times the while loop runs is dependant on the size of n

b) O(n log(n)) - Because it's running a for loop initially for the len(n) and a while loop within, but the while loop isn't dependant on the length of n, its dependant on j being less than n, and everytime the while loop runs j is multiplied by 2, significantly decreasing the amount of times the while loop runs.

c) O(n) - Because the amount of time the function is called recursively is dependant on the size of n.

## Exercise II

So if I understand this question correctly, I'm assuming that I have to start on the bottom "level" of the n value and go until I hit the f-level of the building and that is when my eggs start to break. So in order to see if I can get the highest amount of dropped eggs I would make a for loop and keeping count of the eggs that are not on f-level and stopping once I hit the f-level. So my minimized outcome would be j eggs dropped compared to 1 egg broken. The time complexity of this solution is O(n).
Upon revising my strategy I know that the stories or levels of the building have to be going from lowest to highest. So we could actually use binary search to find the f-level before we actually even have to throw off an egg. So we could have j number of dropped eggs compared to 0 number of broken eggs with a time complexity of O(logn). In the first solution we could also stop the loop on len(f) - 1 to have no broken eggs too but again I'm just hoping I understand the question correctly lol.
