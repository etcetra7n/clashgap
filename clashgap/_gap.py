# This file contains the clashgap implementation
# and all the functions required for the clashgap function

def list_has(arr, index):
    return (len(arr) > index)

def collision(arr, brr):
    for i in range(len(arr)):
        collision = brr.find(arr[i])
        if collision != -1:
            return i, collision
    return -1, 0

def gap(clash):
    res = []
    buff = ['', '']
    for i in range(len(clash[0])):
        buff[0] += clash[0][i]
        if list_has(clash[1], i):
            buff[1] += clash[1][i]

        o, l = collision(buff[0], buff[1])

        if o != -1:
            if buff[0][:o] or buff[1][:l]:
                res += [[buff[0][:o], buff[1][:l]], buff[1][l]]
            elif (len(res) == 0) or (type(res[-1]) is list):
                res += buff[1][l]
            else:
                res[-1] += buff[1][l]

            buff[0] = buff[0][o+1:]
            buff[1] = buff[1][l+1:]

    if buff[0] or buff[1]:
        res.append(buff)

    return res


