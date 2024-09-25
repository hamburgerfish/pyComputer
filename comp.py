
### TRANSISTOR ###
class transistor:
    def r(self, b, c):
        assert(b in (0,1) and c in (0,1))
        self.b = b
        self.c = c
        self.e = b and c
        return self.e
### TRANSISTOR ###
    
### LOGIC GATES ###
class inv: #INVERTOR
    def r(self, a):
        self.out = int(not a)
        return self.out

class gAnd: # AND GATE
    def __init__(self):
        self.t0 = transistor()
        self.t1 = transistor()

    def r(self, a, b):
        i = self.t0.r(a, 1)
        self.out = self.t1.r(b, i)
        return self.out
    
class gOr: # OR GATE
    def __init__(self):
        self.t0 = transistor()
        self.t1 = transistor()

    def r(self, a, b):
        i0 = self.t0.r(a, 1)
        i1 = self.t1.r(b, 1)
        self.out = i0
        if self.out == 0:
            self.out = i1
        return self.out
    
class gOr8: # 8 BIT OR GATE
    def __init__(self):
        self.go0 = gOr()
        self.go1 = gOr()
        self.go2 = gOr()
        self.go3 = gOr()
        self.go4 = gOr()
        self.go5 = gOr()
        self.go6 = gOr()
    
    def r(self, a0,a1,a2,a3,a4,a5,a6,a7):
        i0 = self.go0.r(a0, a1)
        i1 = self.go1.r(a2, a3)
        i2 = self.go2.r(a4, a5)
        i3 = self.go3.r(a6, a7)
        i4 = self.go4.r(i0, i1)
        i5 = self.go5.r(i2, i3)
        self.out = self.go6.r(i4, i5)
        return self.out
    
class gXor: # XOR GATE
    def __init__(self):
        self.go0 = gOr()
        self.inv0 = inv()
        self.ga0 = gAnd()
        self.ga1 = gAnd()

    def r(self, a, b):
        i0 = self.go0.r(a, b)
        i1 = self.inv0.r(self.ga0.r(a, b))
        self.out = self.ga1.r(i0, i1)
        return self.out
### LOGIC GATES ###

### ARITHMETIC OPERATIONS ###
class adder: # ADDER/SUBTRACTOR
    def __init__(self):
        self.gx0 = gXor()
        self.gx1 = gXor()
        self.ga0 = gAnd()
        self.ga1 = gAnd()
        self.go0 = gOr()

    def r(self, a, b, cin):
        i0 = self.gx0.r(a, b)
        i1 = self.ga0.r(a, b)
        self.sum = self.gx1.r(i0, cin)
        i2 = self.ga1.r(i0, cin)
        self.cout = self.go0.r(i1, i2)
        return self.sum, self.cout
    
class adder8: # 8 BIT ADDER/SUBTRACTOR
    def __init__(self):
        self.gx0 = gXor()
        self.gx1 = gXor()
        self.gx2 = gXor()
        self.gx3 = gXor()
        self.gx4 = gXor()
        self.gx5 = gXor()
        self.gx6 = gXor()
        self.gx7 = gXor()
        self.gx8 = gXor()
        self.gx9 = gXor()
        self.add0 = adder()
        self.add1 = adder()
        self.add2 = adder()
        self.add3 = adder()
        self.add4 = adder()
        self.add5 = adder()
        self.add6 = adder()
        self.add7 = adder()

    def r(self, a0,a1,a2,a3,a4,a5,a6,a7, b0,b1,b2,b3,b4,b5,b6,b7, cin, sub):
        cin = self.gx0.r(cin, sub)
        b0 = self.gx1.r(b0, sub)
        b1 = self.gx2.r(b1, sub)
        b2 = self.gx3.r(b2, sub)
        b3 = self.gx4.r(b3, sub)
        b4 = self.gx5.r(b4, sub)
        b5 = self.gx6.r(b5, sub)
        b6 = self.gx7.r(b6, sub)
        b7 = self.gx8.r(b7, sub)
        self.sum7, i0 = self.add0.r(a7, b7, cin)
        self.sum6, i0 = self.add1.r(a6, b6, i0)
        self.sum5, i0 = self.add2.r(a5, b5, i0)
        self.sum4, i0 = self.add4.r(a4, b4, i0)
        self.sum3, i0 = self.add4.r(a3, b3, i0)
        self.sum2, i0 = self.add4.r(a2, b2, i0)
        self.sum1, i0 = self.add4.r(a1, b1, i0)
        self.sum0, i0 = self.add4.r(a0, b0, i0)
        self.cout = self.gx9.r(i0, sub)
        return self.sum0,self.sum1,self.sum2,self.sum3,self.sum4,self.sum5,self.sum6,self.sum7, self.cout
    
class band: # BIT WISE AND
    def __init__(self):
        self.ga0 = gAnd()
        self.ga1 = gAnd()
        self.ga2 = gAnd()
        self.ga3 = gAnd()
        self.ga4 = gAnd()
        self.ga5 = gAnd()
        self.ga6 = gAnd()
        self.ga7 = gAnd()

    def r(self, a0,a1,a2,a3,a4,a5,a6,a7, b0,b1,b2,b3,b4,b5,b6,b7):
        out0 = self.ga0.r(a0, b0)
        out1 = self.ga1.r(a1, b1)
        out2 = self.ga2.r(a2, b2)
        out3 = self.ga3.r(a3, b3)
        out4 = self.ga4.r(a4, b4)
        out5 = self.ga5.r(a5, b5)
        out6 = self.ga6.r(a6, b6)
        out7 = self.ga7.r(a7, b7)
        return out0,out1,out2,out3,out4,out5,out6,out7

class bor: # BIT WISE OR
    def __init__(self):
        self.go0 = gOr()
        self.go1 = gOr()
        self.go2 = gOr()
        self.go3 = gOr()
        self.go4 = gOr()
        self.go5 = gOr()
        self.go6 = gOr()
        self.go7 = gOr()

    def r(self, a0,a1,a2,a3,a4,a5,a6,a7, b0,b1,b2,b3,b4,b5,b6,b7):
        out0 = self.go0.r(a0, b0)
        out1 = self.go1.r(a1, b1)
        out2 = self.go2.r(a2, b2)
        out3 = self.go3.r(a3, b3)
        out4 = self.go4.r(a4, b4)
        out5 = self.go5.r(a5, b5)
        out6 = self.go6.r(a6, b6)
        out7 = self.go7.r(a7, b7)
        return out0,out1,out2,out3,out4,out5,out6,out7
    
class bxor: # BIT WISE XOR
    def __init__(self):
        self.gx0 = gXor()
        self.gx1 = gXor()
        self.gx2 = gXor()
        self.gx3 = gXor()
        self.gx4 = gXor()
        self.gx5 = gXor()
        self.gx6 = gXor()
        self.gx7 = gXor()

    def r(self, a0,a1,a2,a3,a4,a5,a6,a7, b0,b1,b2,b3,b4,b5,b6,b7):
        out0 = self.gx0.r(a0, b0)
        out1 = self.gx1.r(a1, b1)
        out2 = self.gx2.r(a2, b2)
        out3 = self.gx3.r(a3, b3)
        out4 = self.gx4.r(a4, b4)
        out5 = self.gx5.r(a5, b5)
        out6 = self.gx6.r(a6, b6)
        out7 = self.gx7.r(a7, b7)
        return out0,out1,out2,out3,out4,out5,out6,out7

class binv: # BIT WISE INVERTOR
    def __init__(self):
        self.gi0 = inv()
        self.gi1 = inv()
        self.gi2 = inv()
        self.gi3 = inv()
        self.gi4 = inv()
        self.gi5 = inv()
        self.gi6 = inv()
        self.gi7 = inv()

    def r(self, a0,a1,a2,a3,a4,a5,a6,a7, b0,b1,b2,b3,b4,b5,b6,b7):
        out0 = self.gi0.r(a0)
        out1 = self.gi1.r(a1)
        out2 = self.gi2.r(a2)
        out3 = self.gi3.r(a3)
        out4 = self.gi4.r(a4)
        out5 = self.gi5.r(a5)
        out6 = self.gi6.r(a6)
        out7 = self.gi7.r(a7)
        return out0,out1,out2,out3,out4,out5,out6,out7

class binc: # INCREMENT
    def __init__(self):
        self.add = adder8()

    def r(self, a0,a1,a2,a3,a4,a5,a6,a7, b0,b1,b2,b3,b4,b5,b6,b7):
        self.out = self.add.r(a0,a1,a2,a3,a4,a5,a6,a7, 0,0,0,0,0,0,0,1, 0, 0)
        return self.out
    
class bdec: # DECREMENT
    def __init__(self):
        self.add = adder8()

    def r(self, a0,a1,a2,a3,a4,a5,a6,a7, b0,b1,b2,b3,b4,b5,b6,b7):
        self.out = self.add.r(a0,a1,a2,a3,a4,a5,a6,a7, 0,0,0,0,0,0,0,1, 0, 1)
        return self.out
### ARITHMETIC OPERATIONS ###

### 3 TO 8 BINARY DECODER ###
class bdecoder: 
    def __init__(self):
        self.in0 = inv()
        self.in1 = inv()
        self.in2 = inv()
        self.ga0 = gAnd()
        self.ga01 = gAnd()
        self.ga1 = gAnd()
        self.ga11 = gAnd()
        self.ga2 = gAnd()
        self.ga21 = gAnd()
        self.ga3 = gAnd()
        self.ga31 = gAnd()
        self.ga4 = gAnd()
        self.ga41 = gAnd()
        self.ga5 = gAnd()
        self.ga51 = gAnd()
        self.ga6 = gAnd()
        self.ga61 = gAnd()
        self.ga7 = gAnd()
        self.ga71 = gAnd()

    def r(self, i2, i1, i0):
        t0 = self.in0.r(i0)
        t1 = i0
        t2 = self.in1.r(i1)
        t3 = i1
        t4 = self.in2.r(i2)
        t5 = i2
        out0 = self.ga01.r(self.ga0.r(t0, t2), t4)
        out1 = self.ga11.r(self.ga1.r(t1, t2), t4)
        out2 = self.ga21.r(self.ga2.r(t0, t3), t4)
        out3 = self.ga31.r(self.ga0.r(t1, t3), t4)
        out4 = self.ga01.r(self.ga0.r(t0, t2), t5)
        out5 = self.ga11.r(self.ga1.r(t1, t2), t5)
        out6 = self.ga21.r(self.ga2.r(t0, t3), t5)
        out7 = self.ga31.r(self.ga0.r(t1, t3), t5)
        return out0, out1, out2, out3, out4, out5, out6, out7
