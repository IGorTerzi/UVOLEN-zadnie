for i in range(1, 10, 3):
    for j in range(1, 11):
        print(
            f'{i} x {j} = {i*j}\t', 
            f'{i+1} x {j} = {(i+1)*j}\t',
            f'{i+2} x {j} = {(i+2)*j}')
    print('---------------------------------------------')