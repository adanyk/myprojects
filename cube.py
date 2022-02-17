import random
import numpy as np
import time


solved = "wwwwwwwwwooooooooogggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy"



#Display cube:

def display(cube):
    print(4 * ' ' + cube[:3])
    print(4 * ' ' + cube[3:6])
    print(4 * ' ' + cube[6:9])
    print(cube[9:12] + ' ' + cube[18:21] + ' ' + cube[27:30] + ' ' + cube[36:39])
    print(cube[12:15] + ' ' + cube[21:24] + ' ' + cube[30:33] + ' ' + cube[39:42])
    print(cube[15:18] + ' ' + cube[24:27] + ' ' + cube[33:36] + ' ' + cube[42:45])
    print(4 * ' ' + cube[45:48])
    print(4 * ' ' + cube[48:51])
    print(4 * ' ' + cube[51:])

#] + cube[]     ("", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
#           0  1  2
#           3  4  5
#           6  7  8

# 9 10 11  18 19 20  27 28 29  36 37 38
#12 13 14  21 22 23  30 31 32  39 40 41
#15 16 17  24 25 26  33 34 35  42 43 44

#          45 46 47
#          48 49 50
#          51 52 53




#Moving functions:

def scramble_move(cube, move):
    if move == 'U':
        return cube[6] + cube[3] + cube[0] + cube[7] + cube[4] + cube[1] + cube[8] + cube[5] + cube[2] + cube[18:21] + cube[12:18] + cube[27:30] + cube[21:27] + cube[36:39] + cube[30:36] + cube[9:12] + cube[39:]
    elif move == 'U\'':
        return cube[2] + cube[5] + cube[8] + cube[1] + cube[4] + cube[7] + cube[0] + cube[3] + cube[6] + cube[36:39] + cube[12:18] + cube[9:12] + cube[21:27] + cube[18:21] + cube[30:36] + cube[27:30] + cube[39:]
    elif move == 'U2' or move == 'U2\'':
        return cube[8::-1] + cube[27:30] + cube[12:18] + cube[36:39] + cube[21:27] + cube[9:12] + cube[30:36] + cube[18:21] + cube[39:]

    elif move == 'D':
        return cube[:15] + cube[42:45] + cube[18:24] + cube[15:18] + cube[27:33] + cube[24:27] + cube[36:42] + cube[33:36] + cube[51] + cube[48] + cube[45] + cube[52] + cube[49] + cube[46] + cube[53] + cube[50] + cube[47]
    elif move == 'D\'':
        return cube[:15] + cube[24:27] + cube[18:24] + cube[33:36] + cube[27:33] + cube[42:45] + cube[36:42] + cube[15:18] + cube[47] + cube[50] + cube[53] + cube[46] + cube[49] + cube[52] + cube[45] + cube[48] + cube[51]
    elif move == 'D2' or move == 'D2\'':
        return cube[:15] + cube[33:36] + cube[18:24] + cube[42:45] + cube[27:33] + cube[15:18] + cube[36:42] + cube[24:27] + cube[:44:-1]

    elif move == 'L':
        return cube[44] + cube[1:3] + cube[41] + cube[4:6] + cube[38] + cube[7:9] + cube[15] + cube[12] + cube[9] + cube[16] + cube[13] + cube[10] + cube[17] + cube[14] + cube[11] + cube[0] + cube[19:21] + cube[3] + cube[22:24] + cube[6] + cube[25:38] + cube[51] + cube[39:41] + cube[48] + cube[42:44] + cube[45] + cube[18] + cube[46:48] + cube[21] + cube[49:51] + cube[24] + cube[52:]
    elif move == 'L\'':
        return cube[18] + cube[1:3] + cube[21] + cube[4:6] + cube[24] + cube[7:9] + cube[11] + cube[14] + cube[17] + cube[10] + cube[13] + cube[16] + cube[9] + cube[12] + cube[15] + cube[45] + cube[19:21] + cube[48] + cube[22:24] + cube[51] + cube[25:38] + cube[6] + cube[39:41] + cube[3] + cube[42:44] + cube[0] + cube[44] + cube[46:48] + cube[41] + cube[49:51] + cube[38] + cube[52:]
    elif move == 'L2' or move == 'L2\'':
        return cube[45] + cube[1:3] + cube[48] + cube[4:6] + cube[51] + cube[7:9] + cube[17:8:-1] + cube[44] + cube[19:21] + cube[41] + cube[22:24] + cube[38] + cube[25:38] + cube[24] + cube[39:41] + cube[21] + cube[42:44] + cube[18] + cube[0] + cube[46:48] + cube[3] + cube[49:51] + cube[6] + cube[52:]

    elif move == 'R':
        return cube[0:2] + cube[20] + cube[3:5] + cube[23] + cube[6:8] + cube[26] + cube[9:20] + cube[47] + cube[21:23] + cube[50] + cube[24:26] + cube[53] + cube[33] + cube[30] + cube[27] + cube[34] + cube[31] + cube[28] + cube[35] + cube[32] + cube[29] + cube[8] + cube[37:39] + cube[5] + cube[40:42] + cube[2] + cube[43:47] + cube[42] + cube[48:50] + cube[39] + cube[51:53] + cube[36]
    elif move == 'R\'':
        return cube[0:2] + cube[42] + cube[3:5] + cube[39] + cube[6:8] + cube[36] + cube[9:20] + cube[2] + cube[21:23] + cube[5] + cube[24:26] + cube[8] + cube[29] + cube[32] + cube[35] + cube[28] + cube[31] + cube[34] + cube[27] + cube[30] + cube[33] + cube[53] + cube[37:39] + cube[50] + cube[40:42] + cube[47] + cube[43:47] + cube[20] + cube[48:50] + cube[23] + cube[51:53] + cube[26]
    elif move == 'R2' or move == 'R2\'':
        return cube[0:2] + cube[47] + cube[3:5] + cube[50] + cube[6:8] + cube[53] + cube[9:20] + cube[42] + cube[21:23] + cube[39] + cube[24:26] + cube[36] + cube[35:25:-1] + cube[37:39] + cube[23] + cube[40:42] + cube[20] + cube[43:47] + cube[2] + cube[48:50] + cube[5] + cube[51:53] + cube[8]

    elif move == 'F':
        return cube[0:6] + cube[17] + cube[14] + cube[11] + cube[9:11] + cube[45] + cube[12:14] + cube[46] + cube[15:17] + cube[47] + cube[24] + cube[21] + cube[18] + cube[25] + cube[22] + cube[19] + cube[26] + cube[23] + cube[20] + cube[6] + cube[28:30] + cube[7] + cube[31:33] + cube[8] + cube[34:45] + cube[33] + cube[30] + cube[27] + cube[48:]
    elif move == 'F\'':
        return cube[0:6] + cube[27] + cube[30] + cube[33] + cube[9:11] + cube[8] + cube[12:14] + cube[7] + cube[15:17] + cube[6] + cube[20] + cube[23] + cube[26] + cube[19] + cube[22] + cube[25] + cube[18] + cube[21] + cube[24] + cube[47] + cube[28:30] + cube[46] + cube[31:33] + cube[45] + cube[34:45] + cube[11] + cube[14] + cube[17] + cube[48:]
    elif move == 'F2' or move == 'F2\'':
        return cube[0:6] + cube[47:44:-1] + cube[9:11] + cube[33] + cube[12:14] + cube[30] + cube[15:17] + cube[27:16:-1] + cube[28:30] + cube[14] + cube[31:33] + cube[11] + cube[34:45] + cube[8:5:-1] + cube[48:]

    elif move == 'B':
        return cube[29] + cube[32] + cube[35] + cube[3:9] + cube[2] + cube[10:12] + cube[1] + cube[13:15] + cube[0] + cube[16:29] + cube[53] + cube[30:32] + cube[52] + cube[33:35] + cube[51] + cube[42] + cube[39] + cube[36] + cube[43] + cube[40] + cube[37] + cube[44] + cube[41] + cube[38] + cube[45:51] + cube[9] + cube[12] + cube[15]
    elif move == 'B\'':
        return cube[15] + cube[12] + cube[9] + cube[3:9] + cube[51] + cube[10:12] + cube[52] + cube[13:15] + cube[53] + cube[16:29] + cube[0] + cube[30:32] + cube[1] + cube[33:35] + cube[2] + cube[38] + cube[41] + cube[44] + cube[37] + cube[40] + cube[43] + cube[36] + cube[39] + cube[42] + cube[45:51] + cube[35] + cube[32] + cube[29]
    elif move == 'B2' or move == 'B2\'':
        return cube[:50:-1] + cube[3:9] + cube[35] + cube[10:12] + cube[32] + cube[13:15] + cube[29] + cube[16:29] + cube[15] + cube[30:32] + cube[12] + cube[33:35] + cube[9] + cube[44:35:-1] + cube[45:51] + cube[2::-1]
    else:
        return None


