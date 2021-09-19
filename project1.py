# screen recorder
import cv2 as c
import pyautogui as p 
import numpy as np

#resolution capture
#Create resolution
rs= p.size()

#filename in which we store recording
fn = input("Enter the file path")
fps = 60.0

fourcc = c.VideoWriter_fourcc(*'XVID')# to save the format
output = c.VideoWriter(fn, fourcc, fps,rs) 

c.namedWindow("Live Recording", c.WINDOW_NORMAL)# to display the 
#window name

c.resizeWindow("Live Recording", (600,400))

# now to record
while True:
	img = p.screenshot()
	f= np.array(img)
	f= c.cvtColor(f,c.COLOR_BGR2RGB)
	output.write(f)
	c.imshow("Live Recording",f)

	if c.waitKey(1) == ord('q'):
		break
output.release()
c.destroyAllWindows()
