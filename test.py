def count_paths(width,height):
    if(width==1 and height==1):
        print("end")
        return 1
    if(width<1 or height<1):
        return 0
    print(width,",",height)
    return count_paths(width,height-1)+count_paths(width-1,height)

print(count_paths(6,2))