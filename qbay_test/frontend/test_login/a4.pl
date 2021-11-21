% CISC 360 a4, Fall 2021
%
% See a4.pdf for instructions

/*
 * Q1: Student ID
 */
student_id( this is a syntax error ).
% other_student_id(  ).
% if in a group, uncomment the above line and put the other student ID between the ( )

/*
 * Q2: Prime numbers
 */
 
/*
  hasFactor(N, F): Given positive integers N and F,
                   true iff  there exists F' in {F' | (F' >= F) and (F' * F') < N}
                             such that (N mod F) = 0.
*/
hasFactor(N, F) :- N mod F =:= 0.
hasFactor(N, F) :- N mod F =\= 0,
                   F * F < N,
                   Fplus1 is F + 1,
                   hasFactor(N, Fplus1).
/*
  isPrime(N, What)

  Given an integer N >= 2:
    What = pr      iff  N is prime
    What = co      iff  N is composite
*/

isPrime(2, pr).
isPrime(N, co) :- N > 2,    hasFactor(N, 2).
isPrime(N, pr) :- N > 2, \+ hasFactor(N, 2).
%                        ^^
%                        "not"

/*
  findPrimes(Numbers, Primes)
    Primes = all prime numbers in Numbers
 
  Q2a. Replace the word "change_this" in the rules below.
       Hint:  Try to use  findPrimes(Xs, Ys).
*/
findPrimes([], []).

% In this rule, we include X in the output: [X | Ys].
% So this rule should check that X is prime.
findPrimes([X | Xs], [X | Ys]) :-
  change_this.

% In this rule, we do not include X in the output.
% So this rule should check that X is composite.
findPrimes([X | Xs], Ys) :-
  change_this.

/*
  upto(X, Y, Zs):
  Zs is every integer from X to Y

  Example:
     ?- upto(3, 7, Range)
     Range = [3, 4, 5, 6, 7]
*/
upto(X, X, [X]).
upto(X, Y, [X | Zs]) :-
    X < Y,
    Xplus1 is X + 1,
    upto(Xplus1, Y, Zs).

/*
  primes_range(M, N, Primes)
    Primes = all prime numbers between M and N
    Example:
      ?- primes_range(60, 80, Primes).
      Primes = [61, 67, 71, 73, 79] .

 Q2b. Replace the word "change_this" in the rule below.
      HINT: Use upto and findPrimes.
*/

primes_range(M, N, Primes) :-
   change_this.


/*
 * Q3. Translate the spiral function (similar to a1).
 *

  Write a function `spiral' that, given a pair of numbers `span' and `dir',
  returns 1 if `span' equals 0,
  and otherwise returns (span * dir) * spiral (span - 1, 0 - dir).

  Here is a Haskell solution:
  
  spiral :: (Integer, Integer) -> Integer
  spiral (span, dir) = if span == 0 then 1
                       else (span * dir) * spiral (span - 1, 0 - dir)

  I rewrote this to look more like the Prolog code you need to write:

  spiral :: (Integer, Integer) -> Integer
  spiral (span, dir)
      | span == 0 = 1
      | otherwise = r
                    where
                      product = span * dir
                      spanMinus1 = span - 1
                      zeroMinusDir = 0 - dir
                      spiralresult = spiral (spanMinus1, zeroMinusDir)
                      r = product * spiralresult

Alternatively, using 'let':

  spiral (span, dir)
      | span == 0 = 1
      | otherwise = let product = span * dir
                        spanMinus1 = span - 1
                        zeroMinusDir = 0 - dir
                        spiralresult = spiral (spanMinus1, zeroMinusDir)
                        r = product * spiralresult
                    in
                      r

Write a Prolog predicate

  spiral

such that  spiral(S, D, R) is true  iff  R = (spiral S D)
                                             (in Haskell)
*/

spiral(Span, _, 1) :-
  change_this.

spiral(Span, Dir, R) :-
  change_this.

