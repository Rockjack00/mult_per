# Multiplication Persistance Testing
This script searches for numbers with a multiplication persistance of greater than 11 with the purpose of attempting to find a new record holder for highest multiplication persistance of any integer.
Search additionally looks for the smallest value of any given persistance.
Search is based on a seed number of digits (default is 233) based on the current record.

Numberphile Video: https://www.youtube.com/watch?v=Wim9WJeDTHQ&t=3s

## Assumptions:
* Any starting number containing a 5 will have a persistance of 3 or lower (thus any integer containing a 5 is omitted).
* The smallest value must have all digits in ascending order (thus any integer containing 1 is omitted).
* The first digit may be a 2, 3, 4, 6, 7, 8, or 9.
* The any digit after the the first must be 6 or greater due to smallest value rule.
Example:
  per(2377) = 2 * 3 * 7 * 7 = 294
  per(677) = 6 * 7 * 7 = 294
  ==> 2377 need not be checked.
  
  
## Current Progress:
All candidates up to 10^253 have been checked as of 11:43AM 3-22-2019 (PST)
