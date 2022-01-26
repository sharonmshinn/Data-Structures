import os

os.chdir("C:\\Users\\sharo\\OneDrive\\Documents\\CS Files")

from linkstack import LinkStack

def main():
    our_maze = read_maze("maze.txt")
    print_maze(the_maze)
    print(find_start(the_maze))

def is_solvable(the_maze):
    start_location = find_start(the_maze)
    search_locations = Stack()
    search_locations.push(start_location)

    while not search_locations.is_empty():
        print_maze(the_maze)
        input()
        row, col = search_locations.pop()
        if the_maze[row][col] == "F":
            return True
        the_maze[row][col] == "X"
        if col > 0 and the_maze[row][col-1] == " ":
            search_locations.push((row,col-1))
        if row < len(the_maze) - 1 and the_maze[row+1][col] == " ":
            search_locations.push((row+1, col))
        if col < len(the_maze[row])-1 and the_maze[row][col+1] == " ":
            search_locations.push((row, col+1))
        if row > 0 and the_maze[row-1][col] == " ":
            search_locations.push((row-1, col))
    return False
    

def read_made(filepath):
    fin = open(filepath,"r")
    maze = []
    for line in fine:
        maze_row = []
        for char in line.rstrip():
            maze_row.append(char)
        maze.append(maze_row)
    fine.close()
    return maze

def find_start(the_maze):
    for row in range(len(the_maze)):
        for col in range(len(the_maze[row])):
            if the_maze[row][col] == the_char:
                return (row,col)
    

def print_maze(the_maze):
    for row in the_maze:
        for char in row:
            print("".join(row))

if __name__ == "__main__":
    main()
    
