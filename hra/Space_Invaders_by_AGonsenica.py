import tkinter,random

class Program:
        def __init__(self):
            master = tkinter.Tk()
            photo = tkinter.PhotoImage(file = 'alien.png')
            master.iconphoto(False, photo)
            master.title("Space_Invaders")
            Hracia_plocha.canvas = tkinter.Canvas(master,height=600,width=500, bg="black")
            Hracia_plocha.canvas.pack()
            Hracia_plocha()
        
class Hracia_plocha:
        
        canvas = None
        
        def posun(self,event):
            x, y = event.x, event.y
            self.x,self.y=x,y
            if 20<x<480 and 400<y<580:
                self.canvas.coords(self.a, x,y)
            self.canvas.delete('stit')
            if self.shield>0:
                self.canvas.create_line(x-20, y-30, x+20,y-30,width=10,fill="blue",tag="stit")
                
        def strela(self,event):
            x, y = event.x, event.y
            if 20<x<480 and 400<y<580:
                self.canvas.after(0)
                sid=self.canvas.create_line(x, y-20, x,y-10,width=5,fill="yellow",tag="strela")
                self.zoz_striel.append(sid)
                
        def strela_leti(self):
            for strela in self.zoz_striel:
                if self.stop==0:
                    return
                self.canvas.move(strela,0,-20)
            self.canvas.update()

        def aliens(self):
            self.obr1 = tkinter.PhotoImage(file='alien.png')
            for i in range (8):
                if self.stop==0:
                    return
                aid=self.canvas.create_image(50+60*i, 100, image=self.obr1,tags='alien') 
                self.zoz_aliens.append(aid)
                
        def uhyb(self):
                for i,strela in enumerate(self.zoz_striel):
                    for a,ali in enumerate(self.zoz_aliens):
                        if self.canvas.coords(ali)[0]-22<self.canvas.coords(strela)[0]<self.canvas.coords(ali)[0]+22 and self.canvas.coords(ali)[1]+22<self.canvas.coords(strela)[1]<self.canvas.coords(ali)[1]+55:
                                if ali-1 not in self.zoz_aliens:
                                        if self.canvas.coords(ali)[0]!=50:
                                                if random.randint(0,4)<3:
                                                        self.canvas.move(ali,-60,0)
                                                        ali=ali-1
                                if ali+1 not in self.zoz_aliens:
                                        if self.canvas.coords(ali)[0]!=470:
                                                if random.randint(0,4)<3:
                                                        self.canvas.move(ali,+60,0)
                                                        ali=ali+1

        def hit(self):
            for i,strela in enumerate(self.zoz_striel):
                    for a,ali in enumerate(self.zoz_aliens):
                                                
                                
                        if self.canvas.coords(ali)[0]-22<self.canvas.coords(strela)[0]<self.canvas.coords(ali)[0]+22 and self.canvas.coords(ali)[1]<self.canvas.coords(strela)[1]<self.canvas.coords(ali)[1]+23:
                            self.zoz_striel.pop(i)
                            self.canvas.delete(strela)
                            if random.randint(0,10)==5:
                                m=self.canvas.create_rectangle(self.canvas.coords(ali)[0], self.canvas.coords(ali)[1], self.canvas.coords(ali)[0]+20,self.canvas.coords(ali)[1]+20,width=0,fill='blue')
                                self.canvas.update()
                                self.zoz_spec.append([m,0])
                            self.zoz_aliens.pop(a)
                            self.canvas.create_image(self.canvas.coords(ali)[0],self.canvas.coords(ali)[1],image=self.obr2,tags='dest')
                            self.canvas.delete(ali)
                            return
                        
        def respown(self):
            for alien in self.zoz_aliens:
                    self.canvas.move(alien,0,50)
            self.rychlost+=round(100*self.koef)
            if self.koef>0.6:
                self.koef*=0.95
            self.canvas.update()
            for i in range (8):
                if self.stop==0:
                    return
                aid=self.canvas.create_image(50+60*i, 100, image=self.obr1,tags='alien') 
                self.zoz_aliens.append(aid)
                
        def alien_strela(self):
            if self.stop==0:
                    return
            if len(self.zoz_aliens)!=0:
                a=random.choice(self.zoz_aliens)
                odchylka=0
                sa=self.canvas.create_line(self.canvas.coords(a)[0], self.canvas.coords(a)[1], self.canvas.coords(a)[0]+odchylka,self.canvas.coords(a)[1]+10,width=5,fill=random.choice(('#fe0000','#fe00f6','#0bff01')),tags='sta')
                self.canvas.update()
                self.zoz_astriel.append([sa,odchylka])
                
        def strelaali_leti(self):
            for strela in self.zoz_astriel:
                if self.stop==0:
                    return
                x1,y1,x2,y2=self.canvas.coords(strela[0])
                odch=(self.x-x1)//20 #navadzanie
                self.canvas.coords(strela[0],x1+odch,y1+12,x1+odch+odch/5,y2+12)
            for strela in self.zoz_spec:
                if self.stop==0:
                    return
                self.canvas.move(strela[0],strela[1],+10)
            self.canvas.update()
            
        def hita(self):
            for i,strela in enumerate(self.zoz_astriel):
                if self.stop==0:
                    return
                if self.canvas.coords(self.a)[0]-25<self.canvas.coords(strela[0])[0]<self.canvas.coords(self.a)[0]+25 and self.canvas.coords(self.a)[1]-20<self.canvas.coords(strela[0])[1]<self.canvas.coords(self.a)[1]+10:
                    self.zoz_astriel.pop(i)
                    self.canvas.delete(strela[0])
                    if self.shield==0:
                        self.zivotdole()
                        
            for i,ali in enumerate(self.zoz_aliens):
                if self.stop==0:
                    return
                if self.canvas.coords(self.a)[0]-25<self.canvas.coords(ali)[0]<self.canvas.coords(self.a)[0]+25 and self.canvas.coords(self.a)[1]-40<self.canvas.coords(ali)[1]<self.canvas.coords(self.a)[1]+10:
                    if self.shield==0:
                        self.game_over()
                        
            for i,ali in enumerate(self.zoz_aliens):
                if self.stop==0:
                    return
                if self.canvas.coords(ali)[1]==600:
                    self.game_over()
                
            for i,strela in enumerate(self.zoz_spec):
                if self.stop==0:
                    return
                if self.canvas.coords(self.a)[0]-25<self.canvas.coords(strela[0])[0]+10<self.canvas.coords(self.a)[0]+25 and self.canvas.coords(self.a)[1]-40<self.canvas.coords(strela[0])[1]+10<self.canvas.coords(self.a)[1]+10:
                    self.tshoting+=self.tshot*2
                    self.zoz_spec.pop(i)
                    self.canvas.delete(strela[0])
                    self.shield+=self.tshot*20
                    
        def zbytocnestrely(self):
            for i,strela in enumerate(self.zoz_astriel):
                if self.stop==0:
                    return
                if self.canvas.coords(strela[0])[1]>600:
                    self.zoz_astriel.pop(i)
                    self.canvas.delete(strela[0])
                    self.canvas.update()
            for i,strela in enumerate(self.zoz_striel):
                if self.stop==0:
                    return
                if self.canvas.coords(strela)[1]<0:
                    self.zoz_striel.pop(i)
                    self.canvas.delete(strela)
                    
        def zivot(self):
            self.obrz = tkinter.PhotoImage(file='srdce.png')
            self.zz=Zivot(self.pzivot)
            for i in range(0,self.pzivot):
                if self.stop==0:
                    return
                srd=self.canvas.create_image(30+30*i, 30, image=self.obrz) 
                self.zivoty.append(srd)
                
        def zivotdole(self):
            self.zz.uber()
            self.canvas.delete(self.zivoty[-1])
            del self.zivoty[-1]
            if self.zz.pocet()==0:
                self.game_over()
                
        def game_over(self):
            self.stop=0
            self.canvas.delete('all')
            self.canvas.create_text(250,235,fill="white",font="Fixedsys 20",text='Game Over')
            self.canvas.create_text(250,335,fill="white",font="Fixedsys 20",text=f'Earned: {int(int(self.sk*(1+self.smu/10))/10)}')
            self.canvas.create_text(250,285,fill="white",font="Fixedsys 20",text=f'Score: {int(self.sk*(1+self.smu/10))}')
            self.canvas.create_image(330+len(str(int(int(self.sk*(1+self.smu/10))/10)))*10, 335, image=self.minca)
            if int(self.sk*(1+self.smu/10))>self.hs:
                self.hs=int(self.sk*(1+self.smu/10))
            with open("save.txt",'w') as subor:
                subor.write(f'{self.coins+int(int(self.sk*(1+self.smu/10))/10)} {self.pzivot} {self.tshot} {self.smu} {self.hs}')
            self.canvas.after(1000,self.go)
            
        def go(self):
            self.canvas.delete('all')
            self.canvas.after(1000,self.naspat(int(int(self.sk*(1+self.smu/10))/10),self.pzivot,self.tshot,self.smu,self.hs))
                
        def alienanim(self):
            if self.stop==0:
                    return
            for alien in self.zoz_aliens:
                self.canvas.create_image(self.canvas.coords(alien)[0], self.canvas.coords(alien)[1], image=self.obraza,tags='obraza')

        def score(self):
                self.canvas.delete("skore")
                if self.stop==0:
                    return
                self.canvas.create_text(400,30,text=f"score: {int(self.sk*(1+self.smu/10))}",tags="skore",fill="white",font="Fixedsys 20")

        def hra(self):
            self.canvas.delete('dest')
            if self.cykly%15==5:
                self.canvas.delete('obraza')
            self.strela_leti()
            self.uhyb()
            self.hit()
            self.cykly+=1
            if self.cykly==self.rychlost:
                self.respown()
            if self.cykly%10==1:
                self.alien_strela()
            self.strelaali_leti()
            self.hita()
            self.zbytocnestrely()
            if self.cykly%15==2:
                self.alienanim()
            self.sk+=1
            self.score()
            if self.shield>0:
                self.shield-=1
            if self.stop==0:
                    return
            self.canvas.after(60, self.hra)

        def __init__(self):
            self.logo = tkinter.PhotoImage(file='logo.png')
            logo=self.canvas.create_image(250, 100, image=self.logo)
            self.canvas.bind('<ButtonPress>', self.newgame)
            self.canvas.create_rectangle(100,210,400,280,outline='white',width=4)
            self.canvas.create_text(250,245,fill="white",font="Fixedsys 20",text='New Game')
            self.canvas.create_rectangle(100,300,400,370,outline='white',width=4)
            self.canvas.create_text(250,335,fill="white",font="Fixedsys 20",text='Load Game')
            self.canvas.create_text(250,435,fill="white",font="Fixedsys 10",text='Instructions: Shoot aliens, avoid shots or touch from aliens,')
            self.canvas.create_text(250,455,fill="white",font="Fixedsys 10",text='dead alien drops blue square whitch activate SHIELD powerup,')
            self.canvas.create_text(250,475,fill="white",font="Fixedsys 10",text='upgrade your shield, number of lifes, score multiplier')
            self.canvas.create_text(250,495,fill="white",font="Fixedsys 10",text='and earn highest highscore possible')
            self.canvas.create_text(250,590,fill="white",font="Fixedsys 10",text='Made by Adam Gonsenica')
            self.coins=0
            self.x,self.y=0,0
            self.minca = tkinter.PhotoImage(file='minca.png')

        def newgame(self,event=None):
            if 100<event.x<400 and 210<event.y<280 and event!=None:
                self.canvas.delete('all')
                self.pzivot=1
                self.tshot=1
                self.smu=0
                self.hs=0
                self.canvas.bind('<ButtonPress>', self.hraj)
                self.canvas.create_text(250,35,fill="white",font="Fixedsys 20",text=f'Coins: {self.coins}')
                self.canvas.create_text(260,75,fill="white",font="Fixedsys 20",text=f'Highscore: {self.hs}')
                self.canvas.create_image(330+len(str(self.coins))*10, 35, image=self.minca)
                self.canvas.create_rectangle(100,465,400,535,outline='white',width=5)
                self.canvas.create_text(250,500,fill="white",font="Fixedsys 20",text='Play')
                self.canvas.create_rectangle(30,365,170,435,outline='white',width=5)
                self.canvas.create_rectangle(180,365,470,435,outline='white',width=5)
                self.canvas.create_text(325,400,fill="white",font="Fixedsys 15",text=f'Score multiplier: {1+self.smu/10}x, price: {20*2**self.smu}')
                self.canvas.create_text(100,400,fill="white",font="Fixedsys 20",text='Upgrade')
                self.canvas.create_rectangle(30,265,170,335,outline='white',width=5)
                self.canvas.create_rectangle(180,265,470,335,outline='white',width=5)
                self.canvas.create_text(325,300,fill="white",font="Fixedsys 15",text=f'Tripleshot: {self.tshot*2}s, price: {20*2**self.tshot}')
                self.canvas.create_text(100,300,fill="white",font="Fixedsys 20",text='Upgrade')
                self.canvas.create_rectangle(30,165,170,235,outline='white',width=5)
                self.canvas.create_rectangle(180,165,470,235,outline='white',width=5)
                self.canvas.create_text(325,200,fill="white",font="Fixedsys 15",text=f'Hearts: {self.pzivot}x, price: {20*2**self.pzivot}')
                self.canvas.create_text(100,200,fill="white",font="Fixedsys 20",text='Upgrade')
            
            if 100<event.x<400 and 300<event.y<370 and event!=None:
                print('load')
                with open("save.txt",'r') as subor:
                    szoz=subor.readline().split()
                    a=int(szoz[0])
                    z=int(szoz[1])
                    t=int(szoz[2])
                    smu=int(szoz[3])
                    hs=int(szoz[4])
                    self.naspat(a,z,t,smu,hs)
   
        def naspat(self,sk,z,t,smu,hs):
            self.coins+=sk
            self.pzivot=z
            self.tshot=t
            self.smu=smu
            self.hs=hs
            self.canvas.delete('all')
            self.canvas.config(cursor='')
            self.canvas.bind('<ButtonPress>', self.hraj)
            self.canvas.create_text(250,35,fill="white",font="Fixedsys 20",text=f'Coins: {self.coins}',tags='pc')
            self.canvas.create_text(250,85,fill="white",font="Fixedsys 20",text=f'Highscore: {self.hs}')
            self.canvas.create_image(330+len(str(self.coins))*10, 35, image=self.minca)
            self.canvas.create_rectangle(100,465,400,535,outline='white',width=5)
            self.canvas.create_text(250,500,fill="white",font="Fixedsys 20",text='Play')
            self.canvas.create_rectangle(30,365,170,435,outline='white',width=5)
            self.canvas.create_rectangle(180,365,470,435,outline='white',width=5)
            self.canvas.create_text(325,400,fill="white",font="Fixedsys 15",text=f'Score multiplier: {1+self.smu/10}x, price: {20*2**self.smu}',tags='sm')
            self.canvas.create_text(100,400,fill="white",font="Fixedsys 20",text='Upgrade')
            self.canvas.create_rectangle(30,265,170,335,outline='white',width=5)
            self.canvas.create_rectangle(180,265,470,335,outline='white',width=5)
            self.canvas.create_text(325,300,fill="white",font="Fixedsys 15",text=f'Shield: {self.tshot*2}s, price: {20*2**self.tshot}',tags='sz')
            self.canvas.create_text(100,300,fill="white",font="Fixedsys 20",text='Upgrade')
            self.canvas.create_rectangle(30,165,170,235,outline='white',width=5)
            self.canvas.create_rectangle(180,165,470,235,outline='white',width=5)
            self.canvas.create_text(325,200,fill="white",font="Fixedsys 15",text=f'Hearts: {self.pzivot}x, price: {20*2**self.pzivot}',tags='pz')
            self.canvas.create_text(100,200,fill="white",font="Fixedsys 20",text='Upgrade')
                
        def hraj(self,event):
            if 100<event.x<400 and 465<event.y<535:
                self.stop=1
                self.canvas.delete('all')
                self.obr = tkinter.PhotoImage(file='raketa.png')
                self.obr2 = tkinter.PhotoImage(file='alienm1.png')
                self.obraza = tkinter.PhotoImage(file='alienanim.png')
                self.a=self.canvas.create_image(250, 500, image=self.obr,tags='raketa')
                self.canvas.bind('<Motion>', self.posun)
                self.canvas.bind('<ButtonPress>', self.strela)
                self.zoz_striel=[]
                self.zoz_aliens=[]
                self.zoz_astriel=[]
                self.zoz_spec=[]
                self.zivoty=[]
                self.tshoting=0
                self.cykly=0
                self.rychlost=100
                self.koef=1
                self.aliens()
                self.shield=0
                self.zivot()
                self.canvas.config(cursor='none')
                self.sk = 0
                self.score()
                self.hra()
                tkinter.mainloop()

            if 30<event.x<170 and 165<event.y<235:
                if self.coins>=20*2**self.pzivot:
                    self.canvas.delete('pc')
                    self.coins-=20*2**self.pzivot
                    self.canvas.create_text(250,35,fill="white",font="Fixedsys 20",text=f'Coins: {self.coins}',tags='pc')
                    self.pzivot+=1
                    self.canvas.delete('pz')
                    self.canvas.create_text(325,200,fill="white",font="Fixedsys 15",text=f'Hearts: {self.pzivot}x, price: {20*2**self.pzivot}',tags='pz')
                    with open("save.txt",'w') as subor:
                        subor.write(f'{self.coins} {self.pzivot} {self.tshot} {self.smu} {self.hs}')
                        
            if 30<event.x<170 and 265<event.y<335:
                if self.coins>=20*2**self.tshot:
                    self.canvas.delete('pc')
                    self.coins-=20*2**self.tshot
                    self.canvas.create_text(250,35,fill="white",font="Fixedsys 20",text=f'Coins: {self.coins}',tags='pc')
                    self.tshot+=1
                    self.canvas.delete('sz')
                    self.canvas.create_text(325,300,fill="white",font="Fixedsys 15",text=f'Shield: {self.tshot*2}s, price: {20*2**self.tshot}',tags='sz')
                    with open("save.txt",'w') as subor:
                        subor.write(f'{self.coins} {self.pzivot} {self.tshot} {self.smu} {self.hs}')

            if 30<event.x<170 and 365<event.y<435:
                if self.coins>=20*2**self.smu:
                    self.canvas.delete('pc')
                    self.coins-=20*2**self.smu
                    self.canvas.create_text(250,35,fill="white",font="Fixedsys 20",text=f'Coins: {self.coins}',tags='pc')
                    self.smu+=1
                    self.canvas.delete('sm')
                    self.canvas.create_text(325,400,fill="white",font="Fixedsys 15",text=f'Score multiplier: {1+self.smu/10}x, price: {20*2**self.smu}',tags='sm')
                    with open("save.txt",'w') as subor:
                        subor.write(f'{self.coins} {self.pzivot} {self.tshot} {self.smu} {self.hs}')

    
    
class Zivot:
            def __init__(self,pzivot):
                self.pzivotov=pzivot
            def pocet(self):
                return self.pzivotov
            def uber(self):
                self.pzivotov-=1
Program()

