
def square_footage():
    shape = input('what shape is the room? ')
    if shape == 'square':
        side = int(input('tell me one side '))
        return side * side
    elif shape == 'rectangle':
        length = int(input('what is the length? '))
        width = int(input('what is the width? '))
        area = length * width
    elif shape == 'circle':
        radius = int(input('what is the radius? '))
        return radius * 3.14 * 2
    elif shape == 'triangle':
        base = int(input('what is the base? '))
        height = int(input('what is the height? '))
        return 0.5 * base * height
    

print(square_footage())



def circumference(radius):
    return 2 * 3.1426 * radius

circumference(4)