def middle_move(cube, move):    
    if move == 'M':
        return cube[0] + cube[43] + cube[2:4] + cube[40] + cube[5:7] + cube[37] + cube[8:19] + cube[1] + cube[20:22] + cube[4] + cube[23:25] + cube[7] + cube[26:37] + cube[52] + cube[38:40] + cube[49] + cube[41:43] + cube[46] + cube[44:46] + cube[19] + cube[47:49] + cube[22] + cube[50:52] + cube[25] + cube[53]
    elif move == 'M\'':
        return cube[0] + cube[19] + cube[2:4] + cube[22] + cube[5:7] + cube[25] + cube[8:19] + cube[46] + cube[20:22] + cube[49] + cube[23:25] + cube[52] + cube[26:37] + cube[7] + cube[38:40] + cube[4] + cube[41:43] + cube[1] + cube[44:46] + cube[43] + cube[47:49] + cube[40] + cube[50:52] + cube[37] + cube[53]
    elif move == 'M2' or move == 'M2\'':
        return cube[0] + cube[46] + cube[2:4] + cube[49] + cube[5:7] + cube[52] + cube[8:19] + cube[43] + cube[20:22] + cube[40] + cube[23:25] + cube[37] + cube[26:37] + cube[25] + cube[38:40] + cube[22] + cube[41:43] + cube[19] + cube[44:46] + cube[1] + cube[47:49] + cube[4] + cube[50:52] + cube[7] + cube[53]

    elif move == 'E':
        return cube[0:12] + cube[39:42] + cube[15:21] + cube[12:15] + cube[24:30] + cube[21:24] + cube[33:39] + cube[30:33] + cube[42:]
    elif move == 'E\'':
        return cube[0:12] + cube[21:24] + cube[15:21] + cube[30:33] + cube[24:30] + cube[39:42] + cube[33:39] + cube[12:15] + cube[42:]
    elif move == 'E2' or move == 'E2\'':
        return cube[0:12] + cube[30:33] + cube[15:21] + cube[39:42] + cube[24:30] + cube[12:15] + cube[33:39] + cube[21:24] + cube[42:]
    
    elif move == 'S':
        return cube[0:3] + cube[16] + cube[13] + cube[10] + cube[6:10] + cube[48] + cube[11:13] + cube[49] + cube[14:16] + cube[50] + cube[17:28] + cube[3] + cube[29:31] + cube[4] + cube[32:34] + cube[5] + cube[35:48] + cube[34] + cube[31] + cube[28] + cube[51:]
    elif move == 'S\'':
        return cube[0:3] + cube[28] + cube[31] + cube[34] + cube[6:10] + cube[5] + cube[11:13] + cube[4] + cube[14:16] + cube[3] + cube[17:28] + cube[50] + cube[29:31] + cube[49] + cube[32:34] + cube[48] + cube[35:48] + cube[10] + cube[13] + cube[16] + cube[51:]
    elif move == 'S2' or move == 'S2\'':
        return cube[0:3] + cube[50] + cube[49] + cube[48] + cube[6:10] + cube[34] + cube[11:13] + cube[31] + cube[14:16] + cube[28] + cube[17:28] + cube[16] + cube[29:31] + cube[13] + cube[32:34] + cube[10] + cube[35:48] + cube[5] + cube[4] + cube[3] + cube[51:]
    else:
        return None

def double_layer_move(cube, move):
    if move == 'u':
        return cube[6] + cube[3] + cube[0] + cube[7] + cube[4] + cube[1] + cube[8] + cube[5] + cube[2] + cube[18:24] + cube[15:18] + cube[27:33] + cube[24:27] + cube[36:42] + cube[33:36] + cube[9:15] + cube[42:]
    elif move == 'u\'':
        return cube[2] + cube[5] + cube[8] + cube[1] + cube[4] + cube[7] + cube[0] + cube[3] + cube[6] + cube[36:42] + cube[15:18] + cube[9:15] + cube[24:27] + cube[18:24] + cube[33:36] + cube[27:33] + cube[42:]
    elif move == 'u2' or move == 'u2\'':
        return cube[8::-1] + cube[27:33] + cube[15:18] + cube[36:42] + cube[24:27] + cube[9:15] + cube[33:36] + cube[18:24] + cube[42:]

    elif move == 'd':
        return cube[:12] + cube[39:45] + cube[18:21] + cube[12:18] + cube[27:30] + cube[21:27] + cube[36:39] + cube[30:36] + cube[51] + cube[48] + cube[45] + cube[52] + cube[49] + cube[46] + cube[53] + cube[50] + cube[47]
    elif move == 'd\'':
        return cube[:12] + cube[21:27] + cube[18:21] + cube[30:36] + cube[27:30] + cube[39:45] + cube[36:39] + cube[12:18] + cube[47] + cube[50] + cube[53] + cube[46] + cube[49] + cube[52] + cube[45] + cube[48] + cube[51]
    elif move == 'd2' or move == 'd2\'':
        return cube[:12] + cube[30:36] + cube[18:21] + cube[39:45] + cube[27:30] + cube[12:18] + cube[36:39] + cube[21:27] + cube[:44:-1]

    elif move == 'l':
        return cube[44] + cube[43] + cube[2] + cube[41] + cube[40] + cube[5] + cube[38] + cube[37] + cube[8] + cube[15] + cube[12] + cube[9] + cube[16] + cube[13] + cube[10] + cube[17] + cube[14] + cube[11] + cube[0:2] + cube[20] + cube[3:5] + cube[23] + cube[6:8] + cube[26:37] + cube[52] + cube[51] + cube[39] + cube[49] + cube[48] + cube[42] + cube[46] + cube[45] + cube[18:20] + cube[47] + cube[21:23] + cube[50] + cube[24:26] + cube[53]
    elif move == 'l\'':
        return cube[18:20] + cube[2] + cube[21:23] + cube[5] + cube[24:26] + cube[8] + cube[11] + cube[14] + cube[17] + cube[10] + cube[13] + cube[16] + cube[9] + cube[12] + cube[15] + cube[45:47] + cube[20] + cube[48:50] + cube[23] + cube[51:53] + cube[26:37] + cube[7] + cube[6] + cube[39] + cube[4] + cube[3] + cube[42] + cube[1] + cube[0] + cube[44] + cube[43] + cube[47] + cube[41] + cube[40] + cube[50] + cube[38] + cube[37] + cube[53]
    elif move == 'l2' or move == 'l2\'':
        return cube[45:47] + cube[2] + cube[48:50] + cube[5] + cube[51:53] + cube[8] + cube[17:8:-1] + cube[44] + cube[43] + cube[20] + cube[41] + cube[40] + cube[23] + cube[38] + cube[37] + cube[26:37] + cube[25] + cube[24] + cube[39] + cube[22] + cube[21] + cube[42] + cube[19] + cube[18] + cube[0:2] + cube[47] + cube[3:5] + cube[50] + cube[6:8] + cube[53]

    elif move == 'r':
        return cube[0] + cube[19:21] + cube[3] + cube[22:24] + cube[6] + cube[25:27] + cube[9:19] + cube[46:48] + cube[21] + cube[49:51] + cube[24] + cube[52:] + cube[33] + cube[30] + cube[27] + cube[34] + cube[31] + cube[28] + cube[35] + cube[32] + cube[29] + cube[8] + cube[7] + cube[38] + cube[5] + cube[4] + cube[41] + cube[2] + cube[1] + cube[44:46] + cube[43] + cube[42] + cube[48] + cube[40] + cube[39] + cube[51] + cube[37] + cube[36]
    elif move == 'r\'':
        return cube[0] + cube[43] + cube[42] + cube[3] + cube[40] + cube[39] + cube[6] + cube[37] + cube[36] + cube[9:19] + cube[1:3] + cube[21] + cube[4:6] + cube[24] + cube[7:9] + cube[29] + cube[32] + cube[35] + cube[28] + cube[31] + cube[34] + cube[27] + cube[30] + cube[33] + cube[53] + cube[52] + cube[38] + cube[50] + cube[49] + cube[41] + cube[47] + cube[46] + cube[44:46] + cube[19:21] + cube[48] + cube[22:24] + cube[51] + cube[25:27]
    elif move == 'r2' or move == 'r2\'':
        return cube[0] + cube[46:48] + cube[3] + cube[49:51] + cube[6] + cube[52:] + cube[9:19] + cube[43] + cube[42] + cube[21] + cube[40] + cube[39] + cube[24] + cube[37] + cube[36] + cube[35:24:-1] + cube[38] + cube[23] + cube[22] + cube[41] + cube[20] + cube[19] + cube[44:46] + cube[1:3] + cube[48] + cube[4:6] + cube[51] + cube[7:9]

    elif move == 'f':
        return cube[0:3] + cube[16] + cube[13] + cube[10] + cube[17] + cube[14] + cube[11] + cube[9] + cube[48] + cube[45] + cube[12] + cube[49] + cube[46] + cube[15] + cube[50] + cube[47] + cube[24] + cube[21] + cube[18] + cube[25] + cube[22] + cube[19] + cube[26] + cube[23] + cube[20] + cube[6] + cube[3] + cube[29] + cube[7] + cube[4] + cube[32] + cube[8] + cube[5] + cube[35:45] + cube[33] + cube[30] + cube[27] + cube[34] + cube[31] + cube[28] + cube[51:]
    elif move == 'f\'':
        return cube[0:3] + cube[28] + cube[31] + cube[34] + cube[27] + cube[30] + cube[33] + cube[9] + cube[5] + cube[8] + cube[12] + cube[4] + cube[7] + cube[15] + cube[3] + cube[6] + cube[20] + cube[23] + cube[26] + cube[19] + cube[22] + cube[25] + cube[18] + cube[21] + cube[24] + cube[47] + cube[50] + cube[29] + cube[46] + cube[49] + cube[32] + cube[45] + cube[48] + cube[35:45] + cube[11] + cube[14] + cube[17] + cube[10] + cube[13] + cube[16] + cube[51:]
    elif move == 'f2' or move == 'f2\'':
        return cube[0:3] + cube[50:44:-1] + cube[9] + cube[34] + cube[33] + cube[12] + cube[31] + cube[30] + cube[15] + cube[28:15:-1] + cube[29] + cube[14] + cube[13] + cube[32] + cube[11] + cube[10] + cube[35:45] + cube[8:2:-1] + cube[51:]

    elif move == 'b':
        return cube[29] + cube[32] + cube[35] + cube[28] + cube[31] + cube[34] + cube[6:9] + cube[2] + cube[5] + cube[11] + cube[1] + cube[4] + cube[14] + cube[0] + cube[3] + cube[17:28] + cube[50] + cube[53] + cube[30] + cube[49] + cube[52] + cube[33] + cube[48] + cube[51] + cube[42] + cube[39] + cube[36] + cube[43] + cube[40] + cube[37] + cube[44] + cube[41] + cube[38] + cube[45:48] + cube[10] + cube[13] + cube[16] + cube[9] + cube[12] + cube[15]
    elif move == 'b\'':
        return cube[15] + cube[12] + cube[9] + cube[16] + cube[13] + cube[10] + cube[6:9] + cube[51] + cube[48] + cube[11] + cube[52] + cube[49] + cube[14] + cube[53] + cube[50] + cube[17:28] + cube[3] + cube[0] + cube[30] + cube[4] + cube[1] + cube[33] + cube[5] + cube[2] + cube[38] + cube[41] + cube[44] + cube[37] + cube[40] + cube[43] + cube[36] + cube[39] + cube[42] + cube[45:48] + cube[34] + cube[31] + cube[28] + cube[35] + cube[32] + cube[29]
    elif move == 'b2' or move == 'b2\'':
        return cube[:47:-1] + cube[6:9] + cube[35] + cube[34] + cube[11] + cube[32] + cube[31] + cube[14] + cube[29] + cube[28] + cube[17:28] + cube[16] + cube[15] + cube[30] + cube[13] + cube[12] + cube[33] + cube[10] + cube[9] + cube[44:35:-1] + cube[45:48] + cube[5::-1]
    else:
        return None

