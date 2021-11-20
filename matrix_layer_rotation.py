'''
This function will break down a matrix into a list of lists where the first list represents
the matrix outer layer starting from (0,0) and going clockwise, and the next list represents
the next layer.
This is basically done by fist taking the top and bottom rows of the matrix, then transposing
the matrix and taking the top en bottom rows again. And make a new list of these rows in the 
correct order.

    00000 <- a = row[0]                     00 <- c = row[0]
    01110                   -> transpose    11
    01110                      the rest of  11                  -> [a,d, rev(b), rev(c)]
    00000 <- b = row[-1]       the matrix:  11
                                            00 <- d = row[-1]
'''
def matrix_to_layers(g):
    layers = []
    while len(g) > 0: # for _ in range(len(g)): 
        if len(g) == 1: 
            # this case will only occur for odd square matrices eg 5x5
            # where the center element is a 1x1 matrix
            layers.append(g[0]) 
            break
        else:
            a, b = g[0], list(reversed(g[-1]))
            g = T(g[1:-1])

            if g == []:
                c = d = []
            else:
                c, d = list(reversed(g[0])), g[-1]
                g = T(g[1:-1])

            layers.append([*a,*d,*b,*c]) 
    
    return layers

''' This function will rotate each list a given number of steps. '''
def rotate_lists(xs, rot):
    ys = []
    for x in xs:
        rot = rot % len(x)
        ys.append(x[rot:] + x[:rot])
    return ys

''' This function will transpose a matrix represented as a list of lists. '''
def T(m):
    return list(map(list, zip(*m)))

'''
This function will take a list of matrix layers and rebuild the matrix.
It will basically start with the inner most layer and fold it in half to make a 2xN matrix. 
Then for the next layer (which will wrap around this layer) we calculate the length of each 
part (similarly to the matrix_to_layer function), chop up the layer in to it's parts and
apply the same technique backwards, i.e. add the top and bottom row, transpose and add the 
left and right column and transpose again, to have the correct orientation.
'''
def layers_to_matrix(layers, input_matrix):
    m,n = len(input_matrix), len(input_matrix[0])

    matrix = []
    for x in reversed(layers):
        if len(x) == 1:
            matrix.append(x)
        elif matrix == [] and m <= n:
            matrix.append(x[:len(x)//2])
            matrix.append(list(reversed(x[len(x)//2:])))
        else:
            if matrix == [] and m > n:
                u, v =  len(x)//2 - 2, 2
            else:
                u, v =  len(matrix), len(matrix[0]) + 2

            a, b, c, d = x[:v], x[v: v+u], list(reversed(x[v+u: 2*v+u])), list(reversed(x[2*v+u:]))
            matrix = [d] + T(matrix) + [b]
            matrix = [a] + T(matrix) + [c]
    
    # print('----')
    # print(*m2, sep='\n')
    for a in matrix:
        print(*a)


if __name__ == '__main__':

    g_7x4 = [[ 0, 1, 2, 3],
             [ 4, 5, 6, 7],
             [ 8, 9,10,11],
             [12,13,14,15],
             [16,17,18,19],
             [20,21,22,23],
             [24,22,25,26]]

    g_8x4 = [[0,0,0,0],
             [0,1,1,1],
             [0,1,2,2],
             [0,1,3,3],
             [0,1,3,3],
             [0,1,2,2],
             [0,1,1,1],
             [0,0,0,0]]

    g_4x7 = [[0,0,0,0,0,0,0],
             [0,1,1,1,1,1,0],
             [0,1,2,3,2,1,0],
             [0,1,2,3,2,1,0]]

    g_4x8 = [[0,0,0,0,0,0,0,0],
             [0,1,1,1,1,1,1,0],
             [0,1,2,3,3,2,1,0],
             [0,1,2,3,3,2,1,0]]

    g_6x6 = [[0,0,0,0,0,0],
             [0,1,1,1,1,0],
             [0,1,2,2,1,0],
             [0,1,2,2,1,0],
             [0,1,1,1,1,0],
             [0,0,0,0,0,0]]

    g_5x5 = [[0,0,0,0,0],
             [0,1,1,1,1],
             [0,1,2,2,1],
             [0,1,2,2,1],
             [0,1,1,1,1]]

    # print(*g, sep='\n')
    # print('^- input -^')

    layers_to_matrix(rotate_lists(matrix_to_layers(g_7x4), rot=4), g_7x4)
    print()
    layers_to_matrix(rotate_lists(matrix_to_layers(g_8x4), rot=4), g_8x4)
    print()
    layers_to_matrix(rotate_lists(matrix_to_layers(g_4x7), rot=4), g_4x7)
    print()
    layers_to_matrix(rotate_lists(matrix_to_layers(g_4x8), rot=4), g_4x8)
    print()
    layers_to_matrix(rotate_lists(matrix_to_layers(g_6x6), rot=4), g_6x6)
    print()
    layers_to_matrix(rotate_lists(matrix_to_layers(g_5x5), rot=4), g_5x5)
    print()
    