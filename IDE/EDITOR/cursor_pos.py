import sys
import termios, sys,tty
from IDE.EDITOR                             import details
from script.STDIN.LinuxSTDIN                import bm_configure     as bm
from IDE.EDITOR                             import true_cursor_pos  as cursor_pos
from IDE.EDITOR                             import test 
from script.STDIN.LinuxSTDIN                import ascii
from src.classes                            import error 
from script.STDIN.LinuxSTDIN                import readchar

class new_windows:
    def __init__(self, srt : str = "", line : int = 1):
        self.left       = bm.init.bold+bm.fg.red_L+'>'
        self.right      = bm.init.bold+bm.fg.red_L+'<'
        self.re         = bm.init.reset
        self.w          = bm.bg.black_L+bm.init.bold+bm.fg.white_L
        self.ww         = bm.init.bold+bm.fg.white_L
        self.srt        = " " * len(srt) + "     "
        self.r          = bm.init.bold+bm.fg.rbg(255, 0, 0)
        self.line       = line
        
    def cursor_pos(self, list_of_values: list, true_chaine: str = "", length : int = 1):
        def number(num : int):
            if num <= 9:  return self.ww+'[ '+self.r+f"{num}"+self.re+self.ww+']'+self.re
            else: return self.ww+'['+self.r+f"{num}"+self.re+self.ww+']'+self.re
        
        def select_number(str_ : str):
            try: num = int( str_[1:])
            except TypeError: num = 0
            
            return num 
        
        def id_pos(num: str, w : str, m : str, r: str, c: str):
            l = len(num)
            s = " " * (6-l+1)
            v = f'{v}[ {m}i{r} {w}]   ={c}{num}{r}'+s
        
        
        r = bm.init.reset
        c = bm.init.bold+bm.fg.rbg(255, 0, 255)
        m = bm.init.bold+bm.fg.rbg(0, 255, 255)
        w = bm.init.bold+bm.fg.rbg(255, 255, 255)
        blink = bm.init.blink
        self.pos_x, self.pos_y      = cursor_pos.cursor()
        self.pos_x, self.pos_y      = int(self.pos_x), int( self.pos_y)
        self.max_x, self.max_y      = test.get_linux_ter()
        
        self.disp       = " " * (len(true_chaine)+4)
        self.srt        = self.disp
        self.asc        = ascii.frame(True)
        
        self.list       = list_of_values  
        self.index      = 0 
        self.value      = None
        self.details    = len('[d]     = details ')
        if self.details > length: self.len = self.details
        else: self.len = length+1
        self.val1       = f'{w}[{m}Enter{w}] = {c}{blink}select  {r}'
        self.val2       = f'{w}[{m}q{w}]     = {c}{blink}exit    {r}'
        self.val3       = f'{w}[{m}d{w}]     = {c}{blink}details {r}'
        self.empty      = " "
        self.val1       = f"{self.asc['v']} " + self.val1+self.re + self.w+self.empty * (self.len - len(self.val1))+f"{self.asc['v']}"
        self.val2       = f"{self.asc['v']} " + self.val2+self.re + self.w+self.empty * (self.len - len(self.val2))+f"{self.asc['v']}"
        self.val3       = f"{self.asc['v']} " + self.val3+self.re + self.w+self.empty * (self.len - len(self.val3))+f"{self.asc['v']}"
        self.store_id   = []
        self.string     = ""
        self.err        = None
        self.border_x_limit = self.max_x - int(self.pos_x)
        if self.border_x_limit < length +10 : self.srt = ''
        else: pass
        
        sys.stdout.write(bm.save.save)
        sys.stdout.write("\n")
        sys.stdout.write(self.srt + '  '+self.w+self.asc['ul']+self.asc['h']*(self.len+1)+self.asc['ur'] + self.re+'\n')

        for j, name in enumerate(self.list):
            name = f"{self.asc['v']} " + bm.words(name, self.w).final() +self.re + self.w+self.empty * (self.len - len(name))+f"{self.asc['v']}"+self.re+' '+number(j)
            sys.stdout.write(self.srt + '  '+self.w+ name +self.re+'\n')
            
        sys.stdout.write(self.srt + '  '+self.w+f"{self.asc['v']}"+' '*(self.len+1)+f"{self.asc['v']}" + self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+self.asc['vl']+self.asc['h']*(self.len+1)+self.asc['vr'] + self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+ self.val1+self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+ self.val2+self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+ self.val3+self.re+'\n')
        sys.stdout.write(self.srt + '  '+self.w+self.asc['dl']+self.asc['h']*(self.len+1)+self.asc['dr'] + self.re+'\n')
        
        self.m = len(self.list)+6
        for j in range(self.m):
            sys.stdout.write(bm.move_cursor.UP(pos=1))
        
        sys.stdout.write(bm.move_cursor.RIGHT(pos=len(self.srt)))
    
        sys.stdout.write(bm.save.save)
        sys.stdout.flush() 
        
        while True:
            try:
                self.char = readchar.readchar()
                # keyboardInterrupt
                if   self.char == 3:
                    sys.stdout.write(bm.save.restore)
                    sys.stdout.write(bm.move_cursor.UP(pos=1))
                    sys.stdout.write(bm.clear.screen(pos=0))
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                    self.value = None
                    return
                #moving up and down 
                elif self.char == 27:
                    next1, next2 = ord( sys.stdin.read(1)), ord( sys.stdin.read(1))
                    if next1 == 91:
                        try:
                            # moving cursor down
                            if   next2 == 66:
                                if self.index < len(self.list)-1:
                                    self.index += 1
                                    sys.stdout.write(bm.move_cursor.DOWN(pos=1))
                                    self.store_id.append(self.index)
                                else: pass
                            # moving cursor left
                            elif next2 == 65: 
                                if self.index > 0: 
                                    self.index -=1 
                                    sys.stdout.write(bm.move_cursor.UP(pos=1))
                                    self.store_id.append(self.index)
                                else: pass
                            else: pass
                        except IndexError: pass
                    else: pass            
                # selction 
                elif self.char in {10, 13}: # Enter
                    try:
                        if self.string:
                            self.index = select_number( self.string )
                            try: self.value = self.list[ self.index ]
                            except IndexError: 
                                self.err = error.ERRORS( self.line ).ERROR62( self.index )
                                self.value = None
                                sys.stdout.write(bm.save.restore)
                                sys.stdout.write(bm.move_cursor.UP(pos=1))
                                sys.stdout.write(bm.clear.screen(pos=0))
                                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                break
                        else: self.value = self.list[ self.index ]
                        sys.stdout.write(bm.save.restore)
                        sys.stdout.write(bm.move_cursor.UP(pos=1))
                        sys.stdout.write(bm.clear.screen(pos=0))
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        break
                    except IndexError: 
                        sys.stdout.write(bm.save.restore)
                        sys.stdout.write(bm.move_cursor.UP(pos=1))
                        sys.stdout.write(bm.clear.screen(pos=0))
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        self.err = error.ERRORS( self.line ).ERROR62( self.index )
                        self.value = None
                        break
                # breaking without selecting (q)
                elif self.char == 113 : 
                    sys.stdout.write(bm.save.restore)
                    sys.stdout.write(bm.move_cursor.UP(pos=1))
                    sys.stdout.write(bm.clear.screen(pos=0))
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                    self.value = None
                    return
                # index selection mode [0, ...., 9]
                elif self.char in [x for x in range(48, 58)]: 
                    if self.string: self.string += chr(self.char)
                    else: 
                        if self.index <= len(self.list)-1:
                            self.index = int( chr(self.char))
                            if self.index  <= len(self.list)-1:
                                if not self.store_id: sys.stdout.write(bm.move_cursor.DOWN(pos=self.index))
                                else: 
                                    if   self.store_id[-1] == self.index: pass
                                    elif self.store_id[-1] > self.index :
                                        new_id =  abs(self.store_id[-1] - self.index )
                                        sys.stdout.write(bm.move_cursor.UP(pos=new_id))
                                    else: 
                                        new_id =  abs(self.store_id[-1] - self.index )
                                        sys.stdout.write(bm.move_cursor.DOWN(pos=new_id))
                                self.store_id.append(self.index)
                            else:
                                sys.stdout.write(bm.save.restore)
                                sys.stdout.write(bm.move_cursor.UP(pos=1))
                                sys.stdout.write(bm.clear.screen(pos=0))
                                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                                self.err = error.ERRORS( self.line ).ERROR62( self.index )
                                self.value = None
                                break
                        else: 
                            sys.stdout.write(bm.save.restore)
                            sys.stdout.write(bm.move_cursor.UP(pos=1))
                            sys.stdout.write(bm.clear.screen(pos=0))
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            self.err = error.ERRORS( self.line ).ERROR62( self.index )
                            self.value = None
                            break
                # bottom
                elif self.char == 98:
                    if self.index < len(self.list)-1:
                        self.index = len(self.list)-1
                        if not self.store_id: sys.stdout.write(bm.move_cursor.DOWN(pos=self.index))
                        else: 
                            if   self.store_id[-1] == self.index: pass
                            else: 
                                new_id =  abs(self.store_id[-1] - self.index )
                                sys.stdout.write(bm.move_cursor.DOWN(pos=new_id))
                        self.store_id.append(self.index)
                    else: pass
                # top
                elif self.char == 116:
                    if self.index <= len(self.list)-1:
                        self.index = 0
                        if not self.store_id: pass
                        else: 
                            if   self.store_id[-1] == self.index: pass
                            else:  
                                new_id =  abs(self.store_id[-1] - self.index )
                                sys.stdout.write(bm.move_cursor.UP(pos=new_id))
                        self.store_id.append(self.index)
                    else: pass     
                # middle
                elif self.char == 109:
                    if len(self.list) > 4 and len(self.list) % 2 == 0:
                        self.index = int( len(self.list) / 2)
                        if not self.store_id: sys.stdout.write(bm.move_cursor.DOWN(pos=self.index))
                        else: 
                            if   self.store_id[-1] == self.index: pass
                            elif self.store_id[-1] > self.index :
                                new_id =  abs(self.store_id[-1] - self.index )
                                sys.stdout.write(bm.move_cursor.UP(pos=new_id))
                            else: 
                                new_id =  abs(self.store_id[-1] - self.index )
                                sys.stdout.write(bm.move_cursor.DOWN(pos=new_id))              
                        self.store_id.append(self.index)
                    else: pass
                elif self.char == 105: 
                    if not self.string: self.string += chr(self.char)
                    else: 
                        self.string = ""
                        self.string += chr(self.char)  
                # get more details <d>....
                elif  self.char == 100:
                    try:
                        sys.stdout.write(bm.save.restore)
                        sys.stdout.write(bm.move_cursor.UP(pos=2))
                        sys.stdout.write(bm.clear.screen(pos=0))
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        self.srt = " "*len(true_chaine)
                        details.Details(self.srt, self.line).Details(self.list[self.index])
                        self.value = None
                        break 
                    except IndexError: pass
                else: pass
                    
                sys.stdout.flush() 
                
            except KeyError:
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(self._keyboard_)
                return
            
        return self.value, self.err
 
        
