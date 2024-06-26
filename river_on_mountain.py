def river_finder(mountian, x, y,river_direction = [],vis=[]):
    vis.append((x,y))
    if len(vis)==len(mountain)*len(mountain[0]):
        return river_direction
    if x+1<=len(mountain[0]) and mountain[y][x+1]<mountain[y][x] and (x+1,y) not in river_direction:
        river_direction.append((x+1,y))
        river_finder(mountian, x+1, y, river_direction)
    elif x-1>=0 and mountain[y][x-1]<mountain[y][x] and (x-1,y) not in river_direction:
        river_direction.append((x-1,y))
        river_finder(mountian, x-1, y, river_direction)
    elif y+1<=len(mountain) and mountain[y+1][x]<mountain[y][x] and (x,y+1) not in river_direction:
        river_direction.append((x,y+1))
        river_finder(mountian, x, y+1, river_direction)
    elif y-1>=0 and mountain[y-1][x]<mountain[y][x] and (x,y-1) not in river_direction:
        river_direction.append((x,y-1))
        river_finder(mountian, x, y-1, river_direction)
n, m = map(int, input().split())
x, y = map(int, input().split())
mountain = [list(map(int, input().split())) for i in range(n)]
print(river_finder(mountain,x,y))