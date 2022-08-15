# final version

import heapq
from tkinter import *
from tkinter import messagebox, simpledialog

def identity(numRows, numCols, val=1, rowStart=0):
   return [[(val if i == j else 0) for j in range(numCols)]
               for i in range(rowStart, numRows)]


'''
   standardForm: [float], [[float]], [float], [[float]], [float], [[float]], [float] -> [float], [[float]], [float]
   Convert a linear program in general form to the standard form for the
   simplex algorithm.  The inputs are assumed to have the  correct dimensions: cost
   is a length n list, greaterThans is an n-by-m matrix, gtThreshold is a vector
   of length m, with the same pattern holding for the remaining inputs. No
   dimension errors are caught, and we assume there are no unrestricted variables.
'''
def standardForm(cost, greaterThans=[], gtThreshold=[], lessThans=[], ltThreshold=[],
                equalities=[], eqThreshold=[], maximization=True):
   newVars = 0
   numRows = 0
   if gtThreshold != []:
      newVars += len(gtThreshold)
      numRows += len(gtThreshold)
   if ltThreshold != []:
      newVars += len(ltThreshold)
      numRows += len(ltThreshold)
   if eqThreshold != []:
      numRows += len(eqThreshold)

   if not maximization:
      cost = [-x for x in cost]

   if newVars == 0:
      return cost, equalities, eqThreshold

   newCost = list(cost) + [0] * newVars

   constraints = []
   threshold = []

   oldConstraints = [(greaterThans, gtThreshold, -1), (lessThans, ltThreshold, 1),
                     (equalities, eqThreshold, 0)]

   offset = 0
   for constraintList, oldThreshold, coefficient in oldConstraints:
      constraints += [c + r for c, r in zip(constraintList,
         identity(numRows, newVars, coefficient, offset))]

      threshold += oldThreshold
      offset += len(oldThreshold)

   return newCost, constraints, threshold


def dot(a,b):
   return sum(x*y for x,y in zip(a,b))

def column(A, j):
   return [row[j] for row in A]

def transpose(A):
   return [column(A, j) for j in range(len(A[0]))]

def isPivotCol(col):
   return (len([c for c in col if c == 0]) == len(col) - 1) and sum(col) == 1

def variableValueForPivotColumn(tableau, column):
   pivotRow = [i for (i, x) in enumerate(column) if x == 1][0]
   return tableau[pivotRow][-1]

# assume the last m columns of A are the slack variables; the initial basis is
# the set of slack variables
def initialTableau(c, A, b):
   tableau = [row[:] + [x] for row, x in zip(A, b)]
   tableau.append([ci for ci in c])
   return tableau


def primalSolution(tableau):
   # the pivot columns denote which variables are used
   columns = transpose(tableau)
   indices = [j for j, col in enumerate(columns[:-1]) if isPivotCol(col)]
   return [(colIndex, variableValueForPivotColumn(tableau, columns[colIndex]))
            for colIndex in indices]


def objectiveValue(tableau):
   return -(tableau[-1][-1])


def canImprove(tableau):
   lastRow = tableau[-1]
   return any(x > 0 for x in lastRow[:-1])


# this can be slightly faster
def moreThanOneMin(L):
   if len(L) <= 1:
      return False

   x,y = heapq.nsmallest(2, L, key=lambda x: x[1])
   return x == y


def findPivotIndex(tableau):
   # pick minimum positive index of the last row
   column_choices = [(i,x) for (i,x) in enumerate(tableau[-1][:-1]) if x > 0]
   column = min(column_choices, key=lambda a: a[1])[0]

   # check if unbounded
   if all(row[column] <= 0 for row in tableau):
      raise Exception('Linear program is unbounded.')

   # check for degeneracy: more than one minimizer of the quotient
   quotients = [(i, r[-1] / r[column])
      for i,r in enumerate(tableau[:-1]) if r[column] > 0]

   if moreThanOneMin(quotients):
      raise Exception('Linear program is degenerate.')

   # pick row index minimizing the quotient
   row = min(quotients, key=lambda x: x[1])[0]

   return row, column


def pivotAbout(tableau, pivot):
   i,j = pivot

   pivotDenom = tableau[i][j]
   tableau[i] = [x / pivotDenom for x in tableau[i]]

   for k,row in enumerate(tableau):
      if k != i:
         pivotRowMultiple = [y * tableau[k][j] for y in tableau[i]]
         tableau[k] = [x - y for x,y in zip(tableau[k], pivotRowMultiple)]


'''
   simplex: [float], [[float]], [float] -> [float], float
   Solve the given standard-form linear program:

      max <c,x>
      s.t. Ax = b
           x >= 0

   providing the optimal solution x* and the value of the objective function
'''
def simplex(c, A, b):
   tableau = initialTableau(c, A, b)
   print("Initial tableau:")
   for row in tableau:
      print(row)
   print()

   while canImprove(tableau):
      pivot = findPivotIndex(tableau)
      print("Next pivot index is=%d,%d \n" % pivot)
      pivotAbout(tableau, pivot)
      print("Tableau after pivot:")
      for row in tableau:
         print(row)
      print()

   return tableau, primalSolution(tableau), objectiveValue(tableau)


if __name__ == "__main__":

   root = Tk()
   root.title("Linear Programming - Simplex Method")
   w = Label(root, text="Simplex Algorithm")
   w.pack()

   messagebox.showinfo("Welcome", "Welcome to a simple Linear Programming Calculator!\nPress OK to continue.")
   nNonBasic = simpledialog.askinteger("Num of non-basic variables", "How many non-basic variables are there?\n목적 함수 식의 변수와 잉여 변수가 포함된 비기저 변수의 개수를 입력하세요.")
   nBasic = simpledialog.askinteger("Num of basic variables", "How many basic variables are there?\n여유 변수와 인공 변수가 포함된 기저 변수의 개수를 입력하세요.")

   # 목적함수 계수 입력, 그리고 (있으면) 상수 입력 - list c
   i = 1
   c = []
   while i <= (nNonBasic + nBasic):
      cInput = simpledialog.askfloat("목적 함수 계수 - 변수 x_%d의 계수" % (i), "목적 함수에서 변수 x_%d의 계수를 입력하세요" % (i))
      i += 1
      c.append(cInput)
   cInput = simpledialog.askfloat("목적 함수의 상수", "수리 계획 확장형에서 목적 함수에서 상수항을 입력하세요. 없으면 0을 입력하시면 됩니다.")
   c.append(-cInput)

   # 제약식 좌변 계수 입력 - list A
   A = []
   for i in range(nBasic):
      line = []
      for j in range(nNonBasic + nBasic):
         AInput = simpledialog.askfloat("%d번째 제약식 좌변 계수 변수 x_%d의 계수" % (i + 1, j + 1),
                                          "%d번째 제약식 좌변에서 변수 x_%d의 계수를 입력하세요" % (i + 1, j + 1))
         line.append(AInput)
      A.append(line)

   # 제약식 우변 계수 입력 - list b
   i = 1
   b = []
   while i <= nBasic:
      bInput = simpledialog.askfloat("제약식 우변 계수 - %d번째 제약식의 우변" % (i),
                                       "제약식에서 %d번째 제약식의 우변에 해당하는 수를 입력하세요\n단 우변은 양수여야 합니다." % (i))
      i += 1
      b.append(bInput)


   t, s, v = simplex(c, A, b)
   print(s)
   print(v)
   messagebox.showinfo("Result", s)
   messagebox.showinfo("Result", v)




