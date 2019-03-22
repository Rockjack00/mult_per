# Tool for calculating the multiplicative persistance of a given integer
# Tyler Olson
# March 22, 2019
# Revision 1.1 ~ change n_list handling for better performance
# Inspired by Numberphile: https://www.youtube.com/watch?v=Wim9WJeDTHQ

import time

def per(n_list, steps=0):
    #print(n)
    if len(n_list) == 1:
        #print("DONE. Steps: {0}".format(steps))
        return steps
    else:
        res = 1
        for d in n_list:
            res *= d
        steps += 1
        return per(listify(res), steps)

def seed(num_digits):
    '''Smallest non-trivial value for a given number of digits above 3.
       Returns a list of digits'''
    return [2] + [6] * (num_digits - 1)

def listify(n):
    '''Takes in an integer and returns a list of all of it's digits'''
    return [int(digit) for digit in str(n)]

def iterate(n_list):
    if n_list[1] == 9:
        poss = [2,3,4,6,7,8,9]
        first = n_list[0] + 1
        if first > 9:
            return None
        if first == 5:
            first = 6
        n_list = [6 for i in range(len(n_list))]
        n_list[0] = first
    else:
        n_list = _iterate(n_list)
    #print(ret_val)
    return n_list
    

def _iterate(n_list):
    last = n_list.pop()
    if last < 9:
        n_list.append(last + 1)
    else:
        n_list = _iterate(n_list)
        last = n_list.pop()
        n_list.append(last)
        n_list.append(last)
    return n_list


def processor(n_list):
    found = False
    while not found:
        steps = per(n_list)
        if steps < 11:
            n_list = iterate(n_list)
            if n_list is None:
                print('None found')
                found = True
        else:
            n = 0
            for d in n_list:
                n = n * 10 + d
            #print(ret_val)
            print('Steps:', steps, n)
            found = True
            return n

def main():
    '''Processes 10^'reps' values, starting at num_digits.'''
    timers = []
    num_digits = 245
    reps = 50
#    for i in range(20):
#        main(2 + i)
    start_1 = time.time()
    for i in range(reps):
        start = time.time()
        n_list = seed(num_digits + i)
        n = processor(n_list)
        if n is not None:
            success = n
            end = time.time()
            print('SUCCESS!!!:', success, 'TIME:', end - start)
            break
        end = time.time()
        timers.append(end - start)
        print(num_digits + i, end - start)
    print(timers)
    print('Total Elapsed time: ', end - start_1)

if __name__ == '__main__':
    main()
