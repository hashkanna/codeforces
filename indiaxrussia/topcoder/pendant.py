class PendantNecklace:
    def maxLength(self, beads):
        from collections import Counter
        c=Counter(beads)
        count=0
        for i in c:
            if c[i]%2==0:
                count+=c[i]
            elif c[i]>2:
                count+=c[i]-1
        return count

p=PendantNecklace()
assert(p.maxLength([1,2,3,2,1])==4)
assert(p.maxLength([7,4,9,1])==0)
assert(p.maxLength([3, 3, 8, 5, 10, 3, 1, 5, 4])==4)




# Problem Statement
# You want to create a pendant necklace - a single strand of beads with a pendant attached to its middle. You have a collection of beads of various colors which you can use for the necklace. You want it to be symmetrical with respect to the pendant, so the beads at the same distance from the pendant must have the same color.
# You are given the list of bead colors as beads. Return the maximal length of the necklace you can create from them. The length of the necklace is defined as the number of beads used in it.
# Definition
# Class: PendantNecklace
# Method: maxLength
# Parameters: tuple (integer)
# Returns: integer
# Method signature: def maxLength(self, beads):
# Limits
# Time limit (s): 2.000
# Memory limit (MB): 256
# Notes
# - The pendant is not included in the beads array.
# Constraints
# - beads will contain between 1 and 50 elements, inclusive.
# - Each element of beads will be between 1 and 10, inclusive.
# Examples
# 0)
# {1, 2, 3, 1, 2}
# Returns: 4
# You can use beads of colors 1 and 2, so that the necklace will look like this: 1 - 2 - pendant - 2 - 1 (or the same with colors 1 and 2 swapped).
# 1)
# {7, 4, 9, 1}
# Returns: 0
# All beads have different colors, so you can't make a necklace.
# 2)
# {3, 3, 8, 5, 10, 3, 1, 5, 4, 3}
# Returns: 6
# You can use more than one pair of beads of the same color.
# This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