def rotation_move(cube, move):
    if move == 'x':
        return cube[18:27] + cube[11] + cube[14] + cube[17] + cube[10] + cube[13] + cube[16] + cube[9] + cube[12] + cube[15] + cube[45:] + cube[33] + cube[30] + cube[27] + cube[34] + cube[31] + cube[28] + cube[35] + cube[32] + cube[29] + cube[8::-1] + cube[44:35:-1]
    elif move == 'x\'':
        return cube[44:35:-1] + cube[15] + cube[12] + cube[9] + cube[16] + cube[13] + cube[10] + cube[17] + cube[14] + cube[11] + cube[:9] + cube[29] + cube[32] + cube[35] + cube[28] + cube[31] + cube[34] + cube[27] + cube[30] + cube[33] + cube[:44:-1] + cube[18:27]
    elif move == 'x2' or move == 'x2\'':
        return cube[45::1] + cube[17:8:-1] + cube[44:17:-1] + cube[:9]
    
    elif move == 'y':
        return cube[6] + cube[3] + cube[0] + cube[7] + cube[4] + cube[1] + cube[8] + cube[5] + cube[2] + cube[18:45] + cube[9:18] + cube[47] + cube[50] + cube[53] + cube[46] + cube[49] + cube[52] + cube[45] + cube[48] + cube[51]
    elif move == 'y\'':
        return cube[2] + cube[5] + cube[8] + cube[1] + cube[4] + cube[7] + cube[0] + cube[3] + cube[6] + cube[36:45] + cube[9:36] + cube[51] + cube[48] + cube[45] + cube[52] + cube[49] + cube[46] + cube[53] + cube[50] + cube[47]
    elif move == 'y2' or move == 'y2\'':
        return cube[8::-1] + cube[27:45] + cube[9:27] + cube[:44:-1]
    
    elif move == 'z':
        return cube[15] + cube[12] + cube[9] + cube[16] + cube[13] + cube[10] + cube[17] + cube[14] + cube[11] + cube[51] + cube[48] + cube[45] + cube[52] + cube[49] + cube[46] + cube[53] + cube[50] + cube[47] + cube[24] + cube[21] + cube[18] + cube[25] + cube[22] + cube[19] + cube[26] + cube[23] + cube[20] + cube[6] + cube[3] + cube[0] + cube[7] + cube[4] + cube[1] + cube[8] + cube[5] + cube[2] + cube[38] + cube[41] + cube[44] + cube[37] + cube[40] + cube[43] + cube[36] + cube[39] + cube[42] + cube[33] + cube[30] + cube[27] + cube[34] + cube[31] + cube[28] + cube[35] + cube[32] + cube[29]
    elif move == 'z\'':
        return cube[29] + cube[32] + cube[35] + cube[28] + cube[31] + cube[34] + cube[27] + cube[30] + cube[33] + cube[2] + cube[5] + cube[8] + cube[1] + cube[4] + cube[7] + cube[0] + cube[3] + cube[6] + cube[20] + cube[23] + cube[26] + cube[19] + cube[22] + cube[25] + cube[18] + cube[21] + cube[24] + cube[47] + cube[50] + cube[53] + cube[46] + cube[49] + cube[52] + cube[45] + cube[48] + cube[51] + cube[42] + cube[39] + cube[36] + cube[43] + cube[40] + cube[37] + cube[44] + cube[41] + cube[38] + cube[11] + cube[14] + cube[17] + cube[10] + cube[13] + cube[16] + cube[9] + cube[12] + cube[15]
    elif move == 'z2' or move == 'z2\'':
        return cube[:44:-1] + cube[35:8:-1] + cube[44:35:-1] + cube[8::-1]
    else:
        return None


scramble_moves = ('U', 'U\'', 'U2', 'D', 'D\'', 'D2', 'L', 'L\'', 'L2', 'R', 'R\'', 'R2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2')
not_scramble_moves = ('M', 'M\'', 'M2', 'E', 'E\'', 'E2', 'S', 'S\'', 'S2', 'u', 'u\'', 'u2', 'd', 'd\'', 'd2', 'l', 'l\'', 'l2', 'r', 'r\'', 'r2', 'f', 'f\'', 'f2', 'b', 'b\'', 'b2', 'x', 'x\'', 'x2', 'y', 'y\'', 'y2', 'z', 'z\'', 'z2')
useless_moves = ('U2\'', 'D2\'', 'L2\'', 'R2\'', 'F2\'', 'B2\'', 'M2\'', 'E2\'', 'S2\'', 'u2\'', 'd2\'', 'l2\'', 'r2\'', 'f2\'', 'b2\'', 'x2\'', 'y2\'', 'z2\'')

#scramble_moves slices
without_U = ('D', 'D\'', 'D2', 'L', 'L\'', 'L2', 'R', 'R\'', 'R2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2')
without_D = ('U', 'U\'', 'U2', 'L', 'L\'', 'L2', 'R', 'R\'', 'R2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2')
without_L = ('U', 'U\'', 'U2', 'D', 'D\'', 'D2', 'R', 'R\'', 'R2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2')
without_R = ('U', 'U\'', 'U2', 'D', 'D\'', 'D2', 'L', 'L\'', 'L2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2')
without_F = ('U', 'U\'', 'U2', 'D', 'D\'', 'D2', 'L', 'L\'', 'L2', 'R', 'R\'', 'R2', 'B', 'B\'', 'B2')
without_B = ('U', 'U\'', 'U2', 'D', 'D\'', 'D2', 'L', 'L\'', 'L2', 'R', 'R\'', 'R2', 'F', 'F\'', 'F2')
without_UD = ('L', 'L\'', 'L2', 'R', 'R\'', 'R2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2')
without_LR = ('U', 'U\'', 'U2', 'D', 'D\'', 'D2', 'F', 'F\'', 'F2', 'B', 'B\'', 'B2')
without_FB = ('U', 'U\'', 'U2', 'D', 'D\'', 'D2', 'L', 'L\'', 'L2', 'R', 'R\'', 'R2')


def do_simple_scramble(cube, moves):
    for m in moves:
        cube = scramble_move(cube, m)
    return cube

def do_any_scramble(cube, moves):
    for m in moves:
        temp = scramble_move(cube, m)
        if temp == None:
            temp = middle_move(cube, m)
            if temp == None:
                temp = double_layer_move(cube, m)
                if temp == None:
                    temp = rotation_move(cube, m)
                    if temp == None:
                        print("Invalid move:", m)
        cube = temp
    return cube




#Generating scramble:

def opposite_layer(move1, move2):
    if move1[0] == 'U':
        move1 = 'D'
    elif move1[0] == 'L':
        move1 = 'R'
    elif move1[0] == 'F':
        move1 = 'B'
    
    if move2[0] == 'U':
        move2 = 'D'
    elif move2[0] == 'L':
        move2 = 'R'
    elif move2[0] == 'F':
        move2 = 'B'
    
    if move1[0] == move2[0]:
        return False
    else:
        return True

def generate_scramble(n=25):
    scramble = list()
    scramble.append(random.choice(scramble_moves))
    while len(scramble) < 2:
        next = random.choice(scramble_moves)
        if next[0] != scramble[-1][0]:
            scramble.append(next)        
    while len(scramble) < n:
        next = random.choice(scramble_moves)
        if opposite_layer(next, scramble[-1]):
            scramble.append(next)
        elif next[0] != scramble[-1][0] and next[0] != scramble[-2][0]:
            scramble.append(next)
    for m in scramble:
        print(m, end=' ')
    print("\n")
    display(do_simple_scramble(solved, scramble))
    return scramble




#Solving functions:

#Cross:

def evaluate_cross_onebyone(cube):
    eval = 0
    if cube[16] + cube[48] == "oy":
        eval += 1
    if cube[25] + cube[46] == "gy":
        eval += 1
    if cube[34] + cube[50] == "ry":
        eval += 1
    if cube[43] + cube[52] == "by":
        eval += 1

    return eval

def evaluate_cross_o(cube):
    if cube[16] + cube[48] == "oy":
        return True
    else:
        return False

def evaluate_cross_g(cube):
    if cube[25] + cube[46] == "gy":
        return True
    else:
        return False

def evaluate_cross_r(cube):
    if cube[34] + cube[50] == "ry":
        return True
    else:
        return False

def evaluate_cross_b(cube):
    if cube[43] + cube[52] == "by":
        return True
    else:
        return False


def cross_increase(scrambled, e):
        #1
        for m in without_U:
            if evaluate_cross_onebyone(do_simple_scramble(scrambled, tuple([m]))) > e:
                return [m]
        
        #2
        for m in scramble_moves:
            for n in without_U:
                if n[0] != m[0]:
                    if evaluate_cross_onebyone(do_simple_scramble(scrambled, tuple([m, n]))) > e:
                        return [m, n]
        #3
        for m in scramble_moves:
            for n in scramble_moves:
                if not opposite_layer(m, n):
                    for o in without_U:
                        if n[0] != o[0] != m[0]:
                            if evaluate_cross_onebyone(do_simple_scramble(scrambled, tuple([m, n, o]))) > e:
                                return [m, n, o]
                else:
                    for o in without_U:
                        if o[0] != n[0]:
                            if evaluate_cross_onebyone(do_simple_scramble(scrambled, tuple([m, n, o]))) > e:
                                return [m, n, o]

        #4
        if not evaluate_cross_o(scrambled):
            if evaluate_cross_o(do_simple_scramble(scrambled, ("L\'", "D", "F\'", "D\'"))):
                return ["L\'", "D", "F\'", "D\'"]
            elif evaluate_cross_o(do_simple_scramble(scrambled, ("U\'", "F\'", "L", "F"))):
                return ["U\'", "F\'", "L", "F"]
            elif evaluate_cross_o(do_simple_scramble(scrambled, ("U", "F\'", "L", "F"))):
                return ["U", "F\'", "L", "F"]
            else:
                return ["R", "D", "F", "D\'"]
        
        elif not evaluate_cross_g(scrambled):
            if evaluate_cross_g(do_simple_scramble(scrambled, ("F\'", "D", "R\'", "D\'"))):
                return ["F\'", "D", "R'", "D\'"]
            elif evaluate_cross_g(do_simple_scramble(scrambled, ("U\'", "R\'", "F", "R"))):
                return ["U\'", "R\'", "F", "R"]
            elif evaluate_cross_g(do_simple_scramble(scrambled, ("U", "R\'", "F", "R"))):
                return ["U", "R\'", "F", "R"]
            else:
                return ["B", "D", "R", "D\'"]
        
        elif not evaluate_cross_r(scrambled):
            if evaluate_cross_r(do_simple_scramble(scrambled, ("R", "D\'", "F", "D"))):
                return ["R", "D\'", "F", "D"]
            elif evaluate_cross_r(do_simple_scramble(scrambled, ("U", "F", "R\'", "F\'"))):
                return ["U", "F", "R\'", "F\'"]
            elif evaluate_cross_r(do_simple_scramble(scrambled, ("U\'", "F", "R\'", "F\'"))):
                return ["U\'", "F", "R\'", "F\'"]
            else:
                return ["L", "D\'", "F\'", "D"]
        
        else:
            if evaluate_cross_b(do_simple_scramble(scrambled, ("B", "D\'", "R", "D"))):
                return ["B", "D\'", "R", "D"]
            elif evaluate_cross_b(do_simple_scramble(scrambled, ("U\'", "L\'", "B", "L"))):
                return ["U\'", "L\'", "B", "L"]
            elif evaluate_cross_b(do_simple_scramble(scrambled, ("U", "L\'", "B", "L"))):
                return ["U", "L\'", "B", "L"]
            else:
                return ["F", "D", "L", "D\'"]