### 3 TO 8 BINARY DECODER ###

### 8 TO 1 MULTIPLEXER ###
class mux8:
    def __init__(self):
        self.bd0 = bdecoder()
        self.band0 = band()
        self.band1 = band()
        self.band2 = band()
        self.band3 = band()
        self.band4 = band()
        self.band5 = band()
        self.band6 = band()
        self.gor0 = gOr8()
        self.gor1 = gOr8()
        self.gor2 = gOr8()
        self.gor3 = gOr8()
        self.gor4 = gOr8()
        self.gor5 = gOr8()
        self.gor6 = gOr8()
        self.gor7 = gOr8()
    
    def r(self, o2, o1, o0,
          a0, a1, a2, a3, a4, a5, a6, a7,
          b0, b1, b2, b3, b4, b5, b6, b7,
          c0, c1, c2, c3, c4, c5, c6, c7,
          d0, d1, d2, d3, d4, d5, d6, d7,
          e0, e1, e2, e3, e4, e5, e6, e7,
          f0, f1, f2, f3, f4, f5, f6, f7,
          g0, g1, g2, g3, g4, g5, g6, g7,
          h0, h1, h2, h3, h4, h5, h6, h7):
        op0, op1, op2, op3, op4, op5, op6, op7 = self.bd0.r(o2, o1, o0)
        a0, a1, a2, a3, a4, a5, a6, a7 = self.band0.r(a0, a1, a2, a3, a4, a5, a6, a7, op0, op0, op0, op0, op0, op0, op0, op0)
        b0, b1, b2, b3, b4, b5, b6, b7 = self.band0.r(b0, b1, b2, b3, b4, b5, b6, b7, op1, op1, op1, op1, op1, op1, op1, op1)
        c0, c1, c2, c3, c4, c5, c6, c7 = self.band0.r(c0, c1, c2, c3, c4, c5, c6, c7, op2, op2, op2, op2, op2, op2, op2, op2)
        d0, d1, d2, d3, d4, d5, d6, d7 = self.band0.r(d0, d1, d2, d3, d4, d5, d6, d7, op3, op3, op3, op3, op3, op3, op3, op3)
        e0, e1, e2, e3, e4, e5, e6, e7 = self.band0.r(e0, e1, e2, e3, e4, e5, e6, e7, op4, op4, op4, op4, op4, op4, op4, op4)
        f0, f1, f2, f3, f4, f5, f6, f7 = self.band0.r(f0, f1, f2, f3, f4, f5, f6, f7, op5, op5, op5, op5, op5, op5, op5, op5)
        g0, g1, g2, g3, g4, g5, g6, g7 = self.band0.r(g0, g1, g2, g3, g4, g5, g6, g7, op6, op6, op6, op6, op6, op6, op6, op6)
        h0, h1, h2, h3, h4, h5, h6, h7 = self.band0.r(h0, h1, h2, h3, h4, h5, h6, h7, op7, op7, op7, op7, op7, op7, op7, op7)
        out0 = self.gor0.r(a0, b0, c0, d0, e0, f0, g0, h0)
        out1 = self.gor1.r(a1, b1, c1, d1, e1, f1, g1, h1)
        out2 = self.gor2.r(a2, b2, c2, d2, e2, f2, g2, h2)
        out3 = self.gor3.r(a3, b3, c3, d3, e3, f3, g3, h3)
        out4 = self.gor4.r(a4, b4, c4, d4, e4, f4, g4, h4)
        out5 = self.gor5.r(a5, b5, c5, d5, e5, f5, g5, h5)
        out6 = self.gor6.r(a6, b6, c6, d6, e6, f6, g6, h6)
        out7 = self.gor7.r(a7, b7, c7, d7, e7, f7, g7, h7)
        return out0,out1,out2,out3,out4,out5,out6,out7
### 8 TO 1 MULTIPLEXER ###

### ALU ###
class alu:
    def __init__(self):
        self.o0 = adder8()
        self.o1 = adder8()
        self.o2 = band()
        self.o3 = bor()
        self.o4 = bxor()
        self.o5 = binv()
        self.o6 = binc()
        self.o7 = bdec()
        self.mux0 = mux8()

    def r(self, o2, o1, o0, va0, va1, va2, va3, va4, va5, va6, va7, vb0, vb1, vb2, vb3, vb4, vb5, vb6, vb7):
        a0, a1, a2, a3, a4, a5, a6, a7, _ = self.o0.r(va0, va1, va2, va3, va4, va5, va6, va7, vb0, vb1, vb2, vb3, vb4, vb5, vb6, vb7, 0, 0)
        b0, b1, b2, b3, b4, b5, b6, b7, _ = self.o1.r(va0, va1, va2, va3, va4, va5, va6, va7, vb0, vb1, vb2, vb3, vb4, vb5, vb6, vb7, 0, 1)
        c0, c1, c2, c3, c4, c5, c6, c7 = self.o2.r(va0, va1, va2, va3, va4, va5, va6, va7, vb0, vb1, vb2, vb3, vb4, vb5, vb6, vb7)
        d0, d1, d2, d3, d4, d5, d6, d7 = self.o3.r(va0, va1, va2, va3, va4, va5, va6, va7, vb0, vb1, vb2, vb3, vb4, vb5, vb6, vb7)
        e0, e1, e2, e3, e4, e5, e6, e7 = self.o4.r(va0, va1, va2, va3, va4, va5, va6, va7, vb0, vb1, vb2, vb3, vb4, vb5, vb6, vb7)
        f0, f1, f2, f3, f4, f5, f6, f7 = self.o5.r(va0, va1, va2, va3, va4, va5, va6, va7, vb0, vb1, vb2, vb3, vb4, vb5, vb6, vb7)
        g0, g1, g2, g3, g4, g5, g6, g7, _ = self.o6.r(va0, va1, va2, va3, va4, va5, va6, va7, vb0, vb1, vb2, vb3, vb4, vb5, vb6, vb7)
        h0, h1, h2, h3, h4, h5, h6, h7, _ = self.o7.r(va0, va1, va2, va3, va4, va5, va6, va7, vb0, vb1, vb2, vb3, vb4, vb5, vb6, vb7)
        out0, out1, out2, out3, out4, out5, out6, out7 = self.mux0.r(o2, o1, o0,
                                                                    a0, a1, a2, a3, a4, a5, a6, a7,
                                                                    b0, b1, b2, b3, b4, b5, b6, b7,
                                                                    c0, c1, c2, c3, c4, c5, c6, c7,
                                                                    d0, d1, d2, d3, d4, d5, d6, d7,
                                                                    e0, e1, e2, e3, e4, e5, e6, e7,
                                                                    f0, f1, f2, f3, f4, f5, f6, f7,
                                                                    g0, g1, g2, g3, g4, g5, g6, g7,
                                                                    h0, h1, h2, h3, h4, h5, h6, h7)
        return out0,out1,out2,out3,out4,out5,out6,out7
### ALU ###

### D FLIP FLOP ###
class ff:
    def __init__(self):
        self.ga0 = gAnd()
        self.ga1 = gAnd()
        self.q = 0

    def r(self, d, s, c):
        i0 = self.ga0.r(d, c)
        i1 = self.ga1.r(s, c)
        if i1 == 1:
            self.q = i0
        return self.q
### D FLIP FLOP ###

### 8 BIT REGISTER ###
class reg8:
    def __init__(self):
        self.ff0 = ff()
        self.ff1 = ff()
        self.ff2 = ff()
        self.ff3 = ff()
        self.ff4 = ff()
        self.ff5 = ff()
        self.ff6 = ff()
        self.ff7 = ff()
        self.t0 = transistor()
        self.t1 = transistor()
        self.t2 = transistor()
        self.t3 = transistor()
        self.t4 = transistor()
        self.t5 = transistor()
        self.t6 = transistor()
        self.t7 = transistor()
        self.tc0 = transistor()
        self.tc1 = transistor()
        self.tc2 = transistor()
        self.tc3 = transistor()
        self.tc4 = transistor()
        self.tc5 = transistor()
        self.tc6 = transistor()
        self.tc7 = transistor()

    def r(self, we, re, d0,d1,d2,d3,d4,d5,d6,d7, c):
        assert(we + re < 2)
        self.ff0.r(d0, we, c)
        out0 = self.t0.r(self.ff0.q, re)
        out0 = self.tc0.r(out0, c)
        self.ff1.r(d1, we, c)
        out1 = self.t1.r(self.ff1.q, re)
        out1 = self.tc1.r(out1, c)
        self.ff2.r(d2, we, c)
        out2 = self.t2.r(self.ff2.q, re)
        out2 = self.tc2.r(out2, c)
        self.ff3.r(d3, we, c)
        out3 = self.t3.r(self.ff3.q, re)
        out3 = self.tc3.r(out3, c)
        self.ff4.r(d4, we, c)
        out4 = self.t4.r(self.ff4.q, re)
        out4 = self.tc4.r(out4, c)
        self.ff5.r(d5, we, c)
        out5 = self.t5.r(self.ff5.q, re)
        out5 = self.tc5.r(out5, c)
        self.ff6.r(d6, we, c)
        out6 = self.t6.r(self.ff6.q, re)
        out6 = self.tc6.r(out6, c)
        self.ff7.r(d7, we, c)
        out7 = self.t7.r(self.ff7.q, re)
        out7 = self.tc7.r(out7, c)
        return out0,out1,out2,out3,out4,out5,out6,out7
### 8 BIT REGISTER ###

