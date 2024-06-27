all_rivers = []
def river_finder(mountian, x, y,river_direction = [],flag=0,flag_1=False,counter=0):
    counter+=1
    if x+1<=len(mountain[0]) and mountain[y][x+1]<mountain[y][x] and (x+1,y) not in river_direction:
        river_direction.append((y,x+1))
        river_finder(mountian, x+1, y, river_direction,flag,flag_1,counter)
        river_direction=[]
        flag+=1
        flag_1=True
    if x-1>=0 and mountain[y][x-1]<mountain[y][x] and (x-1,y) not in river_direction:
        river_direction.append((y,x-1))
        river_finder(mountian, x-1, y, river_direction,flag,flag_1,counter)
        river_direction=[]
        if not flag_1:
            flag+=1
            flag_1=True
    if y+1<=len(mountain) and mountain[y+1][x]<mountain[y][x] and (x,y+1) not in river_direction:
        river_direction.append((y+1,x))
        river_finder(mountian, x, y+1, river_direction,flag,flag_1,counter)
        river_direction=[]
        if not flag_1:
            flag+=1
            flag_1=True
    if y-1>=0 and mountain[y-1][x]<mountain[y][x] and (x,y-1) not in river_direction:
        river_direction.append((y-1,x))
        river_finder(mountian, x, y-1, river_direction,flag,flag_1,counter)
        river_direction=[]
        if not flag_1:
            flag+=1
            flag_1=True
    if counter>flag:
        all_rivers.extend(river_direction)
n, m = map(int, input().split())
y, x = map(int, input().split())
mountain = [list(map(int, input().split())) for i in range(n)]
river_finder(mountain,x,y,[(y,x)])
all_rivers=sorted(list(set(all_rivers)),key=lambda x:x[0])
#all_rivers=sorted(all_rivers,key=lambda x:x[1])
print(all_rivers)
#for pos in all_rivers:
    