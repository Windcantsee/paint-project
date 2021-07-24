from pygame import *
from random import *
from math import *
from glob import *
#the paint project
#the size of whole project
screen = display.set_mode((1200,800))

#the caption and icon
display.set_caption("William")
display.set_icon(transform.scale(image.load("icon.png"),(25,25)))

#rectangles of different tools
pencilRect = Rect(20,20,70,70)
eraserRect = Rect(100,20,70,70)
lineRect = Rect(20,100,70,70)
sprayRect = Rect(100,100,70,70)
ovalUnfilledRect = Rect(20,180,70,70)
ovalFilledRect = Rect(100,180,70,70)
rectangleUnfilledRect = Rect(20,260,70,70)
rectangleFilledRect = Rect(100,260,70,70)
saveRect = Rect(20,340,70,70)
mosaicRect = Rect(100,340,70,70)
backgroundRect = Rect(20,420,70,70)
cleanRect = Rect(100,420,70,70)
loadRect = Rect(20,500,70,70)
canvas = Rect(180,20,1000,600)


#draw place where stamp tools placed
stamp1Rect = Rect(190,655,150,100)
stamp2Rect = Rect(360,655,150,100)
stamp3Rect = Rect(530,655,150,100)
stamp4Rect = Rect(700,655,150,100)
stamp5Rect = Rect(870,655,150,100)
stamp6Rect = Rect(1040,655,150,100)

#prepare for drawing line
start = 0,0

#orignal size of tools
size = 10

#load pics of tools and transform into approptiate size
pencilPic = transform.scale(image.load("pencil.jpg"),(70,70))
eraserPic = transform.scale(image.load("eraser.jpg"),(70,70))
linePic = transform.scale(image.load("line.jpg"),(70,70))
sprayPic = transform.scale(image.load("spray.jpg"),(70,70))
ovalUPic = transform.scale(image.load("ovalunfill.png"),(70,70))
ovalFPic = transform.scale(image.load("ovalfill.png"),(70,70))
rectUPic = transform.scale(image.load("rect.png"),(60,60))
rectFPic = transform.scale(image.load("rectfill.png"),(60,60))
JPic = transform.scale(image.load("Junkrat.png"),(1000,600))
JPics = transform.scale(JPic,(70,70))
#savePic = transform.scale(image.load("save.jpg"),(70,70))
mosaicPic = transform.scale(image.load("mosaic.jpg"),(70,70))
cleanPic = transform.scale(image.load("clean.jpg"),(70,70))
loadPic = transform.scale(image.load("load.jpg"),(70,70))
screen.blit(transform.scale(image.load("background.jpg"),(1200,800)),(0,0))
colorpalette = transform.scale(image.load("colorpalette.jpg"),(150,150))

#load stamps and transform into approptiate size
stamp1 = transform.scale(image.load("stamp1.png"),(150,100))
stamp2 = transform.scale(image.load("stamp2.png"),(150,100))
stamp3 = transform.scale(image.load("stamp3.png"),(150,100))
stamp4 = transform.scale(image.load("stamp4.png"),(150,100))
stamp5 = transform.scale(image.load("stamp5.png"),(150,100))
stamp6 = transform.scale(image.load("stamp6.png"),(150,100))

