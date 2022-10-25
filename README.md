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
  Iteration  Queue            a           b             c             d             e             f
-----------  ---------------  ----------  ------------  ------------  ------------  ------------  ------------
          0  ['a']            [0, False]  [249, False]  [249, False]  [249, False]  [249, False]  [249, False]
          1  ['b', 'c']       [0, False]  [5, 'a']      [6, 'a']      [249, False]  [249, False]  [249, False]
          2  ['c', 'd', 'e']  [0, False]  [5, 'a']      [6, 'a']      [10, 'b']     [10, 'b']     [249, False]
          3  ['d', 'e']       [0, False]  [5, 'a']      [6, 'a']      [10, 'b']     [10, 'b']     [249, False]
          4  ['e', 'f']       [0, False]  [5, 'a']      [6, 'a']      [10, 'b']     [10, 'b']     [15, 'd']
          5  ['f', 'c']       [0, False]  [5, 'a']      [4, 'e']      [10, 'b']     [10, 'b']     [15, 'd']
          6  ['c']            [0, False]  [5, 'a']      [4, 'e']      [10, 'b']     [10, 'b']     [15, 'd']
          7  ['d']            [0, False]  [5, 'a']      [4, 'e']      [8, 'c']      [10, 'b']     [15, 'd']
          8  ['f']            [0, False]  [5, 'a']      [4, 'e']      [8, 'c']      [10, 'b']     [13, 'd']
          9  []               [0, False]  [5, 'a']      [4, 'e']      [8, 'c']      [10, 'b']     [13, 'd']

Answer:
	Track length: 13
	Order: a -> b -> e -> c -> d -> f

Computed in: 0.000995s.
```

# To do

**Large code refactor!!!**