def cross_onebyone(cube):
    e = evaluate_cross_onebyone(cube)
    solution = []
    while e < 4:
        more = cross_increase(cube, e)
        solution.append(more)
        cube = do_simple_scramble(cube, more)
        e = evaluate_cross_onebyone(cube)
    
    solution = cancellation_cross(solution)
    return cube, solution


def cancellation_cross(L):
    if len(L) < 2:
        return L
    cancel = True
    while cancel:
        cancel = False
        for i, t in enumerate(L):
            if i < len(L) - 1:
                if t[-1][0] == L[i + 1][0][0]:
                    cancel = True
                    temp = simplify(t[-1], L[i + 1][0])
                    L[i].pop(-1)
                    L[i + 1].pop(0)
                    if temp:
                        L[i].append(temp)
    return L




#FL:

def evaluate_fl(cube):
    eval = 0

    if cube[45] + cube[24] == "yg":
        eval += 1
    if cube[47] + cube[26] == "yg":
        eval += 1
    if cube[51] + cube[42] == "yb":
        eval += 1
    if cube[53] + cube[44] == "yb":
        eval += 1
    
    return eval

def fl_increase(cube):
    for i, y in enumerate((cube[9], cube[11], cube[18], cube[20], cube[27], cube[29], cube[36], cube[38], cube[0], cube[6], cube[8], cube[2], cube[15], cube[17], cube[24], cube[26], cube[33], cube[35], cube[42], cube[44], cube[51], cube[45], cube[47], cube[53])):
        if y == 'y':
            if i == 0:
                if cube[0] == 'o':
                    return ("L", "U", "L\'")
                elif cube[0] == 'g':
                    return ("U2", "L\'", "U", "L")
                elif cube[0] == 'r':
                    return ("U2", "R", "U", "R\'")
                else:
                    return ("R\'", "U", "R")
            elif i == 1:
                if cube[18] == 'o':
                    return ("U2", "L", "U\'", "L\'")
                elif cube[18] == 'g':
                    return ("L\'", "U\'", "L")
                elif cube[18] == 'r':
                    return ("R", "U\'", "R\'")
                else:
                    return ("U2", "R\'", "U\'", "R")
            elif i == 2:
                if cube[6] == 'o':
                    return ("U", "L", "U", "L\'")
                elif cube[6] == 'g':
                    return ("U\'", "L\'", "U", "L")
                elif cube[6] == 'r':
                    return ("U\'", "R", "U", "R\'")
                else:
                    return ("R\'", "U2", "R")
            elif i == 3:
                if cube[27] == 'o':
                    return ("L", "U2", "L\'")
                elif cube[27] == 'g':
                    return ("U", "L\'", "U\'", "L")
                elif cube[27] == 'r':
                    return ("U", "R", "U\'", "R\'")
                else:
                    return ("U\'", "R\'", "U\'", "R")
            elif i == 4:
                if cube[8] == 'o':
                    return ("U2", "L", "U", "L\'")
                elif cube[8] == 'g':
                    return ("L\'", "U", "L")
                elif cube[8] == 'r':
                    return ("R", "U", "R\'")
                else:
                    return ("U2", "R\'", "U", "R")
            elif i == 5:
                if cube[36] == 'o':
                    return ("L", "U\'", "L\'")
                elif cube[36] == 'g':
                    return ("U2", "L\'", "U\'", "L")
                elif cube[36] == 'r':
                    return ("U2", "R", "U\'", "R\'")
                else:
                    return ("R\'", "U\'", "R")
            elif i == 6:
                if cube[2] == 'o':
                    return ("U\'", "L", "U", "L\'")
                elif cube[2] == 'g':
                    return ("L\'", "U2", "L")
                elif cube[2] == 'r':
                    return ("U", "R", "U", "R\'")
                else:
                    return ("U\'", "R\'", "U", "R")
            elif i == 7:
                if cube[9] == 'o':
                    return ("U", "L", "U\'", "L\'")
                elif cube[9] == 'g':
                    return ("U\'", "L\'", "U\'", "L")
                elif cube[9] == 'r':
                    return ("R", "U2", "R\'")
                else:
                    return ("U", "R\'", "U\'", "R")

            elif i == 8:
                if cube[38] == 'o':
                    return ("L", "U2", "L\'", "U\'", "L", "U", "L\'")
                elif cube[38] == 'g':
                    return ("U\'", "L\'", "U2", "L", "U", "L\'", "U\'", "L")
                elif cube[38] == 'r':
                    return ("U2", "R", "U2", "R\'", "U\'", "R", "U", "R\'")
                else:
                    return ("U", "R\'", "U2", "R", "U", "R\'", "U\'", "R")
            elif i == 9:
                if cube[11] == 'o':
                    return ("U", "L", "U2", "L\'", "U\'", "L", "U", "L\'")
                elif cube[11] == 'g':
                    return ("L\'", "U2", "L", "U", "L\'", "U\'", "L")
                elif cube[11] == 'r':
                    return ("U\'", "R", "U2", "R\'", "U\'", "R", "U", "R\'")
                else:
                    return ("U2", "R\'", "U2", "R", "U", "R\'", "U\'", "R")
            elif i == 10:
                if cube[20] == 'o':
                    return ("U2", "L", "U2", "L\'", "U\'", "L", "U", "L\'")
                elif cube[20] == 'g':
                    return ("U", "L\'", "U2", "L", "U", "L\'", "U\'", "L")
                elif cube[20] == 'r':
                    return ("R", "U2", "R\'", "U\'", "R", "U", "R\'")
                else:
                    return ("U\'", "R\'", "U2", "R", "U", "R\'", "U\'", "R")
            elif i == 11:
                if cube[29] == 'o':
                    return ("U\'", "L", "U2", "L\'", "U\'", "L", "U", "L\'")
                elif cube[29] == 'g':
                    return ("U2", "L\'", "U2", "L", "U", "L\'", "U\'", "L")
                elif cube[29] == 'r':
                    return ("U", "R", "U2", "R\'", "U\'", "R", "U", "R\'")
                else:
                    return ("R\'", "U2", "R", "U", "R\'", "U\'", "R")

            elif i == 12:
                if cube[44] == 'o':
                    return ("L", "U", "L\'", "U\'", "L", "U", "L\'")
                elif cube[44] == 'g':
                    return ("L", "U2", "L2", "U", "L")
                elif cube[44] == 'r':
                    return ("L", "U2", "L\'", "R", "U", "R\'")
                else:
                    return ("L", "R\'", "U", "R", "L\'")
            elif i == 13:
                if cube[45] == 'o':
                    return ("L\'", "U\'", "L2", "U2", "L\'")
                elif cube[45] == 'g':
                    return ("L\'", "U\'", "L", "U", "L\'", "U\'", "L")
                elif cube[45] == 'r':
                    return ("L\'", "R", "U\'", "R\'", "L")
                else:
                    return ("L\'", "U2", "L", "R\'", "U\'", "R")
            elif i == 14:
                if cube[17] == 'o':
                    return ("L\'", "U", "L", "U", "L", "U", "L\'")
                elif cube[17] == 'g':
                    return ("L\'", "U", "L", "U\'", "L\'", "U", "L")
                elif cube[17] == 'r':
                    return ("L\'", "U", "L", "U\'", "R", "U", "R\'")
                else:
                    return ("L\'", "U", "L", "R\'", "U2", "R")
            elif i == 15:
                if cube[47] == 'o':
                    return ("R", "U\'", "R\'", "L", "U2", "L\'")
                elif cube[47] == 'g':
                    return ("R", "U\'", "R\'", "U", "L\'", "U\'", "L")
                elif cube[47] == 'r':
                    return ("R", "U\'", "R\'", "U", "R", "U\'", "R\'")
                else:
                    return ("R", "U\'", "R\'", "U\'", "R\'", "U\'", "R")
            elif i == 16:
                if cube[26] == 'o':
                    return ("R", "U2", "R\'", "L", "U", "L\'")
                elif cube[26] == 'g':
                    return ("R", "L\'", "U", "L", "R\'")
                elif cube[26] == 'r':
                    return ("R", "U", "R\'", "U\'", "R", "U", "R\'")
                else:
                    return ("R", "U", "R2", "U2", "R")
            elif i == 17:
                if cube[53] == 'o':
                    return ("R\'", "L", "U\'", "L\'", "R")
                elif cube[53] == 'g':
                    return ("R\'", "U\'", "R", "L\'", "U\'", "L")
                elif cube[53] == 'r':
                    return ("R\'", "U2", "R2", "U\'", "R\'")
                else:
                    return ("R\'", "U\'", "R", "U", "R\'", "U\'", "R")
            elif i == 18:
                if cube[35] == 'o':
                    return ("R\'", "U", "R", "U\'", "L", "U", "L\'")
                elif cube[35] == 'g':
                    return ("R\'", "U", "R", "L\'", "U2", "L")
                elif cube[35] == 'r':
                    return ("R\'", "U", "R", "U", "R", "U", "R\'")
                else:
                    return ("R\'", "U", "R", "U\'", "R\'", "U", "R")
            elif i == 19:
                if cube[51] == 'o':
                    return ("L", "U\'", "L\'", "U", "L", "U\'", "L\'")
                elif cube[51] == 'g':
                    return ("L", "U\'", "L\'", "U\'", "L\'", "U\'", "L")
                elif cube[51] == 'r':
                    return ("L", "U\'", "L\'", "R", "U2", "R\'")
                else:
                    return ("L", "U\'", "L\'", "U", "R\'", "U\'", "R")
                    
            if i == 20:
                if cube[15] == 'g':
                    return ("L", "U\'", "L\'", "U2", "L\'", "U", "L")
                elif cube[15] == 'r':
                    return ("L", "R", "U2", "R\'", "L\'")
                elif cube[15] == 'b':
                    return ("L", "U", "L\'", "R\'", "U\'", "R")
            if i == 21:
                if cube[24] == 'o':
                    return ("L\'", "U\'", "L", "U2", "L", "U", "L\'")
                elif cube[24] == 'r':
                    return ("L\'", "U", "L", "R", "U\'", "R\'")
                elif cube[24] == 'b':
                    return ("L\'", "U", "L", "U2", "R\'", "U\'", "R")
            if i == 22:
                if cube[33] == 'o':
                    return ("R", "L", "U2", "L\'", "R\'")
                elif cube[33] == 'g':
                    return ("R", "U\'", "R\'", "L\'", "U", "L")
                elif cube[33] == 'b':
                    return ("R", "U", "R\'", "U2", "R\'", "U\'", "R")
            if i == 23:
                if cube[42] == 'o':
                    return ("R\'", "U\'", "R", "L", "U", "L\'")
                elif cube[42] == 'g':
                    return ("R\'", "U\'", "L\'", "U2", "L\'", "U", "L")
                elif cube[42] == 'r':
                    return ("R\'", "U", "R", "U2", "R", "U\'", "R\'")

