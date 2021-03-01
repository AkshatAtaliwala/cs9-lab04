from Stack import Stack

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return
    
def solveMaze(maze, startX, startY):
	stack = Stack() # Initialize the stack
	trail_counter = 1 # The starting position should be 1
	stack.push([startX, startY])

	if maze[startX][startY] == '+': # if the starting position is a wall
		return False
	elif maze[startX][startY] == 'G': # if the starting position is the goal
		return True

	while stack.isEmpty() == False: # While the stack has at least 1 item
		[x, y] = stack.peek() # checks the top value in the stack and assigns it to a coordinate

		if maze[x+1][y] == 'G' or maze[x-1][y] == 'G' or maze[x][y+1] == 'G' or maze[x][y-1] == 'G': # if the coordinate is next to the goal
			maze[x][y] = trail_counter
			printMaze(maze)
			return True
		
		if maze[x][y] == ' ': # if the coordinate is an empty string (open space)
			maze[x][y] = trail_counter # assign the coordinate to the counter instead of the empty string
			trail_counter += 1 # update the counter to the next value

			# checking for where to move next
			if maze[x-1][y] == ' ': # if North is an open space
				stack.push([x-1, y]) # add North coordinate to the stack
			elif maze[x][y+1] == ' ': # if N is not empty but East is
				stack.push([x, y+1]) # add East coordinate to the stack
			elif maze[x+1][y] == ' ': # if N and E aren't empty but South is
				stack.push([x+1, y]) # add South coordinate to the stack
			elif maze[x][y-1] == ' ': # if N, E, and S aren't open, check West to see if it is
				stack.push([x, y-1]) # add West coordinate to the stack
			else: # if none of the other directions are empty
				stack.pop() # go back a step and check the other directions from there
			
		elif maze[x][y] != ('G' or ' '): # if the coordinate is a wall or a trail number
			if maze[x-1][y] == ' ':
				stack.push([x-1, y]) # add North coordinate to the stack
			elif maze[x][y+1] == ' ': 
				stack.push([x, y+1]) # add East coordinate to the stack
			elif maze[x+1][y] == ' ': 
				stack.push([x+1, y]) # add South coordinate to the stack
			elif maze[x][y-1] == ' ':
				stack.push([x, y-1]) # add West coordinate to the stack
			else:
				stack.pop()

	printMaze(maze)	
	return False