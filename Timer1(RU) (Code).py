import time


def countdown(user_time):
   while user_time >= 0:
       mins, secs = divmod(user_time, 60)
       timer = '{:02d}:{:02d}'.format(mins, secs)
       print(timer, end='\r')
       time.sleep(1)
       user_time -= 1
   print('Время вышло!!')


if __name__ == '__main__':
   user_time = int(input("Введите время в секундах: "))
   countdown(user_time)