import pyautogui as root
from time import sleep
alphabetE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabetR = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'ц', 'ч', 'ш', 'щ', 'я']
screen_size = str(root.size())
screen_size_x, screen_size_y = screen_size.split(",")
screen_size_x = screen_size_x.replace("Size(width=","")
screen_size_y = screen_size_y.replace("height=","")
screen_size_y = screen_size_y.replace(")","")
screen_size_y = screen_size_y.replace(" ","")
screen_size_x = int(screen_size_x)
screen_size_y = int(screen_size_y)
Xcenter = screen_size_x // 2
Ycenter = screen_size_y // 2
root.moveTo(Xcenter, Ycenter, 0.5)
root.hotkey('win', 'd')
sleep(0.5)
xScreen = screen_size_x
yScreen = screen_size_y // 3 * 2
root.moveTo(1, 1, 0.5)
root.dragTo(xScreen, yScreen, 0.8)
sleep(0.5)
for i in range(30):
	root.hotkey(alphabetE[i])
	root.hotkey('del')
	root.hotkey('Enter')
	sleep(0.1)
for i in range(30):
	root.hotkey('Enter')
	sleep(0.5)
for j in range(33):
	root.hotkey(alphabetR[j])
	root.hotkey('del')
	sleep(0.1)
#sleep(3)
#root.hotkey('ctrl', 'alt', 'delete')