def fl(cube):
    e = evaluate_fl(cube)
    solution = []
    while e < 4:
        more = fl_increase(cube)
        solution.append(more)
        cube = do_simple_scramble(cube, more)
        e = evaluate_fl(cube)
    return cube, solution

#maybe later
        # #
        # def evaluate_fl_og(cube):
        #     if cube[45] + cube[24] == "yg":
        #         return True
        #     else:
        #         False
        # #
        # def evaluate_fl_gr(cube):
        #     if cube[47] + cube[26] == "yg":
        #         return True
        #     else:
        #         False
        # #
        # def evaluate_fl_rb(cube):
        #     if cube[51] + cube[42] == "yb":
        #         return True
        #     else:
        #         False
        # #
        # def evaluate_fl_bo(cube):
        #     if cube[53] + cube[44] == "yb":
        #         return True
        #     else:
        #         False



            #Sl:




#SL:

def evaluate_sl(cube):
    eval = 0

    if cube[12] + cube[41] == "ob":
        eval += 1
    if cube[14] + cube[21] == "og":
        eval += 1
    if cube[23] + cube[30] == "gr":
        eval += 1
    if cube[32] + cube[39] == "rb":
        eval += 1
    
    return eval

def sl_increase(cube):
    for i, y in enumerate(((cube[10] + cube[3]), (cube[19] + cube[7]), (cube[28] + cube[5]), (cube[37] + cube[1]))):
        if y == "ob":
            if i == 0:
                return ("L\'", "U\'", "L\'", "U\'", "L\'", "U", "L", "U", "L")
            elif i == 1:
                return ("B\'", "U", "B", "U", "L", "U\'", "L\'")
            elif i == 2:
                return ("U", "B\'", "U", "B", "U", "L", "U\'", "L\'")
            else:
                return ("U2", "B\'", "U", "B", "U", "L", "U\'", "L\'")
        elif y == "bo":
            if i == 0:
                return ("U2", "L", "U\'", "L\'", "U\'", "B\'", "U", "B")
            elif i == 1:
                return ("U\'", "L", "U\'", "L\'", "U\'", "B\'", "U", "B")
            elif i == 2:
                return ("L", "U\'", "L\'", "U\'", "B\'", "U", "B")
            else:
                return ("U", "L", "U\'", "L\'", "U\'", "B\'", "U", "B")
        
        elif y == "og":
            if i == 0:
                return ("U", "F", "U\'", "F\'", "U\'", "L\'", "U", "L")
            elif i == 1:
                return ("U2", "F", "U\'", "F\'", "U\'", "L\'", "U", "L")
            elif i == 2:
                return ("U\'", "F", "U\'", "F\'", "U\'", "L\'", "U", "L")
            else:
                return ("F", "U\'", "F\'", "U\'", "L\'", "U", "L")
        elif y == "go":
            if i == 0:
                return ("U2", "L\'", "U", "L", "U", "F", "U\'", "F\'")
            elif i == 1:
                return ("U\'", "L\'", "U", "L", "U", "F", "U\'", "F\'")
            elif i == 2:
                return ("L\'", "U", "L", "U", "F", "U\'", "F\'")
            else:
                return ("U", "L\'", "U", "L", "U", "F", "U\'", "F\'")
                
        elif y == "rg":
            if i == 0:
                return ("U", "F\'", "U", "F", "U", "R", "U\'", "R\'")
            elif i == 1:
                return ("U2", "F\'", "U", "F", "U", "R", "U\'", "R\'")
            elif i == 2:
                return ("U\'", "F\'", "U", "F", "U", "R", "U\'", "R\'")
            else:
                return ("F\'", "U", "F", "U", "R", "U\'", "R\'")
        elif y == "gr":
            if i == 0:
                return ("R", "U\'", "R\'", "U\'", "F\'", "U", "F")
            elif i == 1:
                return ("U", "R", "U\'", "R\'", "U\'", "F\'", "U", "F")
            elif i == 2:
                return ("U2", "R", "U\'", "R\'", "U\'", "F\'", "U", "F")
            else:
                return ("U\'", "R", "U\'", "R\'", "U\'", "F\'", "U", "F")

        elif y == "rb":
            if i == 0:
                return ("U\'", "B", "U\'", "B\'", "U\'", "R\'", "U", "R")
            elif i == 1:
                return ("B", "U\'", "B\'", "U\'", "R\'", "U", "R")
            elif i == 2:
                return ("R", "U", "R", "U", "R", "U\'", "R\'", "U\'", "R\'")
            else:
                return ("U2", "B", "U\'", "B\'", "U\'", "R\'", "U", "R")
        elif y == "br":
            if i == 0:
                return ("R\'", "U", "R", "U", "B", "U\'", "B\'")
            elif i == 1:
                return ("U", "R\'", "U", "R", "U", "B", "U\'", "B\'")
            elif i == 2:
                return ("U2", "R\'", "U", "R", "U", "B", "U\'", "B\'")
            else:
                return ("U\'", "R\'", "U", "R", "U", "B", "U\'", "B\'")

    for i, y in enumerate(((cube[12] + cube[41]), (cube[14] + cube[21]), (cube[30] + cube[23]), (cube[32] + cube[39]))):
        if y == "ob":
            if i == 1:
                return ("L2", "U2", "L2", "U2", "L2")
            elif i == 2:
                return ("R\'", "F", "R", "F\'", "R", "U", "R\'", "U2", "L", "U\'", "L\'", "U\'", "B\'", "U", "B")
            elif i == 3:
                return ("B2", "U2", "B2", "U2", "B2")
        elif y == "bo":
            if i == 0:
                return ("L", "U", "L\'", "U2", "L", "U2", "L\'", "U", "B\'", "U\'", "B")
            elif i == 1:
                return ("F", "U", "F\'", "L2", "U\'", "L\'", "U", "L2")
            elif i == 2:
                return ("R\'", "F", "R", "F\'", "R", "U", "R\'", "L\'", "U\'", "L\'", "U\'", "L\'", "U", "L", "U", "L")
            else:
                return ("R\'", "U\'", "R", "F\'", "B2", "U", "B", "U\'", "B2")

        elif y == "og":
            if i == 0:
                return ("L2", "U2", "L2", "U2", "L2")
            elif i == 2:
                return ("F2", "U2", "F2", "U2", "F2")
            elif i == 3:
                return ("B", "U", "B\'", "U\'", "R\'", "U\'", "R", "U2", "L\'", "U", "L", "U", "F", "U\'", "F\'")
        elif y == "go":
            if i == 0:
                return ("B\'", "U\'", "B", "L2", "U", "L", "U\'", "L2")
            elif i == 1:
                return ("F", "U\'", "F\'", "U", "L\'", "U2", "L", "U2", "L\'", "U", "L")
            elif i == 2:
                return ("R\'", "u\'", "R", "u", "F", "R", "F\'")
            else:
                return ("R", "B\'", "R\'", "B", "R\'", "U\'", "R", "U", "F", "U\'", "F\'", "U\'", "L\'", "U", "L")
            
        elif y == "rg":
            if i == 0:
                return ("L2", "U2", "L2", "U2", "L2", "E\'", "L2", "E", "L2")
            elif i == 1:
                return ("F2", "U2", "F2", "U2", "F2")
            elif i == 3:
                return ("R2", "U2", "R2", "U2", "R2")
        elif y == "gr":
            if i == 0:
                return ("B\'", "U\'", "B", "U", "L", "U", "L\'", "U\'", "F\'", "U", "F", "U", "R", "U\'", "R\'")
            elif i == 1:
                return ("L", "u", "L\'", "u\'", "F\'", "L\'", "F")
            elif i == 2:
                return ("R\'", "F", "R", "F\'", "R", "U\'", "R\'", "U", "R", "U\'", "R\'", "U2", "R", "U\'", "R\'")
            else:
                return ("B", "U", "B\'", "U\'", "R\'", "U\'", "R", "U", "F\'", "U", "F", "U", "R", "U\'", "R\'")

        elif y == "rb":
            if i == 0:
                return ("B2", "U2", "B2", "U2", "B2")
            elif i == 1:
                return ("R2", "U2", "R2", "U2", "R2", "E", "R2", "E\'", "R2")
            elif i == 2:
                return ("R2", "U2", "R2", "U2", "R2")
        elif y == "br":
            if i == 0:
                return ("L\'", "u\'", "L", "u", "B", "L", "B\'")
            elif i == 1:
                return ("L\'", "R\'", "M2", "U", "M2", "U2", "M2", "U", "M2", "R", "L")
            elif i == 2:
                return ("R\'", "F", "R", "F\'", "R", "U", "R\'", "U2", "R", "U", "R", "U", "R", "U\'", "R\'", "U\'", "R\'")
            else:
                return ("R", "B\'", "R\'", "B", "R", "U2", "R2", "U\'", "R2", "U\'", "R\'")

