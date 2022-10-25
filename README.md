# BMEP_algorithm
Implementation of BMEP (Bellman, Moore, d’Escopo, Papugo) algorithm used to solve shortest path problem. Program produces output as if it should look like when someone was solving problem on paper - in form of a table in which we can see every iteration and state after subsequent steps. As a result it especially useful for students preparing for exams.

# Requirements
* python 3
* tabulate 0.9.0 (or below)

`pip install -r rerquirements.txt`

# Usage

To run program all you have to do is supply script with appropriate formatted file - refer to /examples folder.
In output you will receive table with every iteration, answer containing shortest path length and how that path runs and also how long it took to find this solution.

```
  Iteration  Queue       a           b             c             d             e             f
-----------  ----------  ----------  ------------  ------------  ------------  ------------  ------------
          0  ['a']       [0, False]  [189, False]  [189, False]  [189, False]  [189, False]  [189, False]
          1  ['b', 'c']  [0, False]  [5, 'a']      [4, 'a']      [189, False]  [189, False]  [189, False]
          2  ['c', 'd']  [0, False]  [5, 'a']      [2, 'b']      [12, 'b']     [189, False]  [189, False]
          3  ['d', 'e']  [0, False]  [5, 'a']      [2, 'b']      [12, 'b']     [7, 'c']      [189, False]
          4  ['e', 'f']  [0, False]  [5, 'a']      [2, 'b']      [12, 'b']     [7, 'c']      [17, 'd']
          5  ['d', 'f']  [0, False]  [5, 'a']      [2, 'b']      [9, 'e']      [7, 'c']      [13, 'e']
          6  ['f']       [0, False]  [5, 'a']      [2, 'b']      [9, 'e']      [7, 'c']      [13, 'e']
          7  []          [0, False]  [5, 'a']      [2, 'b']      [9, 'e']      [7, 'c']      [13, 'e']

Answer:
	Track length: 13
	Order: a -> b -> c -> e -> f

Computed in: 0.000907s.
```

# To do

**Large code refactor!!!**
