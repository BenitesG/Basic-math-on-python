number_predece_suce = int(input('Type a number: '))

print('Analyzing the number {} your predecessor is {} and your sucessor is {}.'
      .format(number_predece_suce, number_predece_suce-1, number_predece_suce+1))

number_multi = int(input('Type another number: '))

print('Looking the number {0}, your double is: {1}, your triple is: {2}, and your square root is: {3}'.format(
    number_multi, number_multi*2, number_multi*3, number_multi**(1/2)))

grade_student = float(input('Type a student grade: '))
grade_student2 = float(input('Type another student grade: '))
average = float((grade_student + grade_student2)) / 2

print('The avarage of {:.1f} and {} is {:.1f}'.format(
    grade_student2, grade_student2, average))

meters_convert = float(input('Type in meters to convert: '))
cent_convert = float(meters_convert * 100)
millim_convert = float(meters_convert * 1000)


print('The number {}m in centimeters: {}cm and millimetters: {}mm'.format(
    meters_convert, cent_convert, millim_convert))

multi_table = int(input('Type a number to make a multiplication table: '))

print('-' * 15)
print(' {0:3} x  1 = {0:2}\n {0:3} x  2 = {1:3}\n {0:3} x  3 = {2:3}\n {0:3} x  4 = {3:3}\n {0:3} x  5 = {4:3}\n {0:3} x  6 = {5:3}\n {0:3} x  7 = {6:3}\n {0:3} x  8 = {7:3}\n {0:3} x  9 = {8:3}\n {0:3} x 10 = {9:3} '.format(
    multi_table, multi_table*2, multi_table*3, multi_table*4, multi_table*5, multi_table*6, multi_table*7, multi_table*8, multi_table*9, multi_table*10))
print('-' * 15)

reais = float(input('How much money do you have in Reais? '))


# fictitious dolar value
print('You can buy {:.2f}$ dollars'.format(reais / 3.27))
