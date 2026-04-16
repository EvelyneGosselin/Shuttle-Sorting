# Shuttle-Sorting

## Chosen problem
The chosen problem is the shuttle crowd ranking, which hekps coordinates the decision of where to send extra shuttles. Considering the crowd at each of them, the problem is in ranking the stops from the most to least crowded.

## Chosen algorithm
The chosen algorithm is Merge Sort. This problem is adapted to it because it is adapted for any size of lists of integers, compare to quicksort which can get to a higher complexity and isn't worth it in the context of a shorter list of crowd_count. It is also good since merge sort is stable so the changing ranking can keep the order of equal crowd_count the same as the previous ones.

## Demo
! [App Demo](18.30.49.gif)

## Problem Breakdown & Computational Thinking
- Decomposition: Merge sorts algorithms can be separated in spliting the list, in this context list of stop, in half. Then, each half is sorted by splitting them continuously until each element is individual and comparing the elements to put the higher crowd_count first. Then, the two halves are merged by comparing each element and putting them in the final ranked list.
- Pattern recognition: The main pattern is continuously splitting the sublist, first in the two main list and then repeatedly to compare the items. Each individual comparison is looking for the larger crowd_count.
- Abstraction choices: The user of the algrotithm doesn't need to see the whole recursive process of the merge sort profoundly. The temporary sublist also aren't relevant to the decision making. What needs to be shown is some narration to explain the results and the changing sorted list. 
- Algorithm-design flow: The input is a list of dictionaries that indicate the name of the stop and the crowd_count. The process to get there is the merge sort, and the main steps are shown on the GUI. The output is every step on the interface and finally the sorted list of the stops names in term of crowd_count.

## Steps to Run and requirements.txt
Requirements.txt -> gradio
Steps to run:
    1. Install the dependencies, through requirements.txt which installs gradio
    2. Run the app on a Python 
    
## Testings
<img width="740" height="350" alt="Capture d’écran, le 2026-04-15 à 18 39 52" src="https://github.com/user-attachments/assets/ae2f673b-3ae7-4db0-884e-d8b111715f1c" />

## Hugging Face Link
https://huggingface.co/spaces/Evelyne06/Shuttle-Sorting

## Author & AI Acknowledgment
- Author : Evelyne Gosselin
- Class : CISC121
- AI Use : Claude was used 
