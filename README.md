# stringClassifier

Little binary tree generator which classify a list of string according to dynamic condition.

Mostly inspired by CART algorithm but instead of trying to reduce the "impurity" of a dataset 
(with Gini impurity formula for example)
it tries to split the dataset in equal categories with a Pivot (which a 2 attributes condition).

## How to use it
> The first argument is the maximum amount of element in a group

> All followings arguments are strings to be classified

## Example
> ./stringClassifier.py 2 aa aa ab ac

> ["aa", "aa"]

> ["ab", "ac"]

In this case the dataset is splitted with the "Pivot" : **a at 2**

Which means if the second char in the string equals 'a'.

If true, the string goes in the first array else in the second array.

This algorithm call itself recursively while the number of elements in an array is superior to the value given as argument
