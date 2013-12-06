

class SudokuBoard:
  def __init__(self, dimension=3, board=None):
    self.dim = dimension
    self.board = [[-1 for x in xrange(dimension * dimension)] for x in xrange(dimension * dimension)]
    self.wid = dimension * dimension
   
  def is_solved(self):
    for x in xrange(self.wid):
      if not self.check_row_col(x) or not self.check_box(x):
        return False
    return True

  def check_row_col(self, y):   
    rvals = [False for x in xrange(self.wid)]
    cvals = [False for x in xrange(self.wid)]
    for x in xrange(self.wid):
      rvals[self.board[y][x]] = True
      cvals[self.board[x][y]] = True
    for x in xrange(self.wid):
      if rvals[x] == False or cvals[x] == False:
        return False
    return True 

  def check_block(self, b):
    bvals = [False for x in xrange(self.wid)]
    init_c = (self.dim * (b % self.dim))
    init_r = (self.dim * floor(b / self.dim))
    for x in xrange(self.wid):
      r = init_r + floor(x / self.dim)
      c = init_c + (x % self.dim)
      bvals[self.board[r][c]] = True
    for x in xrange(self.wid):
      if not bvals[x]:
        return False
    return True

  def is_solvable(self):
    w = self.wid
    S = ones((w,w,w), int)
    

x = SudokuBoard() 
print x.is_solved()
