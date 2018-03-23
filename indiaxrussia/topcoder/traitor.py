class TraitorRecognition:
    def getsets(self, n, k):
        


# Problem Statement
# Hero has n stones: 2*k red ones and n-2*k green ones. He wants to split the stones into two disjoint sets so that each set will contain exactly k red stones (the number of green stones in each set doesn't matter). Unfortunately, Hero is color blind, and thus can't distinguish the stones.
# Hero decides to ask his friend Jack of Blades to help him verify his splits. Hero will split the stones somehow and ask Jack whether both sets in the proposed split contain k red stones. Jack will answer "Yes" or "No" but will not give any other information. Hero doesn't want to ask Jack about more than max(n-3, 5) splits.
# Help Hero to prepare several splits to ask Jack about so that at least one of the splits is guaranteed to satisfy the condition. The splits should be represented as an array of strings, each string should consist of n characters, and each character should be '0' or '1'. i-th string represents i-th split to try: if j-th character of i-th string is '1', then j-th stone is assigned to the first subset of the i-th split, otherwise it is assigned to the second subset.
# Definition
# Class: TraitorRecognition
# Method: getsets
# Parameters: integer, integer
# Returns: tuple (string)
# Method signature: def getsets(self, n, k):
# Limits
# Time limit (s): 2.000
# Memory limit (MB): 256
# Constraints
# - n will be between 2 and 20, inclusive.
# - k will be between 1 and n/2, inclusive.
# Examples
# 0)
# 4
# 2
# Returns: {"1100", "0110", "0011" }
# 1)
# 4
# 1
# Returns: {"1100", "0110", "0011" }
# 2)
# 20
# 3
# Returns: {"11111111110000000000", "01111111111000000000", "00111111111100000000", "00011111111110000000", "00001111111111000000", "00000111111111100000", "00000011111111110000", "00000001111111111000", "00000000111111111100", "00000000011111111110", "00000000001111111111" }
# 3)
# 15
# 2
# Returns: {"111111110000000", "011111111000000", "001111111100000", "000111111110000", "000011111111000", "000001111111100", "000000111111110", "000000011111111", "000000001111111" }
# 4)
# 15
# 7
# Returns: {"111111110000000", "011111111000000", "001111111100000", "000111111110000", "000011111111000", "000001111111100", "000000111111110", "000000011111111", "000000001111111" }
# This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