#get name
def getName(screen,showFiles):
    ans = ""                    # final answer will be built one letter at a time.
    arialFont = font.SysFont("Times New Roman", 16)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(580,625,200,25) # make changes here.

    if showFiles:
        pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
        n = len(pics)
        choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
        draw.rect(screen,(220,220,220),choiceArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),choiceArea,1)        # draw the text window and the text.
        for i in range(n):
            txtPic = arialFont.render(pics[i], True, (0,111,0))   #
            screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))

    cursorShow = 0
    myclock = time.Clock()
    typing = True
    while typing:
        cursorShow += 1
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN :
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans

        txtPic = arialFont.render(ans, True, (0,0,0))   #
        draw.rect(screen,(220,255,220),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        if cursorShow // 50 % 2 == 1:
            cx = textArea.x+txtPic.get_width()+3
            cy = textArea.y+3
            draw.rect(screen,(255,0,0),(cx,cy,2,textArea.height-6))
        myclock.tick(100)
        display.flip()

    screen.blit(back,(0,0))
    return ans

#default size of stamps
m=150
n=150

#default colour
c = 0

#defalut tool
tool = False

running =True
drawed = False
while running:
    press = False
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
           if e.button == 1:
               start = e.pos
               William = screen.subsurface(canvas).copy()   #save what drawed on the canvas
               drawed = True
           if e.button == 4:    #how to change size of tool larger
               size += 1
               if m < 300 and n < 300:
                    m += 4
                    n += 4
           if e.button == 5 and size >1: #how tochange size of tool smaller
               size -= 1
               if m > 4 and n > 4:
                    m -= 4
                    n -= 4
        if e.type == MOUSEBUTTONUP:
            press = True

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    if 20 <= mx <= 170 and 635 <= my <= 785 and press:
        c = screen.get_at((mx,my))
        draw.rect(screen,c,(20,500,70,70))
    
    #blit pics into corresponding rects+
    screen.blit(pencilPic,(20,20))
    screen.blit(eraserPic,(100,20))
    screen.blit(linePic,(20,100))
    screen.blit(sprayPic,(100,100))
    draw.rect(screen,(255,255,255),canvas)
    if drawed :
        screen.blit(David,canvas)
    screen.blit(ovalUPic,(20,180))
    screen.blit(ovalFPic,(100,180))
    screen.blit(rectUPic,(25,265))
    screen.blit(rectFPic,(105,265))
    #screen.blit(savePic,(20,340))
    screen.blit(mosaicPic,(100,340))
    screen.blit(JPics,(20,420))
    screen.blit(cleanPic,(100,420))
    screen.blit(loadPic,(20,500))
    screen.blit(colorpalette,(20,635))
    
    #blit stamps into corresponding rects+
    draw.rect(screen,(255,255,255),stamp1Rect)
    screen.blit(stamp1,(190,655))
    draw.rect(screen,(255,255,255),stamp2Rect)
    screen.blit(stamp2,(360,655))
    draw.rect(screen,(255,255,255),stamp3Rect)
    screen.blit(stamp3,(530,655))
    draw.rect(screen,(255,255,255),stamp4Rect)
    screen.blit(stamp4,(700,655))
    draw.rect(screen,(255,255,255),stamp5Rect)
    screen.blit(stamp5,(870,655))
    draw.rect(screen,(255,255,255),stamp6Rect)
    screen.blit(stamp6,(1040,655))
    
    #draw the black rect outside the tools
    draw.rect(screen,(0,255,0),pencilRect,2)
    draw.rect(screen,(0,255,0),eraserRect,2)
    draw.rect(screen,(0,255,0),lineRect,2)
    draw.rect(screen,(0,255,0),sprayRect,2)
    draw.rect(screen,(0,255,0),ovalUnfilledRect,2)
    draw.rect(screen,(0,255,0),ovalFilledRect,2)
    draw.rect(screen,(0,255,0),rectangleUnfilledRect,2)
    draw.rect(screen,(0,255,0),rectangleFilledRect,2)
    draw.rect(screen,(0,255,0),saveRect,2)
    draw.rect(screen,(0,255,0),mosaicRect,2)
    draw.rect(screen,(0,255,0),backgroundRect,2)
    draw.rect(screen,(0,255,0),cleanRect,2)
    draw.rect(screen,(0,255,0),loadRect,2)
    
    draw.rect(screen,(0,255,0),stamp1Rect,2)
    draw.rect(screen,(0,255,0),stamp2Rect,2)
    draw.rect(screen,(0,255,0),stamp3Rect,2)
    draw.rect(screen,(0,255,0),stamp4Rect,2)
    draw.rect(screen,(0,255,0),stamp5Rect,2)
    draw.rect(screen,(0,255,0),stamp6Rect,2)
    draw.rect(screen,(0,0,0),canvas,2)

    #change colour when choose tools
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),pencilRect,2)
        if press:
            tool="pencil"

    elif eraserRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),eraserRect,2)
        if press:
            tool="eraser"

    elif lineRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),lineRect,2)
        if press:
            tool="line"

    elif sprayRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),sprayRect,2)
        if press:
            tool="spray"

    elif ovalUnfilledRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),ovalUnfilledRect,2)
        if press:
            tool="ovalU"

    elif ovalFilledRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),ovalFilledRect,2)
        if press:
            tool="ovalF"

    elif rectangleUnfilledRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),rectangleUnfilledRect,2)
        if press:
            tool="rectU"

    elif rectangleFilledRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),rectangleFilledRect,2)
        if press:
            tool="rectF"

    elif saveRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),saveRect,2)
        if press:
            name = getName(screen,True)
            image.save(screen.subsurface(canvas),name)
            
    elif loadRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),saveRect,2)
        if press:
            name = getName(screen,True)
            loadpic= image.load(name)
            screen.blit(loadpic,())
    elif mosaicRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),mosaicRect,2)
        if press:
            tool="mosaic"

    elif backgroundRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),backgroundRect,2)
        if press:
            screen.blit(JPic,canvas)    #clean the canvas and have a background

    elif cleanRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),cleanRect,2)
        if press:
            draw.rect(screen,(255,255,255),canvas)  
            draw.rect(screen,0,canvas,2)    #clean the canvas

    elif stamp1Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),stamp1Rect,2)
        if press:
            tool="stamp1"

    elif stamp2Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),stamp2Rect,2)
        if press:
            tool="stamp2"

    elif stamp3Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),stamp3Rect,2)
        if press:
            tool="stamp3"

    elif stamp4Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),stamp4Rect,2)
        if press:
            tool="stamp4"

    elif stamp5Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),stamp5Rect,2)
        if press:
            tool="stamp5"

    elif stamp6Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),stamp6Rect,2)
        if press:
            tool="stamp6"


    #how these tools work
    if canvas.collidepoint(mx,my) and mb[0] == 1:   #make sure that it drawed on the canvas
        screen.set_clip(canvas)     #make sure it cannot draw out of canvas

        if tool == "pencil":
            draw.line(screen,c,(omx,omy),(mx,my),size)

        elif tool == "eraser":
            draw.circle(screen,(255,255,255),(mx,my),size)

        elif tool == "line":
            screen.blit(William,canvas)
            draw.line(screen,c,start,(mx,my),size)

        elif tool == "spray":
            for h in range(3):
                r=size
                x=randint(-r,r)
                y=randint(-r,r)
                if hypot(x,y)<= r:
                    draw.circle(screen,c,(mx+x,my+y),1)
                m=randint(-2*r,2*r)
                n=randint(-2*r,2*r)
                if hypot(m,n)<= 2*r:
                    draw.circle(screen,c,(mx+m,my+n),1)

        elif tool == "ovalU":
            screen.blit(William,canvas)
            a,b = start
            ovalRect = Rect(a,b,mx-a,my-b)
            ovalRect.normalize()
            if ovalRect.width < size*2 or ovalRect.height < size*2 :
                draw.ellipse(screen,c,ovalRect)
            else:
                draw.ellipse(screen,c,ovalRect,size)

        elif tool == "ovalF":
            screen.blit(William,canvas)
            a,b = start
            ovalRect = Rect(a,b,mx-a,my-b)
            ovalRect.normalize()
            draw.ellipse(screen,c,ovalRect)

        elif tool == "rectU":
            screen.blit(William,canvas)
            a,b = start
            draw.rect(screen,c,(a,b,mx-a,my-b),size)

        elif tool == "rectF":
            screen.blit(William,canvas)
            a,b = start
            draw.rect(screen,c,(a,b,mx-a,my-b))

        elif tool == "mosaic":
            c = screen.get_at((mx,my))
            draw.line(screen,c,(omx,omy),(mx,my),size)

        elif tool == "stamp1":
            screen.blit(transform.scale(stamp1,(m,n)),(mx-m/2,my-n/2))

        elif tool == "stamp2":
            screen.blit(transform.scale(stamp2,(m,n)),(mx-m/2,my-n/2))

        elif tool == "stamp3":
            screen.blit(transform.scale(stamp3,(m,n)),(mx-m/2,my-n/2))

        elif tool == "stamp4":
            screen.blit(transform.scale(stamp4,(m,n)),(mx-m/2,my-n/2))

        elif tool == "stamp5":
            screen.blit(transform.scale(stamp5,(m,n)),(mx-m/2,my-n/2))

        elif tool == "stamp6":
            screen.blit(transform.scale(stamp6,(m,n)),(mx-m/2,my-n/2))


        screen.set_clip(None)


    omx,omy = mx,my
    David = screen.subsurface(canvas).copy()    
    display.flip()


quit()
