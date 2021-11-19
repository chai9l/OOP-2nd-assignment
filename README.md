
![Logo](https://dcassetcdn.com/design_img/838187/464630/464630_4966391_838187_image.jpg)



**This project revolves around the implementation of the offline algorithm
for the elevator problem shown in the first part of the assignment.**




## Related

Here are some related projects

[1st project -](https://www.hellocodeclub.com/design-elevator-system-java/)
[2nd project -](https://thinksoftware.medium.com/elevator-system-design-a-tricky-technical-interview-question-116f396f2b1c)
[3rd project](https://medium.com/geekculture/system-design-elevator-system-design-interview-question-6e8d03ce1b44)



## Classes and methods

### Flowchart
![Logo](https://cdn.discordapp.com/attachments/248128879733112833/911369124159049748/MyChart.png)

### Classes
| ***Class*** | ***Description***                |
| :-------- | :------------------------- |
| `myBuildling` | *This class represents a buildling from a given **json** file* |
| `myCall` | *This class represents a call from a given **csv** file* |
| `myelevator` | *This class represent an elevator from a given **building*** |
| `ElevatorAlgo` | *This class represents the algorhythm for the allocation of a call to an elevator* |

### Methods for ElevatorAlgo

| ***Method*** | ***Description***                       |
| :-------- | :-------------------------------- |
| `load_buildings` | *This method loads a buildling from a given **json** file* |
| `load_calls` | *This method loads calls from a given **csv** file* |
| `write_output` | *Writes the id's of the allocated elevators into a new **json** file named Out_put* |
| `allocate_elevator` | *Allocates a call to an elevator using allocation algorhythm* |
| `calc_time_between_floors` | *Calculates the time it takes to reach from floor 'a' to floor 'b' for a specific elevator* |

### Methods for myElevator

| ***Method*** | ***Description***                       |
| :-------- | :-------------------------------- |
| `is_inrange` | *Checks if the elevator's position is in between two given arguments* | 
| `calc_time_all_calls` | *Calculates the time it takes for a specific elevator to finish it's call list* |

## Algorhithm

### Allocation
* We'll start by loading the calls and building from the given files using the load function
* Go through all recieved calls
* For each call go through all recieved elevators
* For each elevator calculate:
    * **calculate** the time it'll take for the elevator to finish it's entire path in addition to the new call
    * save the recieved time
    * save the minimum time and it's elevator's id
* Allocate the new recieved call into the chosen elevator's call list aka path

### Time calculation
* Simulating the elevator's entire path, meaning go through each of the elevator's calls.  
* Creating a new call list for the elevator with the addition of the new call.
* Mark each of the elevator's calls with flags saying if the call is done, going to src and going to dest.
* Each call that is done we'll be removed from the new simulated list.
* Mark each elevator's states with the following flags: UP, DOWN, LEVEL
* Check the elevator's state:
    * LEVEL = The elevator we'll go either UP or DOWN (decided by call's direction)
    * UP, DOWN = The Elevator's we'll move accordingly to the speed it has, and to the direction mentioned.
**In every step we'll add time and check how longs it takes in the end of the calculation**




## Installation
Download this repository's zip-file
| ***Name*** | ***Meaning***                |
| :-------- | :------------------------- |
| **Path** | *represents the path for the folder in which the files are at.*|
| **id1,id2** | *represents id* |
| **Bx** | *represents one of the building json files, x represents which file* |
| **Calls_x** | *represents one of the call csv files, x represents which file* |



```bash
  cd Path
  python ElevatorAlgo.py 313589038,205569890 Ex1_Buildings\B.json Ex1_Calls/Calls_.csv Ex1_Calls/out_put_a.csv
  Overall: python ElevatorAlgo.py id1,id2 building.json calls.csv output.csv
```
    
## Authors

- [@chai](https://github.com/chai9l)
- [@netanel](https://github.com/Netanel94)

