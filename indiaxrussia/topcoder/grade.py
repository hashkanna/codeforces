lectureGrade=int(input())
lectureWeight=int(input())
passingGrade=int(input())

def minToPass(lectureGrade, lectureWeight, passingGrade):
    res = (passingGrade - lectureGrade*(lectureWeight/100.0)) / (1-(lectureWeight/100.0))
    if res>100 or res<0:
        return -1
    return int(res)

print(minToPass(lectureGrade,lectureWeight,passingGrade))

# Problem Statement
# You are preparing for the final exam in an online course, and you want to know score you need to get on it to get a passing grade for the course. The grade for the course is calculated as (percentage of score you got for in-lecture questions) * (weight of in-lecture questions) + (percentage of score you got for final exam) * (weight of final exam).
# lectureGrade is the percentage of max score you got for in-lecture questions.
# lectureWeight is the weight of in-lecture questions in the course grade. The weight of the final exam is 100-lectureWeight.
# passingGrade is the minimal grade you need to get to pass the course, in percent.
# Your score on the final exam will be an integer between 0 and 100, inclusive. Return the score you need to get to pass the course, or -1 if it is impossible for you to pass the course.
# Definition
# Class: ExamGrade
# Method: minToPass
# Parameters:
# Returns: int
# Method signature:
# (be sure your method is public)
# Limits
# Time limit (s): 2.000
# Memory limit (MB): 256
# Constraints
# - lectureGrade will be between 0 and 100, inclusive.
# - lectureWeight will be between 0 and 100, inclusive.
# - passingGrade will be between 0 and 100, inclusive.
# Examples
# 0)
# 70
# 50
# 70
# Returns: 70
# Your grade on lecture is a passing grade, so the exam grade also needs to be at least that same passing grade.
# 1)
# 50
# 50
# 70
# Returns: 90
# Lecture and exam grades have equal weight overall, so 50% and 90% would average out to be 70%.
# 2)
# 0
# 50
# 70
# Returns: -1
# You didn't even bother showing up to class... with a lecture grade so low, there's no hope of passing.
# This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
#
