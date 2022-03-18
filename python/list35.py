game = ["_","_","_","_","_","_","_","_","_"]
turn=1


while turn<10:

  if turn%2==0:

      pos=int(input("Player2 Enter position =>"))
      if
      game[pos-1] ='X'
  else:
      pos = int(input("Player1 Enter position =>"))
      game[pos - 1] = '0'


  print(game[0],'|',game[1],'|',game[2])
  print(game[3],'|',game[4],'|',game[5])
  print(game[6],'|',game[7],'|',game[8])
  if game[0] == game[1] and game[1] == game[2] and game[2] == 'X':
    print(" Player 2  is Winner")
    turn=15

  elif game[0] == game[1] and game[1] == game[2] and game[2] == '0':
    print(" Player 1  is Winner")
    turn=15
    if "X"=="X":
      print("Enter the onther positin")
  elif game[3] == game[4] and game[4] == game[5] and game[5] == 'X':
    print(" Player 2  is Winner")
    turn=15
    if "X"=="X":
      print("Enter the onther positin")
  elif game[3] == game[4] and game[4] == game[5] and game[5] == '0':
    print(" Player 1  is Winner")
    turn=15
  elif game[6] == game[7] and game[7] == game[8] and game[8] == 'X':
    print(" Player 2  is Winner")
    turn=15
  elif game[6] == game[7] and game[7] == game[8] and game[8] == '0':
    print(" Player 1  is Winner")
    turn=15
  elif game[0] == game[3] and game[3] == game[6] and game[6] == 'X':
    print(" Player 2  is Winner")
    turn=15
  elif game[0] == game[3] and game[3] == game[6] and game[6] == '0':
    print(" Player 1  is Winner")
    turn=15
  elif game[1] == game[4] and game[4] == game[7] and game[7] == 'X':
    print(" Player 2  is Winner")
    turn=15
  elif game[1] == game[4] and game[4] == game[7] and game[7] == '0':
    print(" Player 1  is Winner")
    turn=15
  elif game[2] == game[5] and game[5] == game[8] and game[8] == 'X':
    print(" Player 2  is Winner")
    turn=15
  elif game[2] == game[5] and game[5] == game[8] and game[8] == '0':
    print(" Player 1  is Winner")
    turn=15
  elif game[0] == game[4] and game[4] == game[8] and game[8] == 'X':
    print(" Player 2  is Winner")
    turn=15
  elif game[0] == game[4] and game[4] == game[8] and game[8] == '0':
    print(" Player 1  is Winner")
    turn=15
  elif game[2] == game[4] and game[4] == game[6] and game[6] == 'X':
    print(" Player 2  is Winner")
    turn=15
  elif game[2] == game[4] and game[4] == game[6] and game[6] == '0':
    print(" Player 1  is Winner")
    turn=15
  turn=turn+1

if turn ==10:
  print("Match tie")

