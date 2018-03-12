import random

#generate a 9x9 sudoku board
def init_su():
	puzzle=[[None for _ in range(9)] for _ in range(9)]

	#insert while checking

	for i in range(9):
		for j in range(9):
			replace_value = 0
			check = [1,2,3,4,5,6,7,8,9]
			
			random.seed()
			insert_value=random.choice(check)
			#row_check = 0
			#col_check = 0
			row_fail = 0
			col_fail = 0
			grid_fail = 0
			while (puzzle[i][j] == None):
				
				if (row_fail == 1 or col_fail == 1 or grid_fail == 1):
					row_fail = 0
					col_fail = 0
					grid_fail = 0
					replace_value += 1
					insert_value = replace_value				

		
				if (replace_value > 9 or insert_value > 9):
					return None

				#row check
				if (insert_value in puzzle[i]):
					row_fail = 1
					continue
				#else:
				#	row_check = 1

				#column check
				for rows in range(9):
					if (insert_value == puzzle[rows][j]):
						col_fail = 1
						continue
				#	else:
				#		col_check = 1

				#if (row_fail == 0 and col_fail == 0):
				#	puzzle[i][j] = insert_value

				#3x3 check				
				#--first come first serve basis
				if (i%3 == 1):
					if (j%3 == 0):
						if (insert_value == puzzle[i-1][j] or insert_value == puzzle[i-1][j+1] or insert_value == puzzle[i-1][j+2]):
							grid_fail = 1
						elif (insert_value == puzzle[i+1][j] or insert_value == puzzle[i+1][j+1] or insert_value == puzzle[i+1][j+2]):
							grid_fail = 1
					elif (j%3 == 1):
						if (insert_value == puzzle[i-1][j] or insert_value == puzzle[i-1][j+1] or insert_value == puzzle[i-1][j-1]):
							grid_fail = 1 
						elif (insert_value == puzzle[i+1][j] or insert_value == puzzle[i+1][j+1] or insert_value == puzzle[i+1][j-1]):
							grid_fail = 1 
					elif (j%3 == 2):
						if (insert_value == puzzle[i-1][j] or insert_value == puzzle[i-1][j-1] or insert_value == puzzle[i-1][j-2]):
							grid_fail = 1                            
						elif (insert_value == puzzle[i+1][j] or insert_value == puzzle[i+1][j-1] or insert_value == puzzle[i+1][j-2]):
							grid_fail = 1
				

				elif (i%3 ==2):
					if (j%3 == 0):
						if (insert_value == puzzle[i-1][j] or insert_value == puzzle[i-1][j+1] or insert_value == puzzle[i-1][j+2]):
							grid_fail = 1 
						elif (insert_value == puzzle[i-2][j] or insert_value == puzzle[i-2][j+1] or insert_value == puzzle[i-2][j+2]):
							grid_fail = 1  
					elif (j%3 ==1):
						if (insert_value == puzzle[i-1][j] or insert_value == puzzle[i-1][j+1] or insert_value == puzzle[i-1][j-1]):
							grid_fail = 1 
						elif (insert_value == puzzle[i-2][j] or insert_value == puzzle[i-2][j+1] or insert_value == puzzle[i-2][j-1]):
							grid_fail = 1  
					elif (j%3 == 2):
						if (insert_value == puzzle[i-1][j] or insert_value == puzzle[i-1][j-1] or insert_value == puzzle[i-1][j-2]):
							grid_fail = 1 
						elif (insert_value == puzzle[i-2][j] or insert_value == puzzle[i-2][j-1] or insert_value == puzzle[i-2][j-2]):
							grid_fail = 1 	

				if (row_fail == 0 and col_fail == 0 and grid_fail == 0):
					puzzle[i][j] = insert_value
				

		

	return puzzle

def generate_puzzle():
	sudoku = None
	while (sudoku is None):
		sudoku = init_su()
	return sudoku

def dummy():
	puzzle=[[None for _ in range(9)] for _ in range(9)]
	for i in range(9):
		choice_r=['1','2','3','4','5','6','7','8','9']
		for j in range(9):
			random.seed()
			ran_element=random.choice(choice_r)
			puzzle[i][j]=ran_element
			choice_r.remove(ran_element)   
	return puzzle 


#display a sudoku board
def display(a):
	print()
	for i in range(9):
		if (i%3 == 0 and i != 0):
			print ('-----------------')
		for j in range(9):
			if(j==8):
				print(a[i][j])
			elif(j%3 == 2):
				print(a[i][j], end = '|')
			else:
				print(a[i][j], end = ' ')
	print()
a=generate_puzzle()
display(a)
	
