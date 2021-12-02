let, num = (input('Insert the position on the chess using capital letter from A to H and a number from 1 to 8 (ex: A8): ').upper())
num = int(num)
let = str(let) 
let_pos = ['A', 'C', 'E', 'G']
let_pos_x = ['B', 'D', 'F', 'H']
num_pos = [1,3,5,7]
num_pos_x = [2,4,6,8]

if let in let_pos and num in num_pos:
    print('The colour of your square is Black!')
elif let in let_pos and num in num_pos_x:
    print('The colour of your square is White!')
elif let in let_pos_x and num in num_pos: 
    print('The colour of your square is White!')
elif let in let_pos_x and num in num_pos_x:
    print('The colour of your square is Black!')


   


