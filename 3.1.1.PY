import math

# Dictionary of paint colors and cost per gallon
paintColors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

wall_height = float(input('Enter wall height (feet): \n'))
wall_width = float(input('Enter wall width (feet): \n'))
wall_area = wall_width*wall_height
print('Wall area:',int(wall_area),'square feet')
print ('Paint needed:','%.6f'%(wall_area/350),'gallons')
print ('Cans needed:', (int(wall_area/350) + 1), 'can(s)')
print("\n".rstrip("\n"))
print ('Choose a color to paint the wall:')
color = input()
print('Cost of purchasing', color,'paint:', '$'+str(paintColors.get(color,0) *(int(wall_area/350) + 1)))


# this version will pass the zyBooks tests for 3.1.1 in CS 200: Computer Science’s Role in Industry (SNHU)
