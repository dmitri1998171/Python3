from OpenGL.GL import *
from OpenGL.GLU import * 
from OpenGL.GLUT import *
from PIL import Image
import os, math

ESCAPE = b'\033'

xrot, yrot = 0, 0
ambient = (1.0, 1.0, 1.0, 1)
lightpos = (1.0, 1.0, 1.0)

x1,y1,z1 = 0,0,0
x2,y2,z2 = 1,1,1
k = 0.5
j = k/4

angle = 0
lx, ly, lz = 0, 0, 5
camX, camY, camZ = 0, 1, -4
deltaAngle, deltaMove = 0, 0
xOrigin = -1
yOrigin = -1

font = GLUT_STROKE_ROMAN
W,H = 800,600
frame = 0
time, timebase = 0,0
fps = 0

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(width)/float (height), 1.0, 60.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def drawBox ( x1, x2, y1, y2, z1, z2 ):
	glBindTexture ( GL_TEXTURE_2D, texture )
	glBegin       ( GL_POLYGON )         				# front face
	glNormal3f    ( 0.0, 0.0, 1.0 )
	glTexCoord2f  ( 0, 0 )
	glVertex3f    ( x1, y1, z2 )
	glTexCoord2f  ( 1, 0 )
	glVertex3f    ( x2, y1, z2 )
	glTexCoord2f  ( 1, 1 )
	glVertex3f    ( x2, y2, z2 )
	glTexCoord2f  ( 0, 1 )
	glVertex3f    ( x1, y2, z2 )
	glEnd         ()
	
	glBegin      ( GL_POLYGON )         				# back face
	glNormal3f   ( 0.0, 0.0, -1.0 )
	glTexCoord2f ( 1, 0 )
	glVertex3f   ( x2, y1, z1 )
	glTexCoord2f ( 0, 0 )
	glVertex3f   ( x1, y1, z1 )
	glTexCoord2f ( 0, 1 )
	glVertex3f   ( x1, y2, z1 )
	glTexCoord2f ( 1, 1 )
	glVertex3f   ( x2, y2, z1 )
	glEnd        ()
	
	glBegin      ( GL_POLYGON )         				# left face
	glNormal3f   ( -1.0, 0.0, 0.0 )
	glTexCoord2f ( 0, 0 )
	glVertex3f   ( x1, y1, z1 )
	glTexCoord2f ( 0, 1 )
	glVertex3f   ( x1, y1, z2 )
	glTexCoord2f ( 1, 1 )
	glVertex3f   ( x1, y2, z2 )
	glTexCoord2f ( 1, 0 )
	glVertex3f   ( x1, y2, z1 )
	glEnd        ()
	
	glBegin      ( GL_POLYGON )         				#  right face
	glNormal3f   ( 1.0, 0.0, 0.0 )
	glTexCoord2f ( 0, 1 )
	glVertex3f   ( x2, y1, z2 )
	glTexCoord2f ( 0, 0 )
	glVertex3f   ( x2, y1, z1 )
	glTexCoord2f ( 1, 0 )
	glVertex3f   ( x2, y2, z1 )
	glTexCoord2f ( 1, 1 )
	glVertex3f   ( x2, y2, z2 )
	glEnd        ()
	
	glBegin      ( GL_POLYGON )         		# top face
	glNormal3f   ( 0.0, 1.0, 0.0 )
	glTexCoord2f ( 0, 1 )
	glVertex3f   ( x1, y2, z2 )
	glTexCoord2f ( 1, 1 )
	glVertex3f   ( x2, y2, z2 )
	glTexCoord2f ( 1, 0 )
	glVertex3f   ( x2, y2, z1 )
	glTexCoord2f ( 0, 0 )
	glVertex3f   ( x1, y2, z1 )
	glEnd        ()
	
	glBegin      ( GL_POLYGON )         		#  bottom face
	glNormal3f   ( 0.0, -1.0, 0.0 )
	glTexCoord2f ( 1, 1 )
	glVertex3f   ( x2, y1, z2 )
	glTexCoord2f ( 1, 0 )
	glVertex3f   ( x1, y1, z2 )
	glTexCoord2f ( 0, 0 )
	glVertex3f   ( x1, y1, z1 )
	glTexCoord2f ( 1, 0 )
	glVertex3f   ( x2, y1, z1 )
	glEnd        ()

