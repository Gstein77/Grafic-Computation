import numpy as np;
import math;

class Matrizes:
    def multiplicarMatrizQ(m1,m2):
        tam = len(m1)
        mf = [[0]*tam]*tam
        for i in range(tam):
            for j in range(tam):
                for k in range(tam):
                    mf[i][j]+=m1[i][k]*m2[k][j]
        return mf

class DoisD:
    def getMatrizT(tx, ty):
        return [[1,0,tx],[0,1,ty],[0,0,1]]
    
    def getMatrizS(sx, sy):
        return [[sx,0,0],[0,sy,0],[0,0,1]]
    
    def getMatrizR(ang):
        return [[math.cos(ang), -math.sen(ang), 0],
        [math.sen(ang),math.cos(ang),0],[0,0,1]]

class TresD:
    def getMatrizT(tx, ty, tz):
        return [[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]]
    
    def getMatrizS(sx, sy, sz):
        return [[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]]
    
    def getMatrizRZ(ang):
        return [[math.cos(ang), -math.sen(ang), 0,0],
        [math.sen(ang),math.cos(ang),0,0],[0,0,1,0],[0,0,0,1]]
    
    def getMatrizRX(ang):
        return [[1,0,0,0],[0,math.cos(ang), -math.sen(ang), 0],
        [0,math.sen(ang),math.cos(ang),0],[0,0,0,1]]
    
    def getMatrizRY(ang):
        return [[math.cos(ang),0, math.sen(ang), 0],
        [0,1,0,0],[math.sen(ang),0,math.cos(ang),0],[0,0,0,1]]
    
    def getMatrizRX(b,c,d):
        return [[1,0,0,0],[0,c/d,-b/d,0],[0,b/d,c/d,0],[0,0,0,1]]

    def getMatrizRY(a,d):
        return [[d,0,-a,0],[0,1,0,0],[a,0,d,0],[0,0,0,1]]

    def getMatrizR(ang, p1, p2):
        v = [p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2]]
        vu = math.sqrt(v[0]**2+v[1]**2+v[2]**2)
        u = [v[0]/vu,v[1]/vu,v[2]/vu]
        u.append(math.sqrt(v[1]**2+v[2]**2))
        mx = getMatrizRX(u[1],u[2],u[3])
        my = getMatrizRY(u[0],u[3])
        mz = getMatrizRZ(ang)
        mf = multiplicarMatrizQ(mx,my)
        mf = multiplicarMatrizQ(mf,mz)
        mx = getMatrizRX(-u[1],-u[2],-u[3])
        my = getMatrizRY(-u[0],-u[3])
        mf = multiplicarMatrizQ(mf,my)
        mf = multiplicarMatrizQ(mf,mx)
        return mf

class main:
    print("Digite '2' para 2d ou '3' para 3d: ")
    tam = int(scan())
    aux = tam+1
    mf = [[]*aux]*aux
    for i in range(aux):
        mf[i][i] = 1
    while aux != 0:
        print("Qual operação deseja realizar?")
        print("0 = Sair\n1 = Translação\n2 = Rotação\n3 = Escala")
        print("4 = Translação Inversa\n5 = Rotação Inversa\n6 = Escala Inversa")
        aux = int(scan())
        if aux == 1:
            print("Informe os valores: ")
            vx = scan()
            vy = scan()
            ma = none
            if tam == 3:
                ma = getMatrizT(vx,vy)
            elif tam == 4:
                vz = scan()
                ma = getMatrizT(vx,vy,vz)
            mf = multiplicarMatrizQ(mf,ma)
        elif aux == 2:
            print("Informe o ângulo: ")
            va = scan()
            ma = none
            if tam == 2:
                ma = getMatrizR(va)
            elif tam == 3:
                p1 = []*tam
                p2 = []*tam
                print("Informe os valores do ponto 1 do eixo: ")
                for i in p1:
                    p1[i] = scan()
                print("Informe os valores do ponto 2 do eixo: ")
                for i in p2:
                    p2[i] = scan()
                ma = getMatrizR(va,p1,p2)
            mf = mu