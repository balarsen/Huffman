

"""
this code is meant to be obvious on the building, populating, storing, and 
decoding of data using a Huffman tree

This is considered a learnng tool more than anything even remotely production


Brian Larsen
14 Apr 2013
"""

import heapq

text = "I am an input string, I will be encoded!"
text = 'Huffman'

def uniq(inlist): 
    # order preserving
    uniques = []
    for item in inlist:
        if item not in uniques:
            uniques.append(item)
    return uniques


heap = []

tree = {}

# populate the heap form the input text
for v in uniq(text):
    cnt = text.count(v)
    print heap, v, cnt
    heapq.heappush(heap, (cnt, v))


while len(heap) > 1:
    print '-------'
    # get the 2 least common
    sym1 = heapq.heappop(heap)
    sym2 = heapq.heappop(heap)
    tree[sym1[1]] = sym1[0]  # in the dict make a key and values
    tree[sym2[1]] = sym2[0]  # in the dict make a key and values
    heapq.heappush(heap, (sym1[0]+sym2[0], sym1[1]+sym2[1]))

    print sym1, sym2
    #print tree

if len(heap) > 0:
    sym1 = heapq.heappop(heap)
    tree[sym1[1]] = sym1[0]  # in the dict make a key and values
   

print '============'
print tree


