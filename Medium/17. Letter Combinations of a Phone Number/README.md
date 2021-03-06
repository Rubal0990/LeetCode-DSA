# Letter Combinations of a Phone Number
Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in <b>any order</b>.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![Image](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

## Examples
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```
```
Input: digits = ""
Output: []
```
```
Input: digits = "2"
Output: ["a","b","c"]
```

## Constraints
* 0 <= digits.length <= 4
* `digits[i]` is a digit in the range `['2', '9']`.