/*
  To test: ?- spiral(6, 10, -720000000).
           true .
           ?- spiral(2, 360, -259200).
           true .
           ?- spiral(3, 21, R).
           R = -55566 .             % type .
           ?- spiral(3, 10, R).
           R = -6000                % type ;
           false.

  Hint: The last two queries (and similar queries) should give
        only one solution.
        If you get more than one solution when you type ;,
        look at how we defined hasFactor.
*/


/*
  Q4: Trees

  Consider the tree     (We are *not* representing
                          trees with Empty "leaves":
             4                         4                     [4, 2, 1]
            / \                      /   \                   [4, 2, 3]
           2   5                   2       5                 [4, 5]
          / \                    /  \     / \
         1   3                 1     3   E   E
                              / \   / \
                          Empty  E E   E            )

  We will express the above tree in Prolog as

    node( 4, node( 2, leaf(1), leaf(3)), leaf(5))
  
  What we are doing here is similar to the Haskell type
  
    data A4Tree = Node Integer A4Tree A4Tree
                | Leaf Integer

  An *in-order traversal* of a tree is the keys we get when we traverse
  (walk through) a tree, visiting the left subtree first, then the root,
  then the right subtree.

  For example, the in-order traversal of the above tree is

    [1, 2, 3, 4, 5]
                                                         which adds:
  We start at 4, and go to its left child:
    the tree node(2, leaf(1), leaf(3)),
      then we go to 2's left child, which is
        leaf(1)                                          1
      then we add 2                                      2
      then we go to 2's right child, which is
        leaf(3)                                          3
    then we add 4                                        4
    then we go to 4's right child, which is
      leaf(5)                                            5

  The predicate

    inorder(T, Keys)

  is true iff, given a tree T, its in-order traversal is Keys.

  ?- inorder( node( 4, node( 2, leaf(1), leaf(3)), leaf(5)), Keys).
  Keys = [1, 2, 3, 4, 5].
*/

inorder(leaf(K), [K]).

inorder(node(K, L, R), Keys) :-
  inorder(L, Lkeys),
  inorder(R, Rkeys),
  append(Lkeys, [K | Rkeys], Keys).  % similar to Haskell
                                     %   Keys  =  Lkeys ++ (K : Rkeys)

/*
Q4a. Define a predicate

  postorder(T, Keys)

that is true iff, given a tree T, its *post-order* traversal is Keys.

In a post-order traversal, we visit the left subtree, the right subtree,
and *then* the root.

For example, you should get

  ?- postorder( node( 4, node( 2, leaf(1), leaf(3)), leaf(5)), Keys).
  Keys = [1, 3, 2, 5, 4]
*/

postorder(leaf(K), [K]).




/*
Q4b.  In-order and post-order traversals are paths through the entire tree.
  In this part of the question, we consider "vertical" paths from the leaves to a root.
  
  In the tree            4
                        / \      
                       2   5     
                      / \        
                     1   3       
                     
  the paths starting from the leaves are:

    1 to 2 to 4          [1, 2, 4]
    3 to 2 to 4          [3, 2, 4]
    5 to 4               [5, 4]

  The above tree can be represented in Prolog as

    node(4, node(2, leaf(1), leaf(3)), leaf(5))

  In this question, define a Prolog predicate

    findpath(Tree, Path)

  such that if we start from a leaf of Tree,
  then Path is a list of numbers from that leaf to the root.

  For example:
  
    ?- findpath(node(2, leaf(1), leaf(3)), [1, 2]).
    true
    ?- findpath(node(2, leaf(1), leaf(3)), [3, 2]).
    true

  Your predicate should be written so that when the first argument is a specific tree
  (containing no variables) and the second argument is a variable, typing ; returns
  *all* possible paths from all the leaves, from left to right.  For example:

    ?- findpath(node(4, node(2, leaf(1), leaf(3)), leaf(5)), Path).
    Path = [1, 2, 4]
    Path = [3, 2, 4]
    Path = [5, 4].

  Hint:
    ?- findpath(leaf(2), [2]).
  should be true.

  Finish defining clauses for 'findpath' below.
*/

findpath(leaf(K), [K]).