### MEMORY REGISTER ###
class memreg:
    def __init__(self):
        self.reg0 = reg8()
        self.ga0 = gAnd()
        self.ga1 = gAnd()
        self.ga2 = gAnd()

    def r(self, we, re, x, y, d0,d1,d2,d3,d4,d5,d6,d7, c):
        e = self.ga0.r(x, y)
        we = self.ga1.r(we, e)
        re = self.ga2.r(re, e)
        out = self.reg0.r(we, re, d0,d1,d2,d3,d4,d5,d6,d7, c)
        return out
### MEMORY REGISTER ###

### RAM ###
class ram:
    def __init__(self):
        self.bd0 = bdecoder()
        self.bd1 = bdecoder()
        self.reg00 = memreg()
        self.reg10 = memreg()
        self.reg20 = memreg()
        self.reg30 = memreg()
        self.reg40 = memreg()
        self.reg50 = memreg()
        self.reg60 = memreg()
        self.reg70 = memreg()
        self.reg01 = memreg()
        self.reg11 = memreg()
        self.reg21 = memreg()
        self.reg31 = memreg()
        self.reg41 = memreg()
        self.reg51 = memreg()
        self.reg61 = memreg()
        self.reg71 = memreg()
        self.reg02 = memreg()
        self.reg12 = memreg()
        self.reg22 = memreg()
        self.reg32 = memreg()
        self.reg42 = memreg()
        self.reg52 = memreg()
        self.reg62 = memreg()
        self.reg72 = memreg()
        self.reg03 = memreg()
        self.reg13 = memreg()
        self.reg23 = memreg()
        self.reg33 = memreg()
        self.reg43 = memreg()
        self.reg53 = memreg()
        self.reg63 = memreg()
        self.reg73 = memreg()
        self.reg04 = memreg()
        self.reg14 = memreg()
        self.reg24 = memreg()
        self.reg34 = memreg()
        self.reg44 = memreg()
        self.reg54 = memreg()
        self.reg64 = memreg()
        self.reg74 = memreg()
        self.reg05 = memreg()
        self.reg15 = memreg()
        self.reg25 = memreg()
        self.reg35 = memreg()
        self.reg45 = memreg()
        self.reg55 = memreg()
        self.reg65 = memreg()
        self.reg75 = memreg()
        self.reg06 = memreg()
        self.reg16 = memreg()
        self.reg26 = memreg()
        self.reg36 = memreg()
        self.reg46 = memreg()
        self.reg56 = memreg()
        self.reg66 = memreg()
        self.reg76 = memreg()
        self.reg07 = memreg()
        self.reg17 = memreg()
        self.reg27 = memreg()
        self.reg37 = memreg()
        self.reg47 = memreg()
        self.reg57 = memreg()
        self.reg67 = memreg()
        self.reg77 = memreg()
        self.mux0 = mux8()
        self.mux1 = mux8()
        self.mux2 = mux8()
        self.mux3 = mux8()
        self.mux4 = mux8()
        self.mux5 = mux8()
        self.mux6 = mux8()
        self.mux7 = mux8()
        self.mux8 = mux8()
    
    def r(self, we, re, _1, _2, x2,x1,x0, y2,y1,y0, d0,d1,d2,d3,d4,d5,d6,d7, c):
        assert(we + re < 2)
        assert(_1 == 0 and _2 == 0)
        xt0, xt1, xt2, xt3, xt4, xt5, xt6, xt7 = self.bd0.r(x2,x1,x0)
        yt0, yt1, yt2, yt3, yt4, yt5, yt6, yt7 = self.bd1.r(y2,y1,y0)
        o000, o001, o002, o003, o004, o005, o006, o007 = self.reg00.r(we, re, xt0, yt0, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o100, o101, o102, o103, o104, o105, o106, o107 = self.reg10.r(we, re, xt1, yt0, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o200, o201, o202, o203, o204, o205, o206, o207 = self.reg20.r(we, re, xt2, yt0, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o300, o301, o302, o303, o304, o305, o306, o307 = self.reg30.r(we, re, xt3, yt0, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o400, o401, o402, o403, o404, o405, o406, o407 = self.reg40.r(we, re, xt4, yt0, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o500, o501, o502, o503, o504, o505, o506, o507 = self.reg50.r(we, re, xt5, yt0, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o600, o601, o602, o603, o604, o605, o606, o607 = self.reg60.r(we, re, xt6, yt0, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o700, o701, o702, o703, o704, o705, o706, o707 = self.reg70.r(we, re, xt7, yt0, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o010, o011, o012, o013, o014, o015, o016, o017 = self.reg01.r(we, re, xt0, yt1, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o110, o111, o112, o113, o114, o115, o116, o117 = self.reg11.r(we, re, xt1, yt1, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o210, o211, o212, o213, o214, o215, o216, o217 = self.reg21.r(we, re, xt2, yt1, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o310, o311, o312, o313, o314, o315, o316, o317 = self.reg31.r(we, re, xt3, yt1, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o410, o411, o412, o413, o414, o415, o416, o417 = self.reg41.r(we, re, xt4, yt1, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o510, o511, o512, o513, o514, o515, o516, o517 = self.reg51.r(we, re, xt5, yt1, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o610, o611, o612, o613, o614, o615, o616, o617 = self.reg61.r(we, re, xt6, yt1, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o710, o711, o712, o713, o714, o715, o716, o717 = self.reg71.r(we, re, xt7, yt1, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o020, o021, o022, o023, o024, o025, o026, o027 = self.reg02.r(we, re, xt0, yt2, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o120, o121, o122, o123, o124, o125, o126, o127 = self.reg12.r(we, re, xt1, yt2, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o220, o221, o222, o223, o224, o225, o226, o227 = self.reg22.r(we, re, xt2, yt2, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o320, o321, o322, o323, o324, o325, o326, o327 = self.reg32.r(we, re, xt3, yt2, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o420, o421, o422, o423, o424, o425, o426, o427 = self.reg42.r(we, re, xt4, yt2, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o520, o521, o522, o523, o524, o525, o526, o527 = self.reg52.r(we, re, xt5, yt2, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o620, o621, o622, o623, o624, o625, o626, o627 = self.reg62.r(we, re, xt6, yt2, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o720, o721, o722, o723, o724, o725, o726, o727 = self.reg72.r(we, re, xt7, yt2, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o030, o031, o032, o033, o034, o035, o036, o037 = self.reg03.r(we, re, xt0, yt3, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o130, o131, o132, o133, o134, o135, o136, o137 = self.reg13.r(we, re, xt1, yt3, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o230, o231, o232, o233, o234, o235, o236, o237 = self.reg23.r(we, re, xt2, yt3, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o330, o331, o332, o333, o334, o335, o336, o337 = self.reg33.r(we, re, xt3, yt3, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o430, o431, o432, o433, o434, o435, o436, o437 = self.reg43.r(we, re, xt4, yt3, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o530, o531, o532, o533, o534, o535, o536, o537 = self.reg53.r(we, re, xt5, yt3, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o630, o631, o632, o633, o634, o635, o636, o637 = self.reg63.r(we, re, xt6, yt3, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o730, o731, o732, o733, o734, o735, o736, o737 = self.reg73.r(we, re, xt7, yt3, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o040, o041, o042, o043, o044, o045, o046, o047 = self.reg04.r(we, re, xt0, yt4, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o140, o141, o142, o143, o144, o145, o146, o147 = self.reg14.r(we, re, xt1, yt4, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o240, o241, o242, o243, o244, o245, o246, o247 = self.reg24.r(we, re, xt2, yt4, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o340, o341, o342, o343, o344, o345, o346, o347 = self.reg34.r(we, re, xt3, yt4, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o440, o441, o442, o443, o444, o445, o446, o447 = self.reg44.r(we, re, xt4, yt4, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o540, o541, o542, o543, o544, o545, o546, o547 = self.reg54.r(we, re, xt5, yt4, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o640, o641, o642, o643, o644, o645, o646, o647 = self.reg64.r(we, re, xt6, yt4, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o740, o741, o742, o743, o744, o745, o746, o747 = self.reg74.r(we, re, xt7, yt4, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o050, o051, o052, o053, o054, o055, o056, o057 = self.reg05.r(we, re, xt0, yt5, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o150, o151, o152, o153, o154, o155, o156, o157 = self.reg15.r(we, re, xt1, yt5, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o250, o251, o252, o253, o254, o255, o256, o257 = self.reg25.r(we, re, xt2, yt5, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o350, o351, o352, o353, o354, o355, o356, o357 = self.reg35.r(we, re, xt3, yt5, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o450, o451, o452, o453, o454, o455, o456, o457 = self.reg45.r(we, re, xt4, yt5, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o550, o551, o552, o553, o554, o555, o556, o557 = self.reg55.r(we, re, xt5, yt5, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o650, o651, o652, o653, o654, o655, o656, o657 = self.reg65.r(we, re, xt6, yt5, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o750, o751, o752, o753, o754, o755, o756, o757 = self.reg75.r(we, re, xt7, yt5, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o060, o061, o062, o063, o064, o065, o066, o067 = self.reg06.r(we, re, xt0, yt6, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o160, o161, o162, o163, o164, o165, o166, o167 = self.reg16.r(we, re, xt1, yt6, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o260, o261, o262, o263, o264, o265, o266, o267 = self.reg26.r(we, re, xt2, yt6, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o360, o361, o362, o363, o364, o365, o366, o367 = self.reg36.r(we, re, xt3, yt6, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o460, o461, o462, o463, o464, o465, o466, o467 = self.reg46.r(we, re, xt4, yt6, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o560, o561, o562, o563, o564, o565, o566, o567 = self.reg56.r(we, re, xt5, yt6, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o660, o661, o662, o663, o664, o665, o666, o667 = self.reg66.r(we, re, xt6, yt6, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o760, o761, o762, o763, o764, o765, o766, o767 = self.reg76.r(we, re, xt7, yt6, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o070, o071, o072, o073, o074, o075, o076, o077 = self.reg07.r(we, re, xt0, yt7, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o170, o171, o172, o173, o174, o175, o176, o177 = self.reg17.r(we, re, xt1, yt7, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o270, o271, o272, o273, o274, o275, o276, o277 = self.reg27.r(we, re, xt2, yt7, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o370, o371, o372, o373, o374, o375, o376, o377 = self.reg37.r(we, re, xt3, yt7, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o470, o471, o472, o473, o474, o475, o476, o477 = self.reg47.r(we, re, xt4, yt7, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o570, o571, o572, o573, o574, o575, o576, o577 = self.reg57.r(we, re, xt5, yt7, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o670, o671, o672, o673, o674, o675, o676, o677 = self.reg67.r(we, re, xt6, yt7, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o770, o771, o772, o773, o774, o775, o776, o777 = self.reg77.r(we, re, xt7, yt7, d0,d1,d2,d3,d4,d5,d6,d7, c)
        o00, o01, o02, o03, o04, o05, o06, o07 = self.mux0.r(x2,x1,x0,
                                                    o000, o001, o002, o003, o004, o005, o006, o007,
                                                    o100, o101, o102, o103, o104, o105, o106, o107,
                                                    o200, o201, o202, o203, o204, o205, o206, o207,
                                                    o300, o301, o302, o303, o304, o305, o306, o307,
                                                    o400, o401, o402, o403, o404, o405, o406, o407,
                                                    o500, o501, o502, o503, o504, o505, o506, o507,
                                                    o600, o601, o602, o603, o604, o605, o606, o607,
                                                    o700, o701, o702, o703, o704, o705, o706, o707)
        o10, o11, o12, o13, o14, o15, o16, o17 = self.mux1.r(x2,x1,x0,
                                                    o010, o011, o012, o013, o014, o015, o016, o017,
                                                    o110, o111, o112, o113, o114, o115, o116, o117,
                                                    o210, o211, o212, o213, o214, o215, o216, o217,
                                                    o310, o311, o312, o313, o314, o315, o316, o317,
                                                    o410, o411, o412, o413, o414, o415, o416, o417,
                                                    o510, o511, o512, o513, o514, o515, o516, o517,
                                                    o610, o611, o612, o613, o614, o615, o616, o617,
                                                    o710, o711, o712, o713, o714, o715, o716, o717)
        o20, o21, o22, o23, o24, o25, o26, o27 = self.mux2.r(x2,x1,x0,
                                                    o020, o021, o022, o023, o024, o025, o026, o027,
                                                    o120, o121, o122, o123, o124, o125, o126, o127,
                                                    o220, o221, o222, o223, o224, o225, o226, o227,
                                                    o320, o321, o322, o323, o324, o325, o326, o327,
                                                    o420, o421, o422, o423, o424, o425, o426, o427,
                                                    o520, o521, o522, o523, o524, o525, o526, o527,
                                                    o620, o621, o622, o623, o624, o625, o626, o627,
                                                    o720, o721, o722, o723, o724, o725, o726, o727)
        o30, o31, o32, o33, o34, o35, o36, o37 = self.mux3.r(x2,x1,x0,
                                                    o030, o031, o032, o033, o034, o035, o036, o037,
                                                    o130, o131, o132, o133, o134, o135, o136, o137,
                                                    o230, o231, o232, o233, o234, o235, o236, o237,
                                                    o330, o331, o332, o333, o334, o335, o336, o337,
                                                    o430, o431, o432, o433, o434, o435, o436, o437,
                                                    o530, o531, o532, o533, o534, o535, o536, o537,
                                                    o630, o631, o632, o633, o634, o635, o636, o637,
                                                    o730, o731, o732, o733, o734, o735, o736, o737)
        o40, o41, o42, o43, o44, o45, o46, o47 = self.mux4.r(x2,x1,x0,
                                                    o040, o041, o042, o043, o044, o045, o046, o047,
                                                    o140, o141, o142, o143, o144, o145, o146, o147,
                                                    o240, o241, o242, o243, o244, o245, o246, o247,
                                                    o340, o341, o342, o343, o344, o345, o346, o347,
                                                    o440, o441, o442, o443, o444, o445, o446, o447,
                                                    o540, o541, o542, o543, o544, o545, o546, o547,
                                                    o640, o641, o642, o643, o644, o645, o646, o647,
                                                    o740, o741, o742, o743, o744, o745, o746, o747)
        o50, o51, o52, o53, o54, o55, o56, o57 = self.mux5.r(x2,x1,x0,
                                                    o050, o051, o052, o053, o054, o055, o056, o057,
                                                    o150, o151, o152, o153, o154, o155, o156, o157,
                                                    o250, o251, o252, o253, o254, o255, o256, o257,
                                                    o350, o351, o352, o353, o354, o355, o356, o357,
                                                    o450, o451, o452, o453, o454, o455, o456, o457,
                                                    o550, o551, o552, o553, o554, o555, o556, o557,
                                                    o650, o651, o652, o653, o654, o655, o656, o657,
                                                    o750, o751, o752, o753, o754, o755, o756, o757)
        o60, o61, o62, o63, o64, o65, o66, o67 = self.mux6.r(x2,x1,x0,
                                                    o060, o061, o062, o063, o064, o065, o066, o067,
                                                    o160, o161, o162, o163, o164, o165, o166, o167,
                                                    o260, o261, o262, o263, o264, o265, o266, o267,
                                                    o360, o361, o362, o363, o364, o365, o366, o367,
                                                    o460, o461, o462, o463, o464, o465, o466, o467,
                                                    o560, o561, o562, o563, o564, o565, o566, o567,
                                                    o660, o661, o662, o663, o664, o665, o666, o667,
                                                    o760, o761, o762, o763, o764, o765, o766, o767)
        o70, o71, o72, o73, o74, o75, o76, o77 = self.mux7.r(x2,x1,x0,
                                                    o070, o071, o072, o073, o074, o075, o076, o077,
                                                    o170, o171, o172, o173, o174, o175, o176, o177,
                                                    o270, o271, o272, o273, o274, o275, o276, o277,
                                                    o370, o371, o372, o373, o374, o375, o376, o377,
                                                    o470, o471, o472, o473, o474, o475, o476, o477,
                                                    o570, o571, o572, o573, o574, o575, o576, o577,
                                                    o670, o671, o672, o673, o674, o675, o676, o677,
                                                    o770, o771, o772, o773, o774, o775, o776, o777)
        o0, o1, o2, o3, o4, o5, o6, o7 = self.mux8.r(y2,y1,y0,
                                                    o00, o01, o02, o03, o04, o05, o06, o07,
                                                    o10, o11, o12, o13, o14, o15, o16, o17,
                                                    o20, o21, o22, o23, o24, o25, o26, o27,
                                                    o30, o31, o32, o33, o34, o35, o36, o37,
                                                    o40, o41, o42, o43, o44, o45, o46, o47,
                                                    o50, o51, o52, o53, o54, o55, o56, o57,
                                                    o60, o61, o62, o63, o64, o65, o66, o67,
                                                    o70, o71, o72, o73, o74, o75, o76, o77)
        return o0,o1,o2,o3,o4,o5,o6,o7 
### RAM ###

### INSTRUCTION DECODR ###
class idec:
    def __init__(self):
        self.idec0 = bdecoder()
        self.idec1 = bdecoder()
        self.iband0 = band()
        self.iband1 = band()
        self.inv = inv()
        self.bb00 = band()
        self.bb01 = band()
        self.bb02 = band()
        self.bb10 = band()
        self.bb11 = band()
        self.bb12 = band()
        self.bb20 = band()
        self.bb21 = band()
        self.bb22 = band()
        self.bb30 = band()
        self.bb31 = band()
        self.bb32 = band()
        self.bb40 = band()
        self.bb41 = band()
        self.bb42 = band()
        self.bb50 = band()
        self.bb51 = band()
        self.bb52 = band()
        self.bb60 = band()
        self.bb61 = band()
        self.bb62 = band()
        self.bb70 = band()
        self.bb71 = band()
        self.bb72 = band()
        self.bb80 = band()
        self.bb81 = band()
        self.bb82 = band()
        self.bb90 = band()
        self.bb91 = band()
        self.bb92 = band()
        self.bba0 = band()
        self.bba1 = band()
        self.bba2 = band()
        self.bbb0 = band()
        self.bbb1 = band()
        self.bbb2 = band()
        self.bbc0 = band()
        self.bbc1 = band()
        self.bbc2 = band()
        self.bbd0 = band()
        self.bbd1 = band()
        self.bbd2 = band()
        self.bbe0 = band()
        self.bbe1 = band()
        self.bbe2 = band()
        self.bbf0 = band()
        self.bbf1 = band()
        self.bbf2 = band()
        self.oo00 = gOr8()
        self.oo01 = gOr8()
        self.oo10 = gOr8()
        self.oo11 = gOr8()
        self.oo20 = gOr8()
        self.oo21 = gOr8()
        self.oo30 = gOr8()
        self.oo31 = gOr8()
        self.oo40 = gOr8()
        self.oo41 = gOr8()
        self.oo50 = gOr8()
        self.oo51 = gOr8()
        self.oo60 = gOr8()
        self.oo61 = gOr8()
        self.oo70 = gOr8()
        self.oo71 = gOr8()
        self.oo80 = gOr8()
        self.oo81 = gOr8()
        self.oo90 = gOr8()
        self.oo91 = gOr8()
        self.ooa0 = gOr8()
        self.ooa1 = gOr8()
        self.oob0 = gOr8()
        self.oob1 = gOr8()
        self.ooc0 = gOr8()
        self.ooc1 = gOr8()
        self.ood0 = gOr8()
        self.ood1 = gOr8()
        self.ooe0 = gOr8()
        self.ooe1 = gOr8()
        self.oof0 = gOr8()
        self.oof1 = gOr8()
        self.oog0 = gOr8()
        self.oog1 = gOr8()
        self.ooh0 = gOr8()
        self.ooh1 = gOr8()
        self.ooi0 = gOr8()
        self.ooi1 = gOr8()
        self.ooj0 = gOr8()
        self.ooj1 = gOr8()
        self.bor0 = bor()
        self.bor1 = bor()
        self.bor2 = bor()
    
    def r(self, x3, x2, x1, x0,
        i00, i01, i02, i03, a00, a01, a02, a03, a04, a05, a06, a07, b00, b01, b02, b03, b04, b05, b06, b07,
        i10, i11, i12, i13, a10, a11, a12, a13, a14, a15, a16, a17, b10, b11, b12, b13, b14, b15, b16, b17,
        i20, i21, i22, i23, a20, a21, a22, a23, a24, a25, a26, a27, b20, b21, b22, b23, b24, b25, b26, b27,
        i30, i31, i32, i33, a30, a31, a32, a33, a34, a35, a36, a37, b30, b31, b32, b33, b34, b35, b36, b37,
        i40, i41, i42, i43, a40, a41, a42, a43, a44, a45, a46, a47, b40, b41, b42, b43, b44, b45, b46, b47,
        i50, i51, i52, i53, a50, a51, a52, a53, a54, a55, a56, a57, b50, b51, b52, b53, b54, b55, b56, b57,
        i60, i61, i62, i63, a60, a61, a62, a63, a64, a65, a66, a67, b60, b61, b62, b63, b64, b65, b66, b67,
        i70, i71, i72, i73, a70, a71, a72, a73, a74, a75, a76, a77, b70, b71, b72, b73, b74, b75, b76, b77,
        i80, i81, i82, i83, a80, a81, a82, a83, a84, a85, a86, a87, b80, b81, b82, b83, b84, b85, b86, b87,
        i90, i91, i92, i93, a90, a91, a92, a93, a94, a95, a96, a97, b90, b91, b92, b93, b94, b95, b96, b97,
        ia0, ia1, ia2, ia3, aa0, aa1, aa2, aa3, aa4, aa5, aa6, aa7, ba0, ba1, ba2, ba3, ba4, ba5, ba6, ba7,
        ib0, ib1, ib2, ib3, ab0, ab1, ab2, ab3, ab4, ab5, ab6, ab7, bb0, bb1, bb2, bb3, bb4, bb5, bb6, bb7,
        ic0, ic1, ic2, ic3, ac0, ac1, ac2, ac3, ac4, ac5, ac6, ac7, bc0, bc1, bc2, bc3, bc4, bc5, bc6, bc7,
        id0, id1, id2, id3, ad0, ad1, ad2, ad3, ad4, ad5, ad6, ad7, bd0, bd1, bd2, bd3, bd4, bd5, bd6, bd7,
        ie0, ie1, ie2, ie3, ae0, ae1, ae2, ae3, ae4, ae5, ae6, ae7, be0, be1, be2, be3, be4, be5, be6, be7,
        if0, if1, if2, if3, af0, af1, af2, af3, af4, af5, af6, af7, bf0, bf1, bf2, bf3, bf4, bf5, bf6, bf7):
        ins1 = self.inv.r(x3)
        iin0, iin1, iin2, iin3, iin4, iin5, iin6, iin7 = self.idec0.r(x2,x1,x0)
        in0, in1, in2, in3, in4, in5, in6, in7 = self.iband0.r(iin0, iin1, iin2, iin3, iin4, iin5, iin6, iin7, ins1, ins1, ins1, ins1, ins1, ins1, ins1, ins1)
        in8, in9, ina, inb, inc, ind, ine, inf = self.iband1.r(iin0, iin1, iin2, iin3, iin4, iin5, iin6, iin7, x3, x3, x3, x3, x3, x3, x3, x3)
        i00, i01, i02, i03, _, _, _, _ = self.bb00.r(i00, i01, i02, i03, 0,0,0,0, in0,in0,in0,in0, 0,0,0,0)
        a00, a01, a02, a03, a04, a05, a06, a07 = self.bb01.r(a00, a01, a02, a03, a04, a05, a06, a07, in0,in0,in0,in0,in0,in0,in0,in0)
        b00, b01, b02, b03, b04, b05, b06, b07 = self. bb02.r(b00, b01, b02, b03, b04, b05, b06, b07, in0,in0,in0,in0,in0,in0,in0,in0)
        i10, i11, i12, i13, _, _, _, _ = self.bb10.r(i10, i11, i12, i13, 0,0,0,0, in1,in1,in1,in1, 0,0,0,0)
        a10, a11, a12, a13, a14, a15, a16, a17 = self.bb11.r(a10, a11, a12, a13, a14, a15, a16, a17, in1,in1,in1,in1,in1,in1,in1,in1)
        b10, b11, b12, b13, b14, b15, b16, b17 = self. bb12.r(b10, b11, b12, b13, b14, b15, b16, b17, in1,in1,in1,in1,in1,in1,in1,in1)
        i20, i21, i22, i23, _, _, _, _ = self.bb20.r(i20, i21, i22, i23, 0,0,0,0, in2,in2,in2,in2, 0,0,0,0)
        a20, a21, a22, a23, a24, a25, a26, a27 = self.bb21.r(a20, a21, a22, a23, a24, a25, a26, a27, in2,in2,in2,in2,in2,in2,in2,in2)
        b20, b21, b22, b23, b24, b25, b26, b27 = self. bb22.r(b20, b21, b22, b23, b24, b25, b26, b27, in2,in2,in2,in2,in2,in2,in2,in2)
        i30, i31, i32, i33, _, _, _, _ = self.bb30.r(i30, i31, i32, i33, 0,0,0,0, in3,in3,in3,in3, 0,0,0,0)
        a30, a31, a32, a33, a34, a35, a36, a37 = self.bb31.r(a30, a31, a32, a33, a34, a35, a36, a37, in3,in3,in3,in3,in3,in3,in3,in3)
        b30, b31, b32, b33, b34, b35, b36, b37 = self. bb32.r(b30, b31, b32, b33, b34, b35, b36, b37, in3,in3,in3,in3,in3,in3,in3,in3)
        i40, i41, i42, i43, _, _, _, _ = self.bb40.r(i40, i41, i42, i43, 0,0,0,0, in4,in4,in4,in4, 0,0,0,0)
        a40, a41, a42, a43, a44, a45, a46, a47 = self.bb41.r(a40, a41, a42, a43, a44, a45, a46, a47, in4,in4,in4,in4,in4,in4,in4,in4)
        b40, b41, b42, b43, b44, b45, b46, b47 = self. bb42.r(b40, b41, b42, b43, b44, b45, b46, b47, in4,in4,in4,in4,in4,in4,in4,in4)
        i50, i51, i52, i53, _, _, _, _ = self.bb50.r(i50, i51, i52, i53, 0,0,0,0, in5,in5,in5,in5, 0,0,0,0)
        a50, a51, a52, a53, a54, a55, a56, a57 = self.bb51.r(a50, a51, a52, a53, a54, a55, a56, a57, in5,in5,in5,in5,in5,in5,in5,in5)
        b50, b51, b52, b53, b54, b55, b56, b57 = self. bb52.r(b50, b51, b52, b53, b54, b55, b56, b57, in5,in5,in5,in5,in5,in5,in5,in5)
        i60, i61, i62, i63, _, _, _, _ = self.bb60.r(i60, i61, i62, i63, 0,0,0,0, in6,in6,in6,in6, 0,0,0,0)
        a60, a61, a62, a63, a64, a65, a66, a67 = self.bb61.r(a60, a61, a62, a63, a64, a65, a66, a67, in6,in6,in6,in6,in6,in6,in6,in6)
        b60, b61, b62, b63, b64, b65, b66, b67 = self. bb62.r(b60, b61, b62, b63, b64, b65, b66, b67, in6,in6,in6,in6,in6,in6,in6,in6)
        i70, i71, i72, i73, _, _, _, _ = self.bb70.r(i70, i71, i72, i73, 0,0,0,0, in7,in7,in7,in7, 0,0,0,0)
        a70, a71, a72, a73, a74, a75, a76, a77 = self.bb71.r(a70, a71, a72, a73, a74, a75, a76, a77, in7,in7,in7,in7,in7,in7,in7,in7)
        b70, b71, b72, b73, b74, b75, b76, b77 = self. bb72.r(b70, b71, b72, b73, b74, b75, b76, b77, in7,in7,in7,in7,in7,in7,in7,in7)
        i80, i81, i82, i83, _, _, _, _ = self.bb80.r(i80, i81, i82, i83, 0,0,0,0, in8,in8,in8,in8, 0,0,0,0)
        a80, a81, a82, a83, a84, a85, a86, a87 = self.bb81.r(a80, a81, a82, a83, a84, a85, a86, a87, in8,in8,in8,in8,in8,in8,in8,in8)
        b80, b81, b82, b83, b84, b85, b86, b87 = self. bb82.r(b80, b81, b82, b83, b84, b85, b86, b87, in8,in8,in8,in8,in8,in8,in8,in8)
        i90, i91, i92, i93, _, _, _, _ = self.bb90.r(i90, i91, i92, i93, 0,0,0,0, in9,in9,in9,in9, 0,0,0,0)
        a90, a91, a92, a93, a94, a95, a96, a97 = self.bb91.r(a90, a91, a92, a93, a94, a95, a96, a97, in9,in9,in9,in9,in9,in9,in9,in9)
        b90, b91, b92, b93, b94, b95, b96, b97 = self. bb92.r(b90, b91, b92, b93, b94, b95, b96, b97, in9,in9,in9,in9,in9,in9,in9,in9)
        ia0, ia1, ia2, ia3, _, _, _, _ = self.bba0.r(ia0, ia1, ia2, ia3, 0,0,0,0, ina,ina,ina,ina, 0,0,0,0)
        aa0, aa1, aa2, aa3, aa4, aa5, aa6, aa7 = self.bba1.r(aa0, aa1, aa2, aa3, aa4, aa5, aa6, aa7, ina,ina,ina,ina,ina,ina,ina,ina)
        ba0, ba1, ba2, ba3, ba4, ba5, ba6, ba7 = self. bba2.r(ba0, ba1, ba2, ba3, ba4, ba5, ba6, ba7, ina,ina,ina,ina,ina,ina,ina,ina)
        ib0, ib1, ib2, ib3, _, _, _, _ = self.bbb0.r(ib0, ib1, ib2, ib3, 0,0,0,0, inb,inb,inb,inb, 0,0,0,0)
        ab0, ab1, ab2, ab3, ab4, ab5, ab6, ab7 = self.bbb1.r(ab0, ab1, ab2, ab3, ab4, ab5, ab6, ab7, inb,inb,inb,inb,inb,inb,inb,inb)
        bb0, bb1, bb2, bb3, bb4, bb5, bb6, bb7 = self. bbb2.r(bb0, bb1, bb2, bb3, bb4, bb5, bb6, bb7, inb,inb,inb,inb,inb,inb,inb,inb)
        ic0, ic1, ic2, ic3, _, _, _, _ = self.bbc0.r(ic0, ic1, ic2, ic3, 0,0,0,0, inc,inc,inc,inc, 0,0,0,0)
        ac0, ac1, ac2, ac3, ac4, ac5, ac6, ac7 = self.bbc1.r(ac0, ac1, ac2, ac3, ac4, ac5, ac6, ac7, inc,inc,inc,inc,inc,inc,inc,inc)
        bc0, bc1, bc2, bc3, bc4, bc5, bc6, bc7 = self. bbc2.r(bc0, bc1, bc2, bc3, bc4, bc5, bc6, bc7, inc,inc,inc,inc,inc,inc,inc,inc)
        id0, id1, id2, id3, _, _, _, _ = self.bbd0.r(id0, id1, id2, id3, 0,0,0,0, ind,ind,ind,ind, 0,0,0,0)
        ad0, ad1, ad2, ad3, ad4, ad5, ad6, ad7 = self.bbd1.r(ad0, ad1, ad2, ad3, ad4, ad5, ad6, ad7, ind,ind,ind,ind,ind,ind,ind,ind)
        bd0, bd1, bd2, bd3, bd4, bd5, bd6, bd7 = self. bbd2.r(bd0, bd1, bd2, bd3, bd4, bd5, bd6, bd7, ind,ind,ind,ind,ind,ind,ind,ind)
        ie0, ie1, ie2, ie3, _, _, _, _ = self.bbe0.r(ie0, ie1, ie2, ie3, 0,0,0,0, ine,ine,ine,ine, 0,0,0,0)
        ae0, ae1, ae2, ae3, ae4, ae5, ae6, ae7 = self.bbe1.r(ae0, ae1, ae2, ae3, ae4, ae5, ae6, ae7, ine,ine,ine,ine,ine,ine,ine,ine)
        be0, be1, be2, be3, be4, be5, be6, be7 = self. bbe2.r(be0, be1, be2, be3, be4, be5, be6, be7, ine,ine,ine,ine,ine,ine,ine,ine)
        if0, if1, if2, if3, _, _, _, _ = self.bbf0.r(if0, if1, if2, if3, 0,0,0,0, inf,inf,inf,inf, 0,0,0,0)
        af0, af1, af2, af3, af4, af5, af6, af7 = self.bbf1.r(af0, af1, af2, af3, af4, af5, af6, af7, inf,inf,inf,inf,inf,inf,inf,inf)
        bf0, bf1, bf2, bf3, bf4, bf5, bf6, bf7 = self. bbf2.r(bf0, bf1, bf2, bf3, bf4, bf5, bf6, bf7, inf,inf,inf,inf,inf,inf,inf,inf)
        ic00 = self.oo00.r(i00, i10, i20, i30, i40, i50, i60, i70)
        ic01 = self.oo01.r(i80, i90, ia0, ib0, ic0, id0, ie0, if0)
        ic10 = self.oo10.r(i01, i11, i21, i31, i41, i51, i61, i71)
        ic11 = self.oo11.r(i81, i91, ia1, ib1, ic1, id1, ie1, if1)
        ic20 = self.oo20.r(i02, i12, i22, i32, i42, i52, i62, i72)
        ic21 = self.oo21.r(i82, i92, ia2, ib2, ic2, id2, ie2, if2)
        ic30 = self.oo30.r(i03, i13, i23, i33, i43, i53, i63, i73)
        ic31 = self.oo31.r(i83, i93, ia3, ib3, ic3, id3, ie3, if3)
        ac00 = self.oo40.r(a00, a10, a20, a30, a40, a50, a60, a70)
        ac01 = self.oo41.r(a80, a90, aa0, ab0, ac0, ad0, ae0, af0)
        ac10 = self.oo50.r(a01, a11, a21, a31, a41, a51, a61, a71)
        ac11 = self.oo51.r(a81, a91, aa1, ab1, ac1, ad1, ae1, af1)
        ac20 = self.oo60.r(a02, a12, a22, a32, a42, a52, a62, a72)
        ac21 = self.oo61.r(a82, a92, aa2, ab2, ac2, ad2, ae2, af2)
        ac30 = self.oo70.r(a03, a13, a23, a33, a43, a53, a63, a73)
        ac31 = self.oo71.r(a83, a93, aa3, ab3, ac3, ad3, ae3, af3)
        ac40 = self.oo80.r(a04, a14, a24, a34, a44, a54, a64, a74)
        ac41 = self.oo81.r(a84, a94, aa4, ab4, ac4, ad4, ae4, af4)
        ac50 = self.oo90.r(a05, a15, a25, a35, a45, a55, a65, a75)
        ac51 = self.oo91.r(a85, a95, aa5, ab5, ac5, ad5, ae5, af5)
        ac60 = self.ooa0.r(a06, a16, a26, a36, a46, a56, a66, a76)
        ac61 = self.ooa1.r(a86, a96, aa6, ab6, ac6, ad6, ae6, af6)
        ac70 = self.oob0.r(a07, a17, a27, a37, a47, a57, a67, a77)
        ac71 = self.oob1.r(a87, a97, aa7, ab7, ac7, ad7, ae7, af7)
        bc00 = self.ooc0.r(b00, b10, b20, b30, b40, b50, b60, b70)
        bc01 = self.ooc1.r(b80, b90, ba0, bb0, bc0, bd0, be0, bf0)
        bc10 = self.ood0.r(b01, b11, b21, b31, b41, b51, b61, b71)
        bc11 = self.ood1.r(b81, b91, ba1, bb1, bc1, bd1, be1, bf1)
        bc20 = self.ooe0.r(b02, b12, b22, b32, b42, b52, b62, b72)
        bc21 = self.ooe1.r(b82, b92, ba2, bb2, bc2, bd2, be2, bf2)
        bc30 = self.oof0.r(b03, b13, b23, b33, b43, b53, b63, b73)
        bc31 = self.oof1.r(b83, b93, ba3, bb3, bc3, bd3, be3, bf3)
        bc40 = self.oog0.r(b04, b14, b24, b34, b44, b54, b64, b74)
        bc41 = self.oog1.r(b84, b94, ba4, bb4, bc4, bd4, be4, bf4)
        bc50 = self.ooh0.r(b05, b15, b25, b35, b45, b55, b65, b75)
        bc51 = self.ooh1.r(b85, b95, ba5, bb5, bc5, bd5, be5, bf5)
        bc60 = self.ooi0.r(b06, b16, b26, b36, b46, b56, b66, b76)
        bc61 = self.ooi1.r(b86, b96, ba6, bb6, bc6, bd6, be6, bf6)
        bc70 = self.ooj0.r(b07, b17, b27, b37, b47, b57, b67, b77)
        bc71 = self.ooj1.r(b87, b97, ba7, bb7, bc7, bd7, be7, bf7)
        ri0, ri1, ri2, ri3, _, _, _, _ = self.bor0.r(ic00, ic10, ic20, ic30, 0,0,0,0, ic01, ic11, ic21, ic31, 0,0,0,0)
        ra0, ra1, ra2, ra3, ra4, ra5, ra6, ra7 = self.bor1.r(ac00, ac10, ac20, ac30, ac40, ac50, ac60, ac70, ac01, ac11, ac21, ac31, ac41, ac51, ac61, ac71)
        rb0, rb1, rb2, rb3, rb4, rb5, rb6, rb7 = self.bor2.r(bc00, bc10, bc20, bc30, bc40, bc50, bc60, bc70, bc01, bc11, bc21, bc31, bc41, bc51, bc61, bc71)
        return ri0, ri1, ri2, ri3, ra0, ra1, ra2, ra3, ra4, ra5, ra6, ra7, rb0, rb1, rb2, rb3, rb4, rb5, rb6, rb7
### INSTRUCTION DECODR ###

### CPU ###
class cpu:
    def __init__(self):
        self.idec = idec()
        self.rega = reg8() #000
        self.regb = reg8() #001
        self.regc = reg8() #010
        self.regd = reg8() #011
        self.ireg = reg8() #100
        self.ireg.r(1,0, 0,0,0,0,0,0,0,0, 1)
        self.areg = reg8() #101
        self.ram0 = ram()
        self.alu0 = alu()
        self.ga0 = gAnd()
        self.inv0 = inv()
        self.ba0 = band()
        self.ba1 = band()
        self.bdec0 = bdecoder()
        self.bdec1 = bdecoder()
        self.bdec2 = bdecoder()
        self.gaa0 = gAnd()
        self.gaa1 = gAnd()
        self.gaa2 = gAnd()
        self.gaa3 = gAnd()
        self.gaa4 = gAnd()
        self.gaa5 = gAnd()
        self.gaa6 = gAnd()
        self.gaa7 = gAnd()
        self.gab0 = gAnd()
        self.gab1 = gAnd()
        self.gab2 = gAnd()
        self.gab3 = gAnd()
        self.gab4 = gAnd()
        self.gab5 = gAnd()
        self.gab6 = gAnd()
        self.gab7 = gAnd()
        self.gac0 = gAnd()
        self.gac1 = gAnd()
        self.gac2 = gAnd()
        self.gac3 = gAnd()
        self.gac4 = gAnd()
        self.gac5 = gAnd()
        self.gac6 = gAnd()
        self.gac7 = gAnd()
        self.gad0 = gAnd()
        self.gad1 = gAnd()
        self.gad2 = gAnd()
        self.gad3 = gAnd()
        self.gad4 = gAnd()
        self.gad5 = gAnd()
        self.gad6 = gAnd()
        self.gad7 = gAnd()
        self.iga0 = gAnd()
        self.iga1 = gAnd()
        self.iga2 = gAnd()
        self.iga3 = gAnd()
        self.iga4 = gAnd()
        self.iga5 = gAnd()
        self.iga6 = gAnd()
        self.iga7 = gAnd()
        self.aga0 = gAnd()
        self.aga1 = gAnd()
        self.aga2 = gAnd()
        self.aga3 = gAnd()
        self.aga4 = gAnd()
        self.aga5 = gAnd()
        self.aga6 = gAnd()
        self.aga7 = gAnd()
        self.bor00 = bor()
        self.bor01 = bor()
        self.bor02 = bor()
        self.bor03 = bor()
        self.bor04 = bor()
        self.bor10 = bor()
        self.bor11 = bor()
        self.bor12 = bor()
        self.bor13 = bor()
        self.bor14 = bor()
        self.bor20 = bor()
        self.bor21 = bor()
        self.bor22 = bor()
        self.bor23 = bor()
        self.bor24 = bor()
        self.incr = binc()

    def r(self, cl,
        i00, i01, i02, i03, a00, a01, a02, a03, a04, a05, a06, a07, b00, b01, b02, b03, b04, b05, b06, b07,
        i10, i11, i12, i13, a10, a11, a12, a13, a14, a15, a16, a17, b10, b11, b12, b13, b14, b15, b16, b17,
        i20, i21, i22, i23, a20, a21, a22, a23, a24, a25, a26, a27, b20, b21, b22, b23, b24, b25, b26, b27,
        i30, i31, i32, i33, a30, a31, a32, a33, a34, a35, a36, a37, b30, b31, b32, b33, b34, b35, b36, b37,
        i40, i41, i42, i43, a40, a41, a42, a43, a44, a45, a46, a47, b40, b41, b42, b43, b44, b45, b46, b47,
        i50, i51, i52, i53, a50, a51, a52, a53, a54, a55, a56, a57, b50, b51, b52, b53, b54, b55, b56, b57,
        i60, i61, i62, i63, a60, a61, a62, a63, a64, a65, a66, a67, b60, b61, b62, b63, b64, b65, b66, b67,
        i70, i71, i72, i73, a70, a71, a72, a73, a74, a75, a76, a77, b70, b71, b72, b73, b74, b75, b76, b77,
        i80, i81, i82, i83, a80, a81, a82, a83, a84, a85, a86, a87, b80, b81, b82, b83, b84, b85, b86, b87,
        i90, i91, i92, i93, a90, a91, a92, a93, a94, a95, a96, a97, b90, b91, b92, b93, b94, b95, b96, b97,
        ia0, ia1, ia2, ia3, aa0, aa1, aa2, aa3, aa4, aa5, aa6, aa7, ba0, ba1, ba2, ba3, ba4, ba5, ba6, ba7,
        ib0, ib1, ib2, ib3, ab0, ab1, ab2, ab3, ab4, ab5, ab6, ab7, bb0, bb1, bb2, bb3, bb4, bb5, bb6, bb7,
        ic0, ic1, ic2, ic3, ac0, ac1, ac2, ac3, ac4, ac5, ac6, ac7, bc0, bc1, bc2, bc3, bc4, bc5, bc6, bc7,
        id0, id1, id2, id3, ad0, ad1, ad2, ad3, ad4, ad5, ad6, ad7, bd0, bd1, bd2, bd3, bd4, bd5, bd6, bd7,
        ie0, ie1, ie2, ie3, ae0, ae1, ae2, ae3, ae4, ae5, ae6, ae7, be0, be1, be2, be3, be4, be5, be6, be7,
        if0, if1, if2, if3, af0, af1, af2, af3, af4, af5, af6, af7, bf0, bf1, bf2, bf3, bf4, bf5, bf6, bf7):

        for _ in range(cl):
            c = 1

            finc0, finc1, finc2, finc3, inc0, inc1, inc2, inc3 = self.ireg.r(0, 1, 0,0,0,0,0,0,0,0, c)

            i00, i01, i02, i03, a00, a01, a02, a03, a04, a05, a06, a07, b00, b01, b02, b03, b04, b05, b06, b07 = self.idec.r(inc0, inc1, inc2, inc3,
                                                i00, i01, i02, i03, a00, a01, a02, a03, a04, a05, a06, a07, b00, b01, b02, b03, b04, b05, b06, b07,
                                                i10, i11, i12, i13, a10, a11, a12, a13, a14, a15, a16, a17, b10, b11, b12, b13, b14, b15, b16, b17,
                                                i20, i21, i22, i23, a20, a21, a22, a23, a24, a25, a26, a27, b20, b21, b22, b23, b24, b25, b26, b27,
                                                i30, i31, i32, i33, a30, a31, a32, a33, a34, a35, a36, a37, b30, b31, b32, b33, b34, b35, b36, b37,
                                                i40, i41, i42, i43, a40, a41, a42, a43, a44, a45, a46, a47, b40, b41, b42, b43, b44, b45, b46, b47,
                                                i50, i51, i52, i53, a50, a51, a52, a53, a54, a55, a56, a57, b50, b51, b52, b53, b54, b55, b56, b57,
                                                i60, i61, i62, i63, a60, a61, a62, a63, a64, a65, a66, a67, b60, b61, b62, b63, b64, b65, b66, b67,
                                                i70, i71, i72, i73, a70, a71, a72, a73, a74, a75, a76, a77, b70, b71, b72, b73, b74, b75, b76, b77,
                                                i80, i81, i82, i83, a80, a81, a82, a83, a84, a85, a86, a87, b80, b81, b82, b83, b84, b85, b86, b87,
                                                i90, i91, i92, i93, a90, a91, a92, a93, a94, a95, a96, a97, b90, b91, b92, b93, b94, b95, b96, b97,
                                                ia0, ia1, ia2, ia3, aa0, aa1, aa2, aa3, aa4, aa5, aa6, aa7, ba0, ba1, ba2, ba3, ba4, ba5, ba6, ba7,
                                                ib0, ib1, ib2, ib3, ab0, ab1, ab2, ab3, ab4, ab5, ab6, ab7, bb0, bb1, bb2, bb3, bb4, bb5, bb6, bb7,
                                                ic0, ic1, ic2, ic3, ac0, ac1, ac2, ac3, ac4, ac5, ac6, ac7, bc0, bc1, bc2, bc3, bc4, bc5, bc6, bc7,
                                                id0, id1, id2, id3, ad0, ad1, ad2, ad3, ad4, ad5, ad6, ad7, bd0, bd1, bd2, bd3, bd4, bd5, bd6, bd7,
                                                ie0, ie1, ie2, ie3, ae0, ae1, ae2, ae3, ae4, ae5, ae6, ae7, be0, be1, be2, be3, be4, be5, be6, be7,
                                                if0, if1, if2, if3, af0, af1, af2, af3, af4, af5, af6, af7, bf0, bf1, bf2, bf3, bf4, bf5, bf6, bf7)

            a = self.inv0.r(i00)
            m = i00
            rta0, rtb0, rtc0, rtd0, irt0, art0, rt60, rt70 = self.bdec0.r(a05,a06,a07)
            rta1, rtb1, rtc1, rtd1, irt1, art1, rt61, rt71 = self.bdec1.r(b05,b06,b07)

            fda0, fda1, fda2, fda3, fda4, fda5, fda6, fda7 = self.rega.r(0, rta0, 0,0,0,0,0,0,0,0, c)
            fdb0, fdb1, fdb2, fdb3, fdb4, fdb5, fdb6, fdb7 = self.regb.r(0, rtb0, 0,0,0,0,0,0,0,0, c)
            fdc0, fdc1, fdc2, fdc3, fdc4, fdc5, fdc6, fdc7 = self.regc.r(0, rtc0, 0,0,0,0,0,0,0,0, c)
            fdd0, fdd1, fdd2, fdd3, fdd4, fdd5, fdd6, fdd7 = self.regd.r(0, rtd0, 0,0,0,0,0,0,0,0, c)
            fid0, fid1, fid2, fid3, fid4, fid5, fid6, fid7 = self.ireg.r(0, irt0, 0,0,0,0,0,0,0,0, c)
            fad0, fad1, fad2, fad3, fad4, fad5, fad6, fad7 = self.areg.r(0, art0, 0,0,0,0,0,0,0,0, c)
            fr0, fr1, fr2, fr3, fr4, fr5, fr6, fr7 = self.bor00.r(fda0, fda1, fda2, fda3, fda4, fda5, fda6, fda7, fdb0, fdb1, fdb2, fdb3, fdb4, fdb5, fdb6, fdb7)
            fr0, fr1, fr2, fr3, fr4, fr5, fr6, fr7 = self.bor01.r(fr0, fr1, fr2, fr3, fr4, fr5, fr6, fr7, fdc0, fdc1, fdc2, fdc3, fdc4, fdc5, fdc6, fdc7)
            fr0, fr1, fr2, fr3, fr4, fr5, fr6, fr7 = self.bor02.r(fr0, fr1, fr2, fr3, fr4, fr5, fr6, fr7, fdd0, fdd1, fdd2, fdd3, fdd4, fdd5, fdd6, fdd7)
            fr0, fr1, fr2, fr3, fr4, fr5, fr6, fr7 = self.bor03.r(fr0, fr1, fr2, fr3, fr4, fr5, fr6, fr7, fid0, fid1, fid2, fid3, fid4, fid5, fid6, fid7)
            fr0, fr1, fr2, fr3, fr4, fr5, fr6, fr7 = self.bor04.r(fr0, fr1, fr2, fr3, fr4, fr5, fr6, fr7, fad0, fad1, fad2, fad3, fad4, fad5, fad6, fad7)
            ffda0, ffda1, ffda2, ffda3, ffda4, ffda5, ffda6, ffda7 = self.rega.r(0, rta1, 0,0,0,0,0,0,0,0, c)
            ffdb0, ffdb1, ffdb2, ffdb3, ffdb4, ffdb5, ffdb6, ffdb7 = self.regb.r(0, rtb1, 0,0,0,0,0,0,0,0, c)
            ffdc0, ffdc1, ffdc2, ffdc3, ffdc4, ffdc5, ffdc6, ffdc7 = self.regc.r(0, rtc1, 0,0,0,0,0,0,0,0, c)
            ffdd0, ffdd1, ffdd2, ffdd3, ffdd4, ffdd5, ffdd6, ffdd7 = self.regd.r(0, rtd1, 0,0,0,0,0,0,0,0, c)
            ffid0, ffid1, ffid2, ffid3, ffid4, ffid5, ffid6, ffid7 = self.ireg.r(0, irt1, 0,0,0,0,0,0,0,0, c)
            ffad0, ffad1, ffad2, ffad3, ffad4, ffad5, ffad6, ffad7 = self.areg.r(0, art1, 0,0,0,0,0,0,0,0, c)
            ffr0, ffr1, ffr2, ffr3, ffr4, ffr5, ffr6, ffr7 = self.bor10.r(ffda0, ffda1, ffda2, ffda3, ffda4, ffda5, ffda6, ffda7, ffdb0, ffdb1, ffdb2, ffdb3, ffdb4, ffdb5, ffdb6, ffdb7)
            ffr0, ffr1, ffr2, ffr3, ffr4, ffr5, ffr6, ffr7 = self.bor11.r(ffr0, ffr1, ffr2, ffr3, ffr4, ffr5, ffr6, ffr7, ffdc0, ffdc1, ffdc2, ffdc3, ffdc4, ffdc5, ffdc6, ffdc7)
            ffr0, ffr1, ffr2, ffr3, ffr4, ffr5, ffr6, ffr7 = self.bor12.r(ffr0, ffr1, ffr2, ffr3, ffr4, ffr5, ffr6, ffr7, ffdd0, ffdd1, ffdd2, ffdd3, ffdd4, ffdd5, ffdd6, ffdd7)
            ffr0, ffr1, ffr2, ffr3, ffr4, ffr5, ffr6, ffr7 = self.bor13.r(ffr0, ffr1, ffr2, ffr3, ffr4, ffr5, ffr6, ffr7, ffid0, ffid1, ffid2, ffid3, ffid4, ffid5, ffid6, ffid7)
            ffr0, ffr1, ffr2, ffr3, ffr4, ffr5, ffr6, ffr7 = self.bor14.r(ffr0, ffr1, ffr2, ffr3, ffr4, ffr5, ffr6, ffr7, ffad0, ffad1, ffad2, ffad3, ffad4, ffad5, ffad6, ffad7)

            _, _, _, _, _, ai1, ai2, ai3 = self.ba0.r(0,0,0,0,0,i01,i02,i03, 0,0,0,0,0,a,a,a)
            ar0, ar1, ar2, ar3, ar4, ar5, ar6, ar7 = self.alu0.r(ai1,ai2,ai3, fr0,fr1,fr2,fr3,fr4,fr5,fr6,fr7, ffr0,ffr1,ffr2,ffr3,ffr4,ffr5,ffr6,ffr7)
            self.rega.r(a, m, ar0, ar1, ar2, ar3, ar4, ar5, ar6, ar7, c)
            _, _, _, _, _, mi1, mi2, mi3 = self.ba1.r(0,0,0,0,0,i01,i02,i03, 0,0,0,0,0,m,m,m)
            t0, t1, t2, t3, t4, t5, t6, t7 = self.bdec2.r(mi1,mi2,mi3)

            t1a = self.gaa1.r(t1, rta0)
            t2a = self.gaa2.r(t2, rta0)
            t3a = self.gaa3.r(t3, rta0)
            t4a = self.gaa4.r(t4, rta0)
            t5a = self.gaa5.r(t5, rta0)
            t6a = self.gaa6.r(t6, rta0)
            t7a = self.gaa7.r(t7, rta0)
            t1b = self.gab1.r(t1, rtb0)
            t2b = self.gab2.r(t2, rtb0)
            t3b = self.gab3.r(t3, rtb0)
            t4b = self.gab4.r(t4, rtb0)
            t5b = self.gab5.r(t5, rtb0)
            t6b = self.gab6.r(t6, rtb0)
            t7b = self.gab7.r(t7, rtb0)
            t1c = self.gac1.r(t1, rtc0)
            t2c = self.gac2.r(t2, rtc0)
            t3c = self.gac3.r(t3, rtc0)
            t4c = self.gac4.r(t4, rtc0)
            t5c = self.gac5.r(t5, rtc0)
            t6c = self.gac6.r(t6, rtc0)
            t7c = self.gac7.r(t7, rtc0)
            t1d = self.gad1.r(t1, rtd0)
            t2d = self.gad2.r(t2, rtd0)
            t3d = self.gad3.r(t3, rtd0)
            t4d = self.gad4.r(t4, rtd0)
            t5d = self.gad5.r(t5, rtd0)
            t6d = self.gad6.r(t6, rtd0)
            t7d = self.gad7.r(t7, rtd0)
            ti1 = self.iga1.r(t1, irt0)
            ti2 = self.iga2.r(t2, irt0)
            ti3 = self.iga3.r(t3, irt0)
            ti4 = self.iga4.r(t4, irt0)
            ti5 = self.iga5.r(t5, irt0)
            ti6 = self.iga6.r(t6, irt0)
            ti7 = self.iga7.r(t7, irt0)
            ta1 = self.aga1.r(t1, art0)
            ta2 = self.aga2.r(t2, art0)
            ta3 = self.aga3.r(t3, art0)
            ta4 = self.aga4.r(t4, art0)
            ta5 = self.aga5.r(t5, art0)
            ta6 = self.aga6.r(t6, art0)
            ta7 = self.aga7.r(t7, art0)

            #1000
            self.ram0.r(t0, 0, b00,b01,b02,b03,b04,b05,b06,b07, a00,a01,a02,a03,a04,a05,a06,a07, c)

            #1001
            da0, da1, da2, da3, da4, da5, da6, da7 = self.rega.r(0, t1a, 0,0,0,0,0,0,0,0, c)
            db0, db1, db2, db3, db4, db5, db6, db7 = self.regb.r(0, t1b, 0,0,0,0,0,0,0,0, c)
            dc0, dc1, dc2, dc3, dc4, dc5, dc6, dc7 = self.regc.r(0, t1c, 0,0,0,0,0,0,0,0, c)
            dd0, dd1, dd2, dd3, dd4, dd5, dd6, dd7 = self.regd.r(0, t1d, 0,0,0,0,0,0,0,0, c)
            rid0, rid1, rid2, rid3, rid4, rid5, rid6, rid7 = self.ireg.r(0, ti1, 0,0,0,0,0,0,0,0, c)
            rad0, rad1, rad2, rad3, rad4, rad5, rad6, rad7 = self.areg.r(0, ta1, 0,0,0,0,0,0,0,0, c)
            r0, r1, r2, r3, r4, r5, r6, r7 = self.bor20.r(da0, da1, da2, da3, da4, da5, da6, da7, db0, db1, db2, db3, db4, db5, db6, db7)
            r0, r1, r2, r3, r4, r5, r6, r7 = self.bor21.r(r0, r1, r2, r3, r4, r5, r6, r7, dc0, dc1, dc2, dc3, dc4, dc5, dc6, dc7)
            r0, r1, r2, r3, r4, r5, r6, r7 = self.bor22.r(r0, r1, r2, r3, r4, r5, r6, r7, dd0, dd1, dd2, dd3, dd4, dd5, dd6, dd7)
            r0, r1, r2, r3, r4, r5, r6, r7 = self.bor23.r(r0, r1, r2, r3, r4, r5, r6, r7, rid0, rid1, rid2, rid3, rid4, rid5, rid6, rid7)
            r0, r1, r2, r3, r4, r5, r6, r7 = self.bor24.r(r0, r1, r2, r3, r4, r5, r6, r7, rad0, rad1, rad2, rad3, rad4, rad5, rad6, rad7)
            self.ram0.r(t1, 0, b00,b01,b02,b03,b04,b05,b06,b07, r0,r1,r2,r3,r4,r5,r6,r7, c)

            #1010
            d0, d1, d2, d3, d4, d5, d6, d7 = self.ram0.r(0, t2, b00,b01,b02,b03,b04,b05,b06,b07, 0,0,0,0,0,0,0,0, c)
            self.rega.r(t2a, 0, d0,d1,d2,d3,d4,d5,d6,d7, c)
            self.regb.r(t2b, 0, d0,d1,d2,d3,d4,d5,d6,d7, c)
            self.regc.r(t2c, 0, d0,d1,d2,d3,d4,d5,d6,d7, c)
            self.regd.r(t2d, 0, d0,d1,d2,d3,d4,d5,d6,d7, c)
            self.ireg.r(ti2, 0, d0,d1,d2,d3,d4,d5,d6,d7, c)
            self.areg.r(ta2, 0, d0,d1,d2,d3,d4,d5,d6,d7, c)

            # INCREMENT INSTRUCTION REGISTER
            finc0, finc1, finc2, finc3, inc0, inc1, inc2, inc3, _ = self.incr.r(finc0, finc1, finc2, finc3, inc0, inc1, inc2, inc3, 0,0,0,0,0,0,0,0)
            self.ireg.r(1,0, finc0, finc1, finc2, finc3, inc0, inc1, inc2, inc3, c)

            #1100
            self.ireg.r(t3,0, a00, a01, a02, a03, a04, a05, a06, a07, c)
### CPU ###

######
'''
(0XXX)
ADD 0000 (REG REG)
SUB 0001 (REG REG)
AND 0010 (REG REG)
BOR 0011 (REG REG)
XOR 0100 (REG REG)
INV 0101 (REG ___)
INC 0110 (REG ___)
DEC 0111 (REG ___)

(1XXX)
MOV 1000 (NUM ADD)
STR 1001 (REG ADD)
LDR 1010 (REG ADD)
JMP 1011 (IAD ___)


0000 00000000 00000000
'''