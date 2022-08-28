#!/usr/bin/env python3

def merge(L1, L2):
    size1 = len(L1)
    size2 = len(L2)
    
    i, j = 0, 0
    result = []

    while i < size1 and j <size2:
        if L1[i] < L2[j]:
            result.append(L1[i])
            i += 1
        else:
            result.append(L2[j])
            j += 1
    
    # adding leftovers
    result = result + L1[i:] + L2[j:]
    return result

def main():
    merge([5,3,7,1],[6,1,7,3,6])

if __name__ == "__main__":
    main()
