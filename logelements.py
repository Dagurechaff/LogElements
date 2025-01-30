class TLogElement:
    """Базовый класс для логического элемента."""
    def __init__(self):
        self.__in1 = 0
        self.__in2 = 0
        self._res = 0
        if not hasattr(self, "_calc"):
            raise NotImplementedError("Нельзя создать такой объект!!!")

    def __setQ(self, newQ):
        if newQ in (0, 1):
            self.__Q = newQ
            self._calc()

    def __setIn1(self, newIn1):
        if newIn1 in (0, 1):
            self.__in1 = newIn1
            self._calc()

    def __setIn2(self, newIn2):
        if newIn2 in (0, 1):
            self.__in2 = newIn2
            self._calc()
    Q = property(lambda self: self._TLogElement__Q, __setQ)
    In1 = property(lambda self: self._TLogElement__in1, __setIn1)
    In2 = property(lambda self: self._TLogElement__in2, __setIn2)
    Res = property(lambda self: self._res)


class TNot(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)
    def _calc(self):
        self._res = int(not self.In1)


class TAnd(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)
    def _calc(self):
        self._res = self.In1 * self.In2

class Tor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)
    def _calc(self):
        if self.In1 == self.In2 == 1:
            self._res = 1
        else:
            self._res = self.In1 + self.In2


class T_ecvival(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)
    def _calc(self):
        if self.In1 == self.In2:
            self._res = 1
        else:
            self._res = 0
class T_em(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)
    def _calc(self):
        if self.In1 == self.In2:
            self._res = 1
        elif self.In1==0 and self.In2==1:
            self._res=1
        else:
            self._res = 0
class Txor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)
    def _calc(self):
        if self.In1 != self.In2:
            self._res = 1
        else:
            self._res = 0


class TNAnd(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)
    def _calc(self):
        self._res = int(not(self.In1 * self.In2))


class TNor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)
    def _calc(self):
        if self.In1 == self.In2 == 0:
            self._res = 1
        elif self.In1 == self.In2 == 1:
            self._res = 0
        else:
            self._res = int(not(self.In1 + self.In2))

'''print('---И')
trigger_and = TAnd()
for x in 0,1:
    for y in 0,1:
        trigger_and.In1 = x
        trigger_and.In2 = y
        print(trigger_and.In1,trigger_and.In2,trigger_and._res)
print('---Или')
trigger_or = Tor()
for x in 0,1:
    for y in 0,1:
        trigger_or.In1 = x
        trigger_or.In2 = y
        print(trigger_or.In1,trigger_or.In2,trigger_or._res)
print('---Эквивалентность')
trigger_ecviv = T_ecvival()
for x in 0,1:
    for y in 0,1:
        trigger_ecviv.In1 = x
        trigger_ecviv.In2 = y
        print(trigger_ecviv.In1,trigger_ecviv.In2,trigger_ecviv._res)'''