def sl(cube):
    e = evaluate_sl(cube)
    solution = []
    while e < 4:
        more = sl_increase(cube)
        solution.append(more)
        cube = do_any_scramble(cube, more)
        e = evaluate_sl(cube)
    return cube, solution




#OLL:

def evaluate_oll(cube):
    if cube[1] == cube[3] == cube[5] == cube[7]:
        if cube[0] == cube[2] == cube[4] == cube[6]:
            return 0
        else:
            return 10
    elif cube[1] == cube[3]:
        return 1
    elif cube[7] == cube[3]:
        return 2
    elif cube[7] == cube[5]:
        return 3
    elif cube[1] == cube[5]:
        return 4
    elif cube[5] == cube[3]:
        return 5
    elif cube[1] == cube[7]:
        return 6
    else:
        return 7


def oll_10(cube):
    #if cube[1] == cube[3] == cube[7] == cube[5] == 'w':
        if cube[0] == 'w':
            if cube[2] == 'w':
                if cube[11] == 'w':
                    return ("l", "U", "R\'", "D", "R", "U\'", "l\'", "F\'")
                else:
                    return ("R2", "D", "R\'", "U2", "R", "D\'", "R\'", "U2", "R\'")
            elif cube[6] == 'w':
                if cube[20] == 'w':
                    return ("U", "l", "U", "R\'", "D", "R", "U\'", "l\'", "F\'")
                else:
                    return ("U\'", "R2", "D\'", "R", "U2", "R\'", "D", "R", "U2", "R")
            elif cube[8] == 'w':
                if cube[11] == 'w':
                    return ("x\'", "D", "R", "U", "R\'", "D\'", "R", "U\'", "l\'")
                else:
                    return ("l\'", "U", "R", "D\'", "R\'", "U\'", "l", "B")
            elif cube[11] == 'w':
                return ("L\'", "U2", "L", "U", "L\'", "U", "L")
            else:
                return ("R\'", "U\'", "R", "U\'", "R\'", "U2", "R")
        elif cube[2] == 'w':
            if cube[8] == 'w':
                if cube[18] == 'w':
                    return ("U\'", "l", "U", "R\'", "D", "R", "U\'", "l\'", "F\'")
                else:
                    return ("U\'", "R2", "D", "R\'", "U2", "R", "D\'", "R\'", "U2", "R\'")
            if cube[6] == 'w':
                if cube[38] == 'w':
                    return ("l", "U\'", "R\'", "D", "R", "U", "l\'", "F\'")
                else:
                    return ("U", "x\'", "D", "R", "U", "R\'", "D\'", "R", "U\'", "l\'")
            elif cube[38] == 'w':
                return ("L", "U", "L\'", "U", "L", "U2", "L\'")
            else:
                return ("R", "U2", "R\'", "U\'", "R", "U\'", "R\'")
        elif cube[6] == 'w':
            if cube[8] == 'w':
                if cube[38] == 'w':
                    return ("R2", "D\'", "R", "U2", "R\'", "D", "R", "U2", "R")
                else:
                    return ("U2", "l", "U", "R\'", "D", "R", "U\'", "l\'", "F\'")
            elif cube[38] == 'w':
                return ("R", "U", "R\'", "U", "R", "U2", "R\'")
            else:
                return ("L", "U2", "L\'", "U\'", "L", "U\'", "L\'")
        elif cube[8] == 'w':
            if cube[38] == 'w':
                return ("R\'", "U2", "R", "U", "R\'", "U", "R")
            else:
                return ("L\'", "U\'", "L", "U\'", "L\'", "U2", "L")
        else:
            if cube[9] == cube[36] == 'w':
                return ("R", "U2", "R2", "U\'", "R2", "U\'", "R2", "U2", "R")
            elif cube[36] == cube[27] == 'w':
                return ("U\'", "R", "U2", "R2", "U\'", "R2", "U\'", "R2", "U2", "R")
            elif cube[27] == cube[18] == 'w':
                return ("U2", "R", "U2", "R2", "U\'", "R2", "U\'", "R2", "U2", "R")
            elif cube[18] == cube[9] == 'w':
                return ("U", "R", "U2", "R2", "U\'", "R2", "U\'", "R2", "U2", "R")
            else:
                if cube[9] == 'w':
                    return ("R\'", "U\'", "R", "U\'", "R\'", "U", "R", "U\'", "R\'", "U2", "R")
                else:
                    return ("R", "U2", "R\'", "U\'", "R", "U", "R\'", "U\'", "R", "U\'", "R\'")

def oll_1(cube):
    if cube[0] == 'w':
        if cube[2] == 'w':
            if cube[6] == 'w':
                return ("M", "U", "M\'", "U2", "M", "U", "M\'")
            else:
                if cube[11] == 'w':
                    return ("U", "R\'", "U\'", "F", "U", "R", "U\'", "R\'", "F\'", "R")
                else:
                    return ("R\'", "U\'", "F\'", "U", "F", "R")
        elif cube[6] == 'w':
            if cube[29] == 'w':
                return ("F", "U", "R", "U\'", "R\'", "F\'")
            else:
                return ("L", "U", "F\'", "U\'", "L\'", "U", "L", "F", "L\'")
        elif cube[8] == 'w':
            if cube[18] == 'w':
                return ("F", "R", "U\'", "R\'", "U\'", "R", "U", "R\'", "F\'")
            else:
                return ("U2", "R", "U2", "R2", "F", "R", "F\'", "R", "U2", "R\'")
        else:
            if cube[18] == 'w':
                return ("U", "r", "U2", "R\'", "U\'", "R", "U\'", "r\'")
            else:
                return ("l\'", "U2", "L", "U", "L\'", "U", "l")
    elif cube[2] == 'w':
        if cube[6] == 'w':
            if cube[27] == 'w':
                return ("R", "U", "R\'", "U", "R", "U\'", "R\'", "U\'", "R\'", "F", "R", "F\'")
            else:
                return ("U", "L\'", "U\'", "L", "U\'", "L\'", "U", "L", "U", "L", "F\'", "L\'", "F")
        elif cube[8] == 'w':
            if cube[18] == 'w':
                return ("R", "U", "R\'", "U\'", "R", "U\'", "R\'", "F\'", "U\'", "F", "R", "U", "R\'")
            else:
                return ("U\'", "R\'", "U\'", "R", "U\'", "R\'", "U2", "R", "F", "R", "U", "R\'", "U\'", "F\'")
        else:
            if cube[18] == 'w':
                return ("U", "l\'", "U\'", "L", "U\'", "L\'", "U2", "l")
            else:
                return ("U2", "r\'", "R2", "U", "R\'", "U", "R", "U2", "R\'", "U", "M\'")
    elif cube[6] == 'w':
        if cube[8] == 'w':
            if cube[36] == 'w':
                return ("R", "U", "R\'", "U", "R", "U2", "R\'", "F", "R", "U", "R\'", "U\'", "F\'")
            else:
                return ("F", "R\'", "F", "R2", "U\'", "R\'", "U\'", "R", "U", "R\'", "F2")
        else:
            if cube[29] == 'w':
                return ("r", "U", "R\'", "U", "R", "U2", "r\'")
            else:
                return ("U2", "F", "R", "U", "R\'", "U\'", "F\'", "U", "F", "R", "U", "R\'", "U\'", "F\'")
    elif cube[8] == 'w':
        if cube[9] == 'w':
            return ("R", "U", "R\'", "U\'", "R\'", "F", "R2", "U", "R\'", "U\'", "F\'")
        else:
            return ("U\'", "R", "U", "R\'", "U", "R\'", "F", "R", "F\'", "R", "U2", "R\'")
    else:
        if cube[9] == 'w':
            if cube[11] == 'w':
                if cube[20] == 'w':
                    return ("F", "R", "U", "R\'", "U\'", "R", "U", "R\'", "U\'", "F\'")
                else:
                    return ("l\'", "U\'", "L", "U\'", "L\'", "U", "L", "U\'", "L\'", "U2", "l")
            else:
                return ("U", "r", "U\'", "r2", "U", "r2", "U", "r2", "U\'", "r")
        else:
            if cube[11] == 'w':
                return ("U", "F\'", "L\'", "U\'", "L", "U", "L\'", "U\'", "L", "U", "F")
            else:
                if cube[29] == 'w':
                    return ("U2", "r\'", "U", "r2", "U\'", "r2", "U\'", "r2", "U", "r\'")
                else:
                    return ("r", "U2", "R\'", "U\'", "R", "U", "R\'", "U\'", "R", "U\'", "r\'")

def oll_5(cube):
    if cube[0] == 'w':
        if cube[2] == 'w':
            if cube[6] == 'w':
                return ("R", "U", "R\'", "U\'", "M\'", "U", "R", "U\'", "r\'")
            else:
                if cube[18] == 'w':
                    return ("U\'", "R\'", "U\'", "R\'", "F", "R", "F\'", "U", "R")
                else:
                    return ("U2", "R", "U", "R2", "U\'", "R\'", "F", "R", "U", "R", "U\'", "F\'")
        if cube[6] == 'w':
            if cube[20] == 'w':
                return ("U2", "R", "U", "R\'", "U\'", "R\'", "F", "R", "F\'")
            else:
                return ("U2", "F", "R", "U", "R\'", "U\'", "F\'")
        if cube[8] == 'w':
            if cube[11] == 'w':
                return ("R\'", "F", "R", "U", "R\'", "U\'", "F\'", "U", "R")
            else:
                return ("U2", "R\'", "F", "R", "U", "R\'", "U\'", "F\'", "U", "R")
        else:
            if cube[18] == 'w':
                return ("U2", "R\'", "F", "R", "U", "R\'", "F\'", "R", "F", "U\'", "F\'")
            else:
                return ("l\'", "U\'", "M", "U\'", "L", "U", "l\'", "U", "l")
    if cube[0] != 'w' != cube[2] and cube[6] != 'w' != cube[8]:
        if cube[9] == 'w':
            if cube[36] == 'w':
                return ("f", "R", "U", "R\'", "U\'", "R", "U", "R\'", "U\'", "f\'")
            else:
                if cube[18] == 'w':
                    return ("U\'", "R\'", "U\'", "R", "U\'", "R\'", "d", "R\'", "U", "R", "B")
                else:
                    return ("F", "R", "U", "R\'", "U\'", "F\'", "r", "U", "R\'", "U\'", "r\'", "F", "R", "F\'")
        if cube[20] == 'w':
            return ("R\'", "F", "R", "U", "R", "U\'", "R2", "F\'", "R2", "U\'", "R\'", "U", "R", "U", "R\'")
        if cube[27] == cube[29] == cube[4]:
            return ("F", "U", "R", "U\'", "R\'", "U", "R", "U\'", "R\'", "F\'")
    if cube[2] == cube[9] == cube[18]:
        return ("r", "U", "M", "U", "R\'", "U\'", "r", "U\'", "r\'")
    if cube[2] == cube[11] == cube[20]:
        return ("U2", "F", "U", "R", "U2", "R\'", "U\'", "R", "U", "R\'", "F\'")
    if cube[2] == cube[6] == 'w':
        if cube[9] == 'w':
            return ("U2", "L", "F\'", "L\'", "U\'", "L", "U", "F", "U\'", "L\'")
        else:
            return ("L", "F\'", "L\'", "U\'", "L", "U", "F", "U\'", "L\'")
    else:
        solution = ["U2"] + list(oll_5(do_simple_scramble(cube, ["U2"])))
        return solution

