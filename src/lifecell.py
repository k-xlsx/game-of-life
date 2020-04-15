import grid


class Cell(grid.Cell):
    """
    A Game of Life cell placed on the given grid
    """

    def __init__(self, grid, gridPosition: list, size: list,
                 color: list, borderColor: list=None, borderWidth: int=1,
                 alive: bool=True):
        self.alive = alive

        self.aliveColor = color
        self.aliveBorderColor = borderColor
        self.aliveBorderWidth = borderWidth

        self.deadColor = grid.cellColor
        self.deadBorderColor = grid.cellBorderColor
        self.deadBorderWidth = grid.cellBorderWidth

        if not(self.alive):
            color = self.deadColor
            borderColor = self.deadBorderColor
            borderWidth = self.deadBorderWidth

        position = grid[gridPosition[0]][gridPosition[1]].position
        super().__init__(position, gridPosition, size,
                         color, borderColor, borderWidth)

        grid[gridPosition[0]][gridPosition[1]] = self

    def __str__(self):
        return (('Cell' + str(self.gridPosition)) + ', ' +
                ('Alive: ' + str(self.alive)) + ', ' +
                ('Pos: ' + str(self.position)) + ', ' +
                ('Color: ' + str(self.color)) + ', ' +
                ('Border Color: ' + str(self.borderColor)))


    def live(self, grid):
        neighbors = self.get_alive_neighbors(grid)

        if len(neighbors) < 2 and self.alive:
            self.die()
        elif len(neighbors) > 3 and self.alive:
            self.die()
        elif len(neighbors) == 3 and not(self.alive):
            self.resurrect()

    def die(self):
        self.color = self.deadColor
        self.borderColor = self.deadBorderColor
        self.borderWidth = self.deadBorderWidth

        self.alive = False

    def resurrect(self):
        self.color = self.aliveColor
        self.borderColor = self.aliveBorderColor
        self.borderWidth = self.aliveBorderWidth

        self.alive = True

    def get_alive_neighbors(self, grid):
        neighbors = self.get_neighbors(grid)

        aliveNeighbors = []
        for neighbor in neighbors:
            if neighbor.alive:
                aliveNeighbors.append(neighbor)
        return aliveNeighbors

    def get_neighbors(self, grid) -> list:
        return super().get_neighbors(grid, self)
