#Given an array of heights
#Which contain n vertical heights
#The ends points of the vertical height are (i,0) and (i,height[i])
#Make two pointers point at both the end of the array and move them closer while calculating the water in the container

height = [1,8,6,2,5,4,8,3,7]

left = 0
right = len(height) - 1
max_area = 0

while left < right:
    h = min(height[left], height[right])
    max_area = max(max_area, h * (right - left))
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(max_area)
