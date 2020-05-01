from tkinter import *
import random
import time

nivel = 1
score = 0
def iniciar():
    
    class Ball:
        def __init__(self, canvas, paddle, color):
            self.canvas = canvas
            self.paddle = paddle
            self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
            self.canvas.move(self.id, 245, 100)
            starts = [-3, -2, -1, 1, 2, 3, 9, -5]
            random.shuffle(starts)
            self.x = starts[0]
            self.y = -3
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()
            #global self.hit_bottom
            self.hit_bottom = False


        def hit_paddle(self, pos):
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                    global score
                    global j
                    score = score + 1
                    canvas.delete(j)
                    j = canvas.create_text(30, 10, text=("Score", score), font=("Comic Sans", 10))
                    if (score % 10 == 0):
                        global w
                        global nivel
                        nivel = nivel + 1
                        w = canvas.create_text(250, 200, text=('Nivel', nivel), font=("Comic Sans", 50))
                        time.sleep(1)
                        #canvas.delete(w)
                    return True
                return False    


                 

        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            global x
            global xx
            x = 2
            xx = -2
            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.y = x
            if pos[3] >= self.canvas_height:
                self.hit_bottom = True
            if self.hit_bottom == True:
                global f
                f = canvas.create_text(250, 200, text=("Game Over"), font=("Comic Sans", 50))
                global nivel
                nivel = 1
                pass
            if self.hit_paddle(pos) == True:
                self.y = xx
            if pos[0] <= 0:
                self.x = x
            if pos[2] >= self.canvas_width:
                self.x = xx


    
    class Paddle:
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
            self.canvas.move(self.id, 200, 300)
            self.x = 0
            self.canvas_width = self.canvas.winfo_width()
            self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
            self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

        def draw(self):
            self.canvas.move(self.id, self.x, 0)
            pos = self.canvas.coords(self.id)
            if pos[0] <= 0:
                self.x = 0
            elif pos[2] >= self.canvas_width:
                self.x = 0

        def turn_left(self, evt):
            self.x = -3


        def turn_right(self, evt):
            self.x = 3


    def start_game():
        
        canvas.delete("all")
        tk.update()
        paddle = Paddle(canvas, 'red')
        ball = Ball(canvas, paddle, 'red')
        #ball2 = Ball(canvas, paddle, 'blue')
        global score
        score = 0
        global j
        j = canvas.create_text(30, 10, text=("Score", score), font=("Comic Sans", 10))

    
        while 1:
            if ball.hit_bottom == False:
                ball.draw()
                paddle.draw()

                
            '''
            if ball2.hit_bottom == False:
                ball2.draw()
                paddle.draw()

    
            ball2.draw()
            '''
            ball.draw()
            paddle.draw()
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
        

    
    tk = Tk()
    tk.title("Game")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    btn = Button(tk, text="Start", command=start_game)
    #w = canvas.create_text(200, 200, text=('Nivel', nivel), font=("Comic Sans", 50))

    btn.pack()
    canvas.pack()
    tk.update()
    
        


'''
tk = Tk()
btn = Button(tk, text="Start", command=iniciar)
btn.pack()
''' 
iniciar()


