Faces = ["RIGHT", "LOWER", "UPPER", "DOWN", "FRONT", "BACK"]

right_face = []
lower_face = []
upper_face = []
down_face = []
front_face = []
back_face = []


class Cube:
    def __init__(self) -> None:
        pass

    def getInput(self):
        global right_face, lower_face, upper_face, down_face, front_face, back_face

        cube = []
        for face in Faces:
            print(f"Enter color row wise for {face} face")
            for i in range(9):
                color = input(": ")
                cube.append(color)

        right_face, lower_face, upper_face, down_face, front_face, back_face = [
            cube[i : i + 9] for i in range(0, len(cube), 9)
        ]


        return cube

    def Rotate(self, face, direction):
        if direction == 'c':
            new_face = [face[6], face[3], face[0],face[7], face[4], face[1],face[8], face[5], face[2],]
        elif direction == 'cc':
            new_face = [face[2], face[5], face[8],face[1], face[4], face[7],face[0], face[3], face[6],]
        return new_face

    

if __name__ == "__main__":
    cube = Cube()
    cube.getInput()
    print(right_face)
    output = cube.Rotate(right_face)
    print(output)