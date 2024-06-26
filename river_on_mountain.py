def river_finder(mountian, x, y,river_direction = [],vis=[]):
    if x+1<=len(mountain[0]) and mountain[y][x+1]<mountain[y][x] and (x+1,y) not in river_direction:
        river_direction.append((x+1,y))
        river_finder(mountian, x+1, y, river_direction,vis)
    elif x-1>=0 and mountain[y][x-1]<mountain[y][x] and (x-1,y) not in river_direction:
        river_direction.append((x-1,y))
        river_finder(mountian, x-1, y, river_direction,vis)
    elif y+1<=len(mountain) and mountain[y+1][x]<mountain[y][x] and (x,y+1) not in river_direction:
        river_direction.append((x,y+1))
        river_finder(mountian, x, y+1, river_direction,vis)
    elif y-1>=0 and mountain[y-1][x]<mountain[y][x] and (x,y-1) not in river_direction:
        river_direction.append((x,y-1))
        river_finder(mountian, x, y-1, river_direction,vis)
    else:
        return 'hi'
n, m = map(int, input().split())
x, y = map(int, input().split())
mountain = [list(map(int, input().split())) for i in range(n)]
print(mountain)
print('####################################')
print(river_finder(mountain,x,y,[(x,y)]))