def oll_7(cube):
    if cube[0] == cube[2] == cube[6]:
        return ("M", "U", "R", "U", "R\'", "U\'", "M2", "U", "R", "U\'", "r\'")
    if cube[0] == 'w':
        if cube[2] == 'w':
            if cube[18] == 'w':
                return ("U", "R", "U2", "R2", "F", "R", "F\'", "U2", "M\'", "U", "R", "U\'", "r\'")
            else:
                return ("M", "U", "R", "U", "R\'", "U\'", "M\'", "R\'", "F", "R", "F\'")
        elif cube[8] == 'w':
            if cube[11] == 'w':
                return ("R", "U", "R\'", "U", "R\'", "F", "R", "F\'", "U2", "R\'", "F", "R", "F\'")
            else:
                return ("U2", "R", "U", "R\'", "U", "R\'", "F", "R", "F\'", "U2", "R\'", "F", "R", "F\'")
        elif cube[6] != cube[4]:
            if cube[11] == 'w':
                return ("U2", "f", "R", "U", "R\'", "U\'", "f\'", "U\'", "F", "R", "U", "R\'", "U\'", "F\'")
            else:
                return ("U", "f", "R", "U", "R\'", "U\'", "f\'", "U", "F", "R", "U", "R\'", "U\'", "F\'")
    if (cube[0] != 'w' != cube[2] and cube[6] != 'w' != cube[8]) and cube[9] == cube[11] == 'w':
        if cube[29] == 'w':
            return ("R", "U2", "R2", "F", "R", "F\'", "U2", "R\'", "F", "R", "F\'")
        else:
            return ("F", "R", "U", "R\'", "U\'", "F\'", "f", "R", "U", "R\'", "U\'", "f\'")
    else:
        solution = ["U"] + list(oll_7(scramble_move(cube, "U")))
        return solution
    

def oll(cube):
    e = evaluate_oll(cube)
    if not e:
        return cube, tuple()

    if e == 10:
        solution = oll_10(cube)
    elif e == 1:
        solution = oll_1(cube)
    elif e == 2:
        solution = ["U"] + list(oll_1(do_simple_scramble(cube, ["U"])))        
    elif e == 3:
        solution = ["U2"] + list(oll_1(do_simple_scramble(cube, ["U2"])))
    elif e == 4:
        solution = ["U\'"] + list(oll_1(do_simple_scramble(cube, ["U\'"])))
    elif e == 5:
        solution = oll_5(cube)
    elif e == 6:
        solution = ["U"] + list(oll_5(do_simple_scramble(cube, ["U"])))
    else:
        solution = oll_7(cube)
    
    cancellation_oll(solution)
    cube = do_any_scramble(cube, solution)
    if evaluate_oll(cube):
        raise Exception("Wrong oll solution:", str(solution))
    return cube, solution


def cancellation_oll(L):
    while L[0][0] == L[1][0]:
        temp = simplify(L[0], L[1])
        if temp:
            L.insert(2, simplify(L[0], L[1]))
        L.pop(0)
        L.pop(0)




#PLL:

def evaluate_pll(cube):
    if cube[9] == cube[10] == cube[11] and cube[18] == cube[19] == cube[20]:
        return 0

    if cube[9] == cube[11] and cube[18] == cube[20] and cube[27] == cube[29] and cube[36] == cube[38]:
        return 1 #edges only: U, H, Z

    if cube[10] + cube[19] + cube[28] + cube[37] == 'ogrb' or cube[19] + cube[28] + cube[37] + cube[10] == 'ogrb' or cube[28] + cube[37] + cube[10] + cube[19] == 'ogrb' or cube[37] + cube[10] + cube[19] + cube[28] == 'ogrb':
        return 2 #corners only: A, E

    if cube[9] == cube[10] == cube[11]:
        return 30 #bar: J, F
    if cube[18] == cube[19] == cube[20]:
        return 31
    if cube[27] == cube[28] == cube[29]:
        return 32
    if cube[36] == cube[37] == cube[38]:
        return 33

    if cube[10] == cube[20] == cube[36] and cube[18] == cube[19]:
        return 40 #T, Y
    if cube[19] == cube[9] == cube[29] and cube[27] == cube[28]:
        return 41
    if cube[28] == cube[18] == cube[38] and cube[36] == cube[37]:
        return 42
    if cube[37] == cube[27] == cube[11] and cube[9] == cube[10]:
        return 43

    if cube[18] == cube[19] == cube[38] and cube[20] == cube[36] == cube[37]:
        return 50 #N1
    if cube[19] == cube[20] == cube[36] and cube[37] == cube[38] == cube[18]:
        return 51 #N2

    if cube[18] == cube[19] == cube[38] and cube[10] == cube[11] == cube[27]:
        return 60 #V
    if cube[27] == cube[28] == cube[11] and cube[19] == cube[20] == cube[36]:
        return 61
    if cube[36] == cube[37] == cube[20] and cube[28] == cube[29] == cube[9]:
        return 62
    if cube[9] == cube[10] == cube[29] and cube[37] == cube[38] == cube[18]:
        return 63

    if cube[9] == cube[29] == cube[37]:
        return 70 #R
    if cube[18] == cube[38] == cube[10]:
        return 71
    if cube[27] == cube[11] == cube[19]:
        return 72
    if cube[36] == cube[20] == cube[28]:
        return 73

    else:
        return 80 #G

