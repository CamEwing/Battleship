#Let players place ships
#Add preview after placing ship (to confirm)
#Hit ship   ✘ 
#missed shot 


dim = 10;

		
attackArray = [[' ' for i in range(dim)] for i in range(dim)]
defenceArray = [[' ' for i in range(dim)] for i in range(dim)]

def printAttackGrid():
    print("┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐");
    print( "│   │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │");
    for i in range(dim):
        print( "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤");
        row = f"│{i+1:2} │";
        for j in range(dim):
            row += f"{attackArray[j][i].center(3)}" + "│";
        print(row);
    print( "└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘");

def printDefenceGrid():
    print("┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐");
    print( "│   │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │");
    for i in range(dim):
        print( "├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤");
        row = f"│{i+1:2} │";
        for j in range(dim):
            row += f"{defenceArray[j][i].center(3)}" + "│";
        print(row);
    print( "└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘");

def playerOneSetUp():
    print("Place battleships");
    print("1 - 2 piece\n2 - 3 piece\n1 - 4 piece\n1 - 5 piece")
    pieceLocation = input('Place ship (length coordinate orientation - ex. "3 C6 V"):');
    placeShip(pieceLocation);

def determineCoordIndex(coord):
    split = list(coord);
    if not split[1].isnumeric():
        split = 'x'; #Mark as error
        print("1");
        return split;
    if (len(split) <= 2):
        split[1] = int(split[1]) - 1;
    else:
        split[1] = int(split[1] + split[2]) - 1;
    if split[1] not in range(dim):
        split = 'x'; #Mark as error
        print("2");
        return split;
    split[0] = split[0].upper();
    split[0] = ord(split[0]) - 65;
    if split[0] not in range(dim):
        split = 'x'; #Mark as error
        print("3");
        return split;
    return split;


#Create loop to reprompt for input if improper values given
#Add placed pieces to attackArray
#Create check for placing pieces against attackArray to prevent overlapping pieces
def placeShip(pieceLocation):
    location = pieceLocation.split();

    length = int(location[0]);
    coord = determineCoordIndex(location[1]);
    if coord == 'x':
        print("improper coordinate", location[1]);
        return;
    orientation = location[2].upper();
    if length not in [2, 3, 4, 5]:
        print("improper length", length);
        return;
    if (orientation != "V" ) and (orientation != "H"):
        print("invalid orientation");
        return;

    if orientation == "V":
        if (coord[1] + length > dim):
            print("invalid placement");
            return;
        attackArray[coord[0]][coord[1]] = "△";
        for i in range(1,length-1):
            attackArray[coord[0]][coord[1]+i] = "□";
        attackArray[coord[0]][coord[1]+length-1] = "▽";
    else:
        if (coord[0] + length > dim):
            print("invalid placement");
            return;
        attackArray[coord[0]][coord[1]] = "◁";
        for i in range(1,length-1):
            attackArray[coord[0]+i][coord[1]] = "□";
        attackArray[coord[0]+length-1][coord[1]] = "▷";

while(1):
    printAttackGrid();
    playerOneSetUp();
