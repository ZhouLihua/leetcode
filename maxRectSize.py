#!/usr/bin/env python


def maxHist(hist):
    stack = []
    i = 0
    max_area = 0
    area = 0
    while i < len(hist):
        if len(stack) == 0 or hist[stack[-1]] <= hist[i]:
            stack.append(i);
            i += 1
        else:
            top_val = hist[stack[-1]]
            stack.pop()
            area = top_val * i
            if len(stack) > 0:
                area = top_val * (i - 1 - stack[-1])
            max_area = max(max_area, area)
    
    while len(stack) > 0:
        top_val = hist[stack[-1]]
        stack.pop()
        area = top_val * i
        if len(stack) > 0:
            area = top_val * (i - 1 - stack[-1])
        max_area = max(max_area, area)
    return max_area

def maxRectSize(rect):
    res = maxHist(rect[0])
    i = 1
    while i < len(rect):
        for j in range(len(rect[i])):
            if rect[i][j] == 1:
                rect[i][j] = rect[i-1][j] + 1
            res = max(res, maxHist(rect[i]))
        i += 1
    return res

if __name__ == "__main__":
    rect = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]
    print maxRectSize(rect)