def find_pll(cube, e):
    if e == 0:
        return ()
    
    if e == 1:
        if cube[9] == cube[10]:
            if cube[19] == cube[36]:
                return ("U\'", "R\'", "U", "R\'", "U\'", "R\'", "U\'", "R\'", "U", "R", "U", "R2")
            else:
                return ("U\'", "R2", "U\'", "R\'", "U\'", "R", "U", "R", "U", "R", "U\'", "R")
        elif cube[18] == cube[19]:
            if cube[28] == cube[9]:
                return ("R\'", "U", "R\'", "U\'", "R\'", "U\'", "R\'", "U", "R", "U", "R2")
            else:
                return ("R2", "U\'", "R\'", "U\'", "R", "U", "R", "U", "R", "U\'", "R")
        elif cube[27] == cube[28]:
            if cube[37] == cube[18]:
                return ("U\'", "R2", "U", "R", "U", "R\'", "U\'", "R\'", "U\'", "R\'", "U", "R\'")
            else:
                return ("U\'", "R", "U\'", "R", "U", "R", "U", "R", "U\'", "R\'", "U\'", "R2")
        elif cube[36] == cube[37]:
            if cube[10] == cube[27]:
                return ("R2", "U", "R", "U", "R\'", "U\'", "R\'", "U\'", "R\'", "U", "R\'")
            else:
                return ("R", "U\'", "R", "U", "R", "U", "R", "U\'", "R\'", "U\'", "R2")

        elif cube[10] == cube[29]:
            return ("M2", "U", "M2", "U2", "M2", "U", "M2")

        elif cube[10] == cube[38]:
            return ("M2", "U", "M2", "U", "M\'", "U2", "M2", "U2", "M\'")
        else:
            return ("M\'", "U2", "M2", "U2", "M\'", "U", "M2", "U", "M2")

    if e == 2:
        if cube[10] == cube[11]:
            if cube[27] == cube[29]:
                return ("R2", "B2", "R", "F", "R\'", "B2", "R", "F\'", "R")
            else:
                return ("R\'", "F", "R\'", "B2", "R", "F\'", "R\'", "B2", "R2")
        elif cube[19] == cube[20]:
            if cube[36] == cube[38]:
                return ("U", "R2", "B2", "R", "F", "R\'", "B2", "R", "F\'", "R")
            else:
                return ("U", "R\'", "F", "R\'", "B2", "R", "F\'", "R\'", "B2", "R2")
        elif cube[28] == cube[29]:
            if cube[9] == cube[11]:
                return ("U2", "R2", "B2", "R", "F", "R\'", "B2", "R", "F\'", "R")
            else:
                return ("U2", "R\'", "F", "R\'", "B2", "R", "F\'", "R\'", "B2", "R2")
        elif cube[37] == cube[38]:
            if cube[18] == cube[20]:
                return ("U\'", "R2", "B2", "R", "F", "R\'", "B2", "R", "F\'", "R")
            else:
                return ("U\'", "R\'", "F", "R\'", "B2", "R", "F\'", "R\'", "B2", "R2")

        elif cube[18] == cube[38] == cube[10]:
            return ("l", "U\'", "R\'", "D", "R", "U", "R\'", "D\'", "R", "U", "R\'", "D", "R", "U\'", "R\'", "D\'", "x")
        else:
            return ("U", "l", "U\'", "R\'", "D", "R", "U", "R\'", "D\'", "R", "U", "R\'", "D", "R", "U\'", "R\'", "D\'", "x")

    if e < 40:
        if e == 30:
            if cube[18] == cube[19]:
                return ("U\'", "R\'", "U", "L\'", "U2", "R", "U\'", "R\'", "U2", "R", "L")
            elif cube[37] == cube[38]:
                return ("R", "U", "R\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'")
            else:
                return ("R\'", "U\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'", "U\'", "R", "U", "R\'", "U", "R")        

        if e == 31:
            if cube[27] == cube[28]:
                return ("R\'", "U", "L\'", "U2", "R", "U\'", "R\'", "U2", "R", "L")
            elif cube[10] == cube[11]:
                return ("U", "R", "U", "R\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'")
            else:
                return ("U", "R\'", "U\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'", "U\'", "R", "U", "R\'", "U", "R")        

        if e == 32:
            if cube[36] == cube[37]:
                return ("U", "R\'", "U", "L\'", "U2", "R", "U\'", "R\'", "U2", "R", "L")
            elif cube[19] == cube[20]:
                return ("U2", "R", "U", "R\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'")
            else:
                return ("U2", "R\'", "U\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'", "U\'", "R", "U", "R\'", "U", "R")        

        else:
            if cube[9] == cube[10]:
                return ("U2", "R\'", "U", "L\'", "U2", "R", "U\'", "R\'", "U2", "R", "L")
            elif cube[28] == cube[29]:
                return ("U\'", "R", "U", "R\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'")
            else:
                return ("U\'", "R\'", "U\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'", "U\'", "R", "U", "R\'", "U", "R")        

    if e < 50:
        if e == 40:
            if cube[28] == cube[29]:
                return ("F", "R", "U\'", "R\'", "U\'", "R", "U", "R\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R", "F\'")
            else:
                return ("R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'", "U\'", "R", "U", "R\'", "F\'")
        elif e == 41:
            if cube[37] == cube[38]:
                return ("U", "F", "R", "U\'", "R\'", "U\'", "R", "U", "R\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R", "F\'")
            else:
                return ("U", "R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'", "U\'", "R", "U", "R\'", "F\'")
        elif e == 42:
            if cube[10] == cube[11]:
                return ("U2", "F", "R", "U\'", "R\'", "U\'", "R", "U", "R\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R", "F\'")
            else:
                return ("U2", "R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'", "U\'", "R", "U", "R\'", "F\'")
        else:
            if cube[19] == cube[20]:
                return ("U\'", "F", "R", "U\'", "R\'", "U\'", "R", "U", "R\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R", "F\'")
            else:
                return ("U\'", "R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'", "U\'", "R", "U", "R\'", "F\'")

    if e == 50:
        return ("R\'", "U", "R", "U\'", "R\'", "F\'", "U\'", "F", "R", "U", "R\'", "F", "R\'", "F\'", "R", "U\'", "R")
    if e == 51:
        return ("R", "U", "R\'", "U", "R", "U", "R\'", "F\'", "R", "U", "R\'", "U\'", "R\'", "F", "R2", "U\'", "R\'", "U2", "R", "U\'", "R\'")

    if e < 70:
        if e == 60:
            return ("R\'", "U", "R\'", "d\'", "R\'", "F\'", "R2", "U\'", "R\'", "U", "R\'", "F", "R", "F")
        elif e == 61:
            return ("U", "R\'", "U", "R\'", "d\'", "R\'", "F\'", "R2", "U\'", "R\'", "U", "R\'", "F", "R", "F")
        elif e == 62:
            return ("U2", "R\'", "U", "R\'", "d\'", "R\'", "F\'", "R2", "U\'", "R\'", "U", "R\'", "F", "R", "F")
        else:
            return ("U\'", "R\'", "U", "R\'", "d\'", "R\'", "F\'", "R2", "U\'", "R\'", "U", "R\'", "F", "R", "F")

    if e < 80:
        if e == 70:
            if cube[10] == cube[11]:
                return ("R\'", "U2", "R", "U2", "R\'", "F", "R", "U", "R\'", "U\'", "R\'", "F\'", "R2")
            else:
                return ("U", "R", "U\'", "R\'", "U\'", "R", "U", "R", "D", "R\'", "U\'", "R", "D\'", "R\'", "U2", "R\'")
        elif e == 71:
            if cube[19] == cube[20]:
                return ("U", "R\'", "U2", "R", "U2", "R\'", "F", "R", "U", "R\'", "U\'", "R\'", "F\'", "R2")
            else:
                return ("U2", "R", "U\'", "R\'", "U\'", "R", "U", "R", "D", "R\'", "U\'", "R", "D\'", "R\'", "U2", "R\'")
        elif e == 72:
            if cube[28] == cube[29]:
                return ("U2", "R\'", "U2", "R", "U2", "R\'", "F", "R", "U", "R\'", "U\'", "R\'", "F\'", "R2")
            else:
                return ("U\'", "R", "U\'", "R\'", "U\'", "R", "U", "R", "D", "R\'", "U\'", "R", "D\'", "R\'", "U2", "R\'")
        else:
            if cube[37] == cube[38]:
                return ("U\'", "R\'", "U2", "R", "U2", "R\'", "F", "R", "U", "R\'", "U\'", "R\'", "F\'", "R2")
            else:
                return ("R", "U\'", "R\'", "U\'", "R", "U", "R", "D", "R\'", "U\'", "R", "D\'", "R\'", "U2", "R\'")

    else:
        if cube[19] == cube[20]:
            if cube[36] == cube[19]:
                return ("R2", "u", "R\'", "U", "R\'", "U\'", "R", "u\'", "R2", "F\'", "U", "F")
            else:
                return ("F\'", "U\'", "F", "R2", "u", "R\'", "U", "R", "U\'", "R", "u\'", "R2")
        elif cube[28] == cube[29]:
            if cube[9] == cube[28]:
                return ("U", "R2", "u", "R\'", "U", "R\'", "U\'", "R", "u\'", "R2", "F\'", "U", "F")
            else:
                return ("R\'", "U\'", "R", "U", "D\'", "R2", "U", "R\'", "U", "R", "U\'", "R", "U\'", "R2", "D")
        elif cube[37] == cube[38]:
            if cube[18] == cube[37]:
                return ("U2", "R2", "u", "R\'", "U", "R\'", "U\'", "R", "u\'", "R2", "F\'", "U", "F")
            else:
                return ("U", "R\'", "U\'", "R", "U", "D\'", "R2", "U", "R\'", "U", "R", "U\'", "R", "U\'", "R2", "D")
        elif cube[10] == cube[11]:
            if cube[27] == cube[10]:
                return ("U\'", "R2", "u", "R\'", "U", "R\'", "U\'", "R", "u\'", "R2", "F\'", "U", "F")
            else:
                return ("U\'", "F\'", "U\'", "F", "R2", "u", "R\'", "U", "R", "U\'", "R", "u\'", "R2")

        elif cube[36] == cube[37]:
            if cube[20] == cube[36]:
                return ("R2", "u\'", "R", "U\'", "R", "U", "R\'", "u", "R2", "f", "R\'", "f\'")
            else:
                return ("f", "R", "f\'", "R2", "u\'", "R", "U\'", "R\'", "U", "R\'", "u", "R2")
        elif cube[9] == cube[10]:
            if cube[29] == cube[9]:
                return ("U", "R2", "u\'", "R", "U\'", "R", "U", "R\'", "u", "R2", "f", "R\'", "f\'")
            else:
                return ("L", "U", "L\'", "B2", "D\'", "R", "U\'", "R\'", "U", "R\'", "u", "R2")
        elif cube[18] == cube[19]:
            if cube[38] == cube[18]:
                return ("U2", "R2", "u\'", "R", "U\'", "R", "U", "R\'", "u", "R2", "f", "R\'", "f\'")
            else:
                return ("U\'", "R", "U", "R\'", "y\'", "R2", "u\'", "R", "U\'", "R\'", "U", "R\'", "u", "R2")
        else:
            if cube[11] == cube[27]:
                return ("U\'", "R2", "u\'", "R", "U\'", "R", "U", "R\'", "u", "R2", "f", "R\'", "f\'")
            else:
                return ("R", "U", "R\'", "y\'", "R2", "u\'", "R", "U\'", "R\'", "U", "R\'", "u", "R2")

def auf(cube):
    if cube[9] == cube[13]:
        return []
    elif cube[9] == cube[22]:
        return ["U\'"]
    elif cube[9] == cube[31]:
        return ["U2"]
    else:
        return ["U"]


def pll(cube):
    solution = find_pll(cube, evaluate_pll(cube))
    if solution:
        cube = do_any_scramble(cube, solution)

    if evaluate_pll(cube):
        raise Exception("Wrong pll solution:", str(solution))

    a = auf(cube)
    if a:
        solution = list(solution) + a
        cube = do_simple_scramble(cube, a)
    return cube, solution





def simplify(m1, m2):
    if len(m1) == 1:
        if len(m2) == 1:
            return m1 + "2"
        if m2[1] == "\'":
            return []
        else:
            return m1 + "\'"
    
    if m1[1] == "\'":
        if len(m2) == 1:
            return []
        if m2[1] == "\'":
            return m1[0] + "2"
        else:
            return m1[0]

    else:
        if len(m2) == 1:
            return m1 + "\'"
        if m2[1] == "\'":
            return m1[0]
        else:
            return []

def solve(cube):

    start = time.time()
    cube, s_cross = cross_onebyone(cube)
    end = time.time()
    print("\nCross found in " + str(end-start) + " s")
    for i, ms in enumerate(s_cross):
        if i != 0:
            print(", ", end='')
        print("(" + ms[0] + ''.join(", " + m for m in ms[1:]) + ")", end='')

    start = time.time()
    cube, s_fl = fl(cube)
    end = time.time()
    print("\n\nFirst layer found in " + str(end-start) + " s")
    for i, ms in enumerate(s_fl):
        if i != 0:
            print(", ", end='')
        print("(" + ms[0] + ''.join(", " + m for m in ms[1:]) + ")", end='')

    start = time.time()
    cube, s_sl = sl(cube)
    end = time.time()
    print("\n\nSecond layer found in " + str(end-start) + " s")
    for i, ms in enumerate(s_sl):
        if i != 0:
            print(", ", end='')
        print("(" + ms[0] + ''.join(", " + m for m in ms[1:]) + ")", end='')

    start = time.time()
    cube, s_oll = oll(cube)
    end = time.time()
    print("\n\nOLL found in " + str(end-start) + " s")
    print("(" + s_oll[0] + ''.join(", " + m for m in s_oll[1:]) + ")")

    start = time.time()
    cube, s_pll = pll(cube)
    end = time.time()
    print("\nPLL found in " + str(end-start) + " s")
    print("(" + s_pll[0] + ''.join(", " + m for m in s_pll[1:]) + ")")

    print()
    print(cube)




if __name__ == "__main__":
#  correct = 0
#  while correct < 10:
    mix = generate_scramble(n=25)
    mixed_cube = do_simple_scramble(solved, mix)

    solve(mixed_cube)
    # correct += 1
    # print(correct)
