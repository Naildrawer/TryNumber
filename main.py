import random as r

def is_valid(s):
   if s.isdigit() and 1 <= int(s) <= 100:
        return True
   else:
        return('А может быть все-таки введем целое число от 1 до 100?')
     
def compare_num():
  randnumber = r.randint(1, 100)
  print(randnumber)
  k = 0
  while True:
    usernumber = (input())
    if is_valid(usernumber) == True:
      usernumber = int(usernumber)
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    k += 1
    if usernumber < randnumber:
      print('Ваше число меньше загаданного, попробуйте еще разок')
    elif usernumber > randnumber:
      print('Ваше число больше загаданного, попробуйте еще разок')
    else:
      print('Вы угадали число за', k,'попыток')
      break 

def continue_game():
  while True:  
    print('Вы желаете сыграть в игру заново?(Y/N)')
    answer = input()
    if answer == "Y":
      return(False)
    elif answer == "N":
      print('Всего доброго')
      return(True)
    else:
      print("Введено неправильное значение")
     
  
    
def game():
  while True:
    print('Добро пожаловать в числовую угадайку')
    compare_num()
    if continue_game():
      break
    
game()  
  

  

  
  
  