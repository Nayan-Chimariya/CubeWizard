Faces = ["RIGHT", "LEFT", "UPPER", "DOWN", "FRONT", "BACK"]
CROSS_POSITIONS = [1, 3, 5, 7]

right_face = []
left_face = []
upper_face = []
down_face = []
front_face = []
back_face = []


class Cube:
    def __init__(self) -> None:
        pass

    def getInput(self):
        global right_face, left_face, upper_face, down_face, front_face, back_face

        # For testing - Ignore input
        # --------------------------#

        # cube = []
        # for face in Faces:
        #     print(f"Enter color row wise for {face} face")
        #     for i in range(9):
        #         color = input(": ")
        #         cube.append(color)

        # --------------------------#

        cube = [
            "b",
            "o",
            "b",
            "r",
            "b",
            "o",
            "w",
            "r",
            "y",
            "w",
            "w",
            "y",
            "g",
            "g",
            "g",
            "g",
            "w",
            "r",
            "o",
            "o",
            "w",
            "b",
            "r",
            "w",
            "r",
            "b",
            "y",
            "w",
            "r",
            "b",
            "g",
            "o",
            "y",
            "y",
            "b",
            "r",
            "b",
            "o",
            "o",
            "y",
            "y",
            "w",
            "g",
            "b",
            "r",
            "o",
            "y",
            "g",
            "g",
            "w",
            "r",
            "g",
            "y",
            "o",
        ]

        right_face, left_face, upper_face, down_face, front_face, back_face = [
            cube[i : i + 9] for i in range(0, len(cube), 9)
        ]

    def Rotate(self, face, direction):
        rf = right_face
        lf = left_face
        ff = front_face
        uf = upper_face
        bf = back_face
        df = down_face

        if face == right_face:
            if direction == "c":
                print({f"Rotate {face} face clockwise"})
                right_face = [
                    face[6],
                    face[3],
                    face[0],
                    face[7],
                    face[4],
                    face[1],
                    face[8],
                    face[5],
                    face[2],
                ]
                front_face = [
                    front_face[0],
                    front_face[1],
                    df[2],
                    front_face[3],
                    front_face[4],
                    df[5],
                    front_face[6],
                    front_face[7],
                    df[8],
                ]
                upper_face = [
                    upper_face[0],
                    upper_face[1],
                    ff[2],
                    upper_face[3],
                    upper_face[4],
                    ff[5],
                    upper_face[6],
                    upper_face[7],
                    ff[8],
                ]
                back_face = [
                    back_face[0],
                    back_face[1],
                    uf[2],
                    back_face[3],
                    back_face[4],
                    uf[5],
                    back_face[6],
                    back_face[7],
                    uf[8],
                ]
                down_face = [
                    down_face[0],
                    down_face[1],
                    bf[2],
                    down_face[3],
                    down_face[4],
                    bf[5],
                    down_face[6],
                    down_face[7],
                    bf[8],
                ]

            elif direction == "cc":
                print({f"Rotate {face} face counter clockwise"})
                right_face = [
                    face[2],
                    face[5],
                    face[8],
                    face[1],
                    face[4],
                    face[7],
                    face[0],
                    face[3],
                    face[6],
                ]
                front_face = [
                    front_face[0],
                    front_face[1],
                    uf[2],
                    front_face[3],
                    front_face[4],
                    uf[5],
                    front_face[6],
                    front_face[7],
                    uf[8],
                ]
                upper_face = [
                    upper_face[0],
                    upper_face[1],
                    bf[2],
                    upper_face[3],
                    upper_face[4],
                    bf[5],
                    upper_face[6],
                    upper_face[7],
                    bf[8],
                ]
                back_face = [
                    back_face[0],
                    back_face[1],
                    df[2],
                    back_face[3],
                    back_face[4],
                    df[5],
                    back_face[6],
                    back_face[7],
                    df[8],
                ]
                down_face = [
                    down_face[0],
                    down_face[1],
                    ff[2],
                    down_face[3],
                    down_face[4],
                    ff[5],
                    down_face[6],
                    down_face[7],
                    ff[8],
                ]

        # todo -complete for all the faces

    def solve_cross(self):
        center_color = front_face[4]

        opposite_color_dict = {
            "r": "o",
            "g": "b",
            "b": "g",
            "w": "y",
            "o": "r",
            "y": "w",
        }
        cross_color = opposite_color_dict.get(center_color)

        for positions in CROSS_POSITIONS:
            if cross_color not in front_face[positions]:
                # todo - complete the algorithm
                print("requires completion")


if __name__ == "__main__":
    cube = Cube()
    cube.getInput()

    print(right_face)

    output = cube.solve_cross()
    print(output)
