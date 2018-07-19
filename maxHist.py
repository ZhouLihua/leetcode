#! /usr/bin/env python


def maxHist(hist):
    index_stack = []
    i = 0
    max_area = 0
    while i < len(hist):
        if len(index_stack) == 0 or hist[index_stack[-1]] <= hist[i]:
            index_stack.append(i)
            i += 1
        else:
            top_val = hist[index_stack[-1]]
            index_stack.pop()
            area = top_val * i
            if len(index_stack) != 0:
                area = top_val * (i - index_stack[-1] -1)
            max_area = max(area, max_area)
    
    while len(index_stack) > 0:
        top_val = hist[index_stack[-1]]
        index_stack.pop()
        area = top_val * i
        if len(index_stack) != 0:
            area = top_val * (i - index_stack[-1] -1)
        max_area = max(area, max_area)
    return max_area


if __name__ == "__main__":
            
     hist = [1, 2, 3, 0, 7]
     print maxHist(hist)
