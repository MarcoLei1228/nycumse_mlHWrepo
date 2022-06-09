from cgitb import grey
from hashlib import new
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
land_shape = []
land_size = sum(land_shape)
land_num = 0

global_loc = []
global_island_loc_list = []

def creat_new_world(): # 創建底圖
    column, row = 10, 10
    arr = np.zeros([10,10])


    arr[1][1:5], arr[1][8:] = 1, 1
    arr[2][2:5], arr[2][6:] = 1, 1
    arr[3][2:4], arr[3][6:] = 1, 1
    arr[4][1:4], arr[4][6:9] = 1, 1
    arr[5][8] = 1
    arr[6][3:6], arr[6][8] = 1, 1 
    arr[7][3:7] = 1
    arr[8][3:7] = 1
    arr[9][6] = 1
    return arr

def isLand(arr, x, y):
    if x >= 0 and x < 10 and y >= 0 and y < 10 and arr[x][y] == 1:
        return True
    return False

def count_island(arr, x, y, tmp_island):
    
    if isLand(arr, x, y) and ((x,y) not in global_loc):
        if (x,y) not in tmp_island :

            tmp_island.append((x,y))
            print(f"({x},{y}) not in island!!")
            if (x, y) not in global_loc:
                global_loc.append((x,y))
        
    
            if count_island(arr, x+1, y, tmp_island):  # 向右行
                print("right")
                return True

            if count_island(arr, x, y+1, tmp_island):  # 向下行
                print("down")
                return True
            
            if count_island(arr, x-1, y, tmp_island):  # 向左行
                print("left")
                return True

            if count_island(arr, x, y-1, tmp_island):  # 向上行
                print("top")
                return True

    if (tmp_island not in global_island_loc_list) and (tmp_island):
        global_island_loc_list.append(tmp_island)
    
    return

arr = creat_new_world()

# Find Island
new_arr = np.zeros([10,10])
for x in range(10):         # 直行
    for y in range(10):     # 橫行
        if isLand(arr, x, y):
            tmp_island = []
            count_island(arr, x, y, tmp_island)
        else:
            continue

for (x,y) in global_loc:
    new_arr[x,y] = 1

# plt.figure(1)
# plt.imshow(arr, cmap="gray_r")
# plt.figure(1)
# plt.imshow(new_arr, cmap="gray_r")
# plt.show()

fig, axis = plt.subplots(1,5, figsize=(16,8))
axis[0].imshow(arr, cmap='gray_r')
axis[0].set_title("Ground Truth")
axis[0].set_xticks(np.arange(0,10))
axis[0].set_yticks(np.arange(0,10))
axis[1].imshow(new_arr, cmap='gray_r')
axis[1].set_title("Answer")
axis[1].set_xticks(np.arange(0,10))
axis[1].set_yticks(np.arange(0,10))

for idx, island_loc_list in enumerate(global_island_loc_list):
    tmp_arr = np.zeros([10,10])
    for (x,y) in island_loc_list:
        tmp_arr[x,y] = 1
    axis[2+idx].imshow(tmp_arr, cmap='gray_r')
    axis[2+idx].set_title(f"Islands {idx+1} size: {len(island_loc_list)}")
    axis[2+idx].set_xticks(np.arange(0,10))
    axis[2+idx].set_yticks(np.arange(0,10))

plt.show()


for i in range(len(global_island_loc_list)):
    print(f"{i}, {global_island_loc_list[i]}, size={len(global_island_loc_list[i])}")