def loadTexture ( fileName ):
	image  = Image.open ( fileName )
	width  = image.size [0]
	height = image.size [1]
	image  = image.tobytes ( "raw", "RGBA", 0, -1 )
	texture = glGenTextures ( 1 )
	
	glBindTexture     ( GL_TEXTURE_2D, texture )   # 2d texture (x and y size)
	glPixelStorei     ( GL_UNPACK_ALIGNMENT,1 )
	glTexParameterf   ( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
	glTexParameterf   ( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
	glTexParameteri   ( GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR )
	glTexParameteri   ( GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_LINEAR )
	gluBuild2DMipmaps ( GL_TEXTURE_2D, 3, width, height, GL_RGBA, GL_UNSIGNED_BYTE, image )
	
	return texture

def Cube(x,y,z):
    glPushMatrix()
    glTranslatef(-x,y,z)

    glRotatef      ( xrot, 1, 0, 0 )
    glTranslatef   ( j,j,j )		    # ось вращ. в центр			
    glRotatef      ( yrot, 0, 1, 0)
    glTranslatef   ( -k,-k,-k )         # ось вращ. в центр
    
    drawBox        (x1, x2, y1, y2, z1, z2)
    glPopMatrix()

def computePos(deltaMove):
    global lx,lz,camX,camZ
    camX = camX + deltaMove * lx * 0.1
    camZ = camZ + deltaMove * lz * 0.1

def blit_text(x,y,scale,w,font,text,r,g,b):
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()

    glOrtho(0, W, 0, H, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    glColor3f(r, g, b)
    glLineWidth(w)
    glTranslatef(x, y, 0)
    glScalef(scale, scale, scale)
    for ch in text:
        glutStrokeCharacter(font,ctypes.c_int(ord(ch)))
    
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()

    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

def fpsFunc():
    global fps, frame, time, timebase
    frame = frame + 1
    time=glutGet(GLUT_ELAPSED_TIME)
    if (time - timebase > 1000):
        fps = frame*1000.0/(time-timebase)
        timebase = time
        frame = 0
    return fps

def draw():
    global camX,camY,camZ,lx,lz,angle,deltaAngle,deltaMove
    
    if (deltaMove): 
        computePos(deltaMove)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # print("tx: ", camX+lx, "\ttz: ", camZ+lz,"\tangle: ", angle)
    gluLookAt(camX,    camY, camZ, 
              camX+lx, camY+ly, camZ+lz,
              0.0,     1, 0.0)
    # glLightfv(GL_LIGHT0, GL_POSITION, lightpos)
    # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (255,0,0))
    
    glTranslatef(5,-1,-5)
    for i in range(10):
        for j in range(10):
            Cube(i,0,j)
    
    text_fps = "FPS: " + str(int(fpsFunc()))
    blit_text(W-(len(text_fps)*17),H-30, 0.2, 3, 
        GLUT_STROKE_ROMAN, text_fps, 0, 255, 0)

    # print(text_fps)
    print("deltaMove: ", deltaMove)

    glutSwapBuffers()
# =================================================
def lightFunc():
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient) # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)                           # Включаем освещение
    glEnable(GL_LIGHT0)                             # Включаем один источник света
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)     # Определяем положение источника света

def textureInit():
    glDepthFunc  ( GL_LEQUAL )
    glEnable     ( GL_DEPTH_TEST )
    glEnable     ( GL_TEXTURE_2D )
    glHint       ( GL_POLYGON_SMOOTH_HINT,         GL_NICEST )
    glHint       ( GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST )
# =================================================
def keyboard(key, foo, bar):
    global deltaMove
    if key == ESCAPE: os.kill(0,4)

def specialkeys(key, x, y):
    global deltaMove
    if key == GLUT_KEY_UP: deltaMove = 0.5             
    if key == GLUT_KEY_DOWN: deltaMove = -0.5

def releaseKey(key, x, y):
    global deltaMove
    if ((key == GLUT_KEY_UP) or (key == GLUT_KEY_DOWN)):
        deltaMove = 0
# =================================================
def mouseButton(button, state, x, y):
    global xOrigin, yOrigin, angle
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            angle += deltaAngle
            xOrigin = -1
            yOrigin = 1
        else:
            xOrigin = x
            yOrigin = y

def passiveMouseMove(x, y):
    global xOrigin, yOrigin, angle, deltaAngle, lx, ly, lz
    if (xOrigin >= 0):
        deltaAngle = -(x - xOrigin) * 0.01
        lx = math.sin(angle + deltaAngle)
        lz = math.cos(angle + deltaAngle)
    if (yOrigin >= 0):
        deltaAngle = -(y - yOrigin) * 0.01
        ly = math.sin(angle + deltaAngle)
# =================================================
def init():
    glClearColor(0.5, 0.5, 0.5, 1.0)                # Серый цвет для первоначальной закраски
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glutSetCursor(GLUT_CURSOR_NONE)
    lightFunc()
    textureInit()

glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(W, H)
glutInitWindowPosition(300, 150)
glutInit(sys.argv)
glutCreateWindow(b"PyCraft")

glutDisplayFunc(draw)
glutReshapeFunc(reshape)
glutIdleFunc(draw) 

glutIgnoreKeyRepeat(1)

glutKeyboardFunc(keyboard)
glutSpecialFunc(specialkeys)
glutSpecialUpFunc(releaseKey)

glutMouseFunc(mouseButton)
glutPassiveMotionFunc(passiveMouseMove)

init()

texture = loadTexture ( "./textures/grass.png" )

glutMainLoop()