from script                                             import control_string
from script.STDIN.WinSTDIN                              import stdin
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_if, for_try, for_switch, for_begin, for_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment
from script.LEXER.FUNCTION                              import main
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from statement                                          import InternalStatement as IS
from statement                                          import externalUnless as eUnless
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import UnlessError
try:  from CythonModules.Windows                        import fileError as fe 
except ImportError: from CythonModules.Linux            import fileError as fe

ke = bm.fg.rbg(255,255,0)

class EXTERNAL_UNLESS_STATEMENT:
    def __init__(self,
                master      :any, 
                data_base   :dict, 
                line        :int
                ):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def UNLESS_STATEMENT(self, 
                        bool_value  : bool, 
                        tabulation  : int = 0,
                        _type_      : str = 'conditional'
                        ):
        """
        :param bool_value:
        :param tabulation:
        :param _type_:
        :return:
        """
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.bool_value             = bool_value
        self.boolean_store          = [self.bool_value]
        self.index_else             = 0
        self.if_line                = self.line

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'unless' ]
        self.color                  = bm.fg.cyan_L
        self.loop                   = []
        self.max_emtyLine           = 5

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.line ).STDIN({ '0': ke, '1': self.color }, self.tabulation )
                if self.error is None:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string,
                                        normal_string=self.normal_string, data_base=self.data_base,  line=self.if_line).BLOCKS(
                                        tabulation=self.tabulation + 1, function=_type_, interpreter=False)

                        if self.error  is None:
                            if self.get_block   == 'begin:'     :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )
                                self._values_, self.error = for_begin.COMMENT_STATEMENT( master=self.master, data_base=self.data_base,
                                                        line=self.if_line  ).COMMENT( tabulation=self.tabulation + 1, color=self.color )
                                if self.error is None:
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else: break
                            elif self.get_block == 'if:'        :
                                self.store_value.append( self.normal_string )
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_if.INTERNAL_IF_STATEMENT(master=self.master,
                                        data_base=self.data_base, line=self.if_line).IF_STATEMENT( bool_value = self.value,
                                                                            tabulation=self.tabulation + 1, _type_ = _type_ )

                                if self.error is None:
                                    self.history.append( 'if' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else: break
                            elif self.get_block == 'unless:'    :
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = INTERNAL_UNLESS_STATEMENT( master=self.master,
                                        data_base=self.data_base, line=self.if_line ).UNLESS_STATEMENT( bool_value = self.value,
                                                                                tabulation=self.tabulation + 1, _type_=_type_)

                                if self.error is None:
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'unless' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else: break
                            elif self.get_block == 'for:'       :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )
                                
                                loop, tab, self.error = for_statement.EXTERNAL_FOR_STATEMENT( master=self.master,
                                                            data_base=self.data_base, line=self.if_line ).FOR_STATEMENT( tabulation=self.tabulation+1 )
                                if self.error is None:
                                    self.history.append( 'for' )
                                    self.space = 0
                                    self.loop.append( (loop, tab, self.error) )
                                else: break
                            elif self.get_block == 'try:'       :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )
                                
                                self._values_, self.error = for_try.INTERNAL_TRY_STATEMENT( master=self.master,
                                       data_base=self.data_base, line=self.if_line ).TRY_STATEMENT( tabulation = self.tabulation + 1,
                                                                                                 _type_=_type_)

                                if self.error is None:
                                    self.history.append( 'try' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else: break
                            elif self.get_block == 'switch:'    :
                                self.store_value.append(self.normal_string)
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_switch.SWITCH_STATEMENT( master=self.master,
                                            data_base=self.data_base, line=self.if_line ).SWITCH( main_values=self.value,
                                                                            tabulation=self.tabulation + 1, _type_=_type_)
                                
                                if self.error is None:
                                    self.history.append( 'switch' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else:  break
                            elif self.get_block == 'empty'      :
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append((self.normal_string, True))
                                else:
                                    self.error = UnlessError.ERRORS( self.if_line ).ERROR4()
                                    break
                            elif self.get_block == 'any'        :
                                self.store_value.append(self.normal_string)
                                self.space = 0
                                self.error      = main.SCANNER(master=self.value,data_base=self.data_base,
                                                            line=self.if_line).SCANNER(_id_ = 1, _type_= _type_, _key_=True)
                                if self.error is None: self.loop.append( (self.normal_string, True) )
                                else: break
                        else: break
                    else:
                        self.get_block, self.value, self.error = eUnless.EXTERNAL_BLOCKS(string=self.string,
                                        normal_string=self.normal_string, data_base=self.data_base,
                                                                            line=self.if_line).BLOCKS(tabulation=self.tabulation)

                        if self.error is None:
                            if self.get_block   == 'end:' :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append((self.normal_string, False))
                                    break
                                else:
                                    self.error = UnlessError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                    break
                            elif self.get_block == 'else:':
                                if self.index_else < 1:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append( 'else' )
                                        self.loop.append((self.normal_string, False))
                                    else:
                                        self.error = UnlessError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = UnlessError.ERRORS( self.if_line ).ERROR3( 'else' )
                                    break
                            elif self.get_block == 'empty':
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append((self.normal_string, False))
                                else:
                                    self.error = UnlessError.ERRORS( self.if_line ).ERROR4()
                                    break
                        else: break
                else:
                    if self.tabulation == 1: break
                    else:
                        self.get_block, self.value, self.error = eUnless.EXTERNAL_BLOCKS(string=self.string,
                                            normal_string=self.normal_string, data_base=self.data_base,
                                                                            line=self.if_line).BLOCKS(tabulation=self.tabulation)

                        if self.error is None:
                            if self.get_block   == 'end:' :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append((self.normal_string, False))
                                    break
                                else:
                                    self.error = UnlessError.ERRORS( self.if_line).ERROR2(self.history[ -1 ] )
                                    break
                            elif self.get_block == 'else:':
                                if self.index_else < 1:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append( 'else' )
                                        self.loop.append((self.normal_string, False))
                                    else:
                                        self.error = UnlessError.ERRORS( self.if_line ).ERROR2(self.history[-1])
                                        break
                                else:
                                    self.error = UnlessError.ERRORS( self.if_line ).ERROR3( 'else' )
                                    break
                            elif self.get_block == 'empty':
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append((self.normal_string, False))
                                else:
                                    self.error = UnlessError.ERRORS(  self.if_line ).ERROR4()
                                    break
                        else: break
            except KeyboardInterrupt:
                self.error = UnlessError.ERRORS( self.line ).ERROR4()
                break

        return self.loop, self.error

class INTERNAL_UNLESS_STATEMENT:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int,
                ):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def UNLESS_STATEMENT(self, 
                        bool_value  : bool, 
                        tabulation  : int,
                        _type_      : str = 'conditional' 
                        ):
        """
        :param bool_value:
        :param tabulation:
        :param _type_:
        :return:
        """
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.bool_value             = bool_value
        self.boolean_store          = [ self.bool_value ]
        self.index_else             = 0
        self.if_line                = self.line

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'unless' ]
        self.color                  = ke
        self.loop                   = []
        self.max_emtyLine           = 5

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.if_line ).STDIN({'0': ke, '1': self.color}, self.tabulation )

                if self.error is None:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string,
                                   normal_string=self.normal_string, data_base=self.data_base, line=self.if_line).BLOCKS(
                                                    tabulation=self.tabulation + 1, function=_type_, interpreter=False)

                        if self.error  is None:
                            if self.get_block   == 'begin:'     :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )
                                self._values_, self.error = for_begin.COMMENT_STATEMENT( master=self.master, data_base=self.data_base,
                                                            line=self.if_line ).COMMENT( tabulation=self.tabulation + 1, color=self.color )
                                if self.error is None:
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else: break
                            elif self.get_block == 'if:'        :
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_if.EXTERNAL_IF_STATEMENT(master=self.master,
                                            data_base=self.data_base, line=self.if_line ).IF_STATEMENT(bool_value=self.value,
                                                                            tabulation=self.tabulation + 1, _type_=_type_)

                                if self.error is None:
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'if' )
                                    self.space = 0
                                    self.loop.append(self._values_)
                                else:  break
                            elif self.get_block == 'try:'       :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )
                                
                                self._values_, self.error = for_try.INTERNAL_TRY_STATEMENT( master=self.master,
                                       data_base=self.data_base, line=self.if_line ).TRY_STATEMENT( tabulation = self.tabulation + 1,
                                                                                                 _type_=_type_)

                                if self.error is None:
                                    self.history.append( 'try' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else: break
                            elif self.get_block == 'unless:'    :
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = EXTERNAL_UNLESS_STATEMENT( master=self.master,
                                        data_base=self.data_base, line=self.if_line ).UNLESS_STATEMENT( bool_value=self.value,
                                                                                tabulation=self.tabulation + 1, _type_=_type_)

                                if self.error is None:
                                    self.store_value.append(self.normal_string)
                                    self.history.append( 'unless' )
                                    self.space = 0
                                    self.loop.append(self._values_)
                                else:  break
                            elif self.get_block == 'for:'       :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )
                                
                                loop, tab, self.error = for_statement.EXTERNAL_FOR_STATEMENT( master=self.master,
                                            data_base=self.data_base, line=self.if_line ).FOR_STATEMENT( tabulation=self.tabulation+1 )
                                if self.error is None:
                                    self.history.append( 'for' )
                                    self.space = 0
                                    self.loop.append( (loop, tab, self.error) )
                                else: break
                            elif self.get_block == 'switch:'    :
                                self.store_value.append(self.normal_string)
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_switch.SWITCH_STATEMENT( master=self.master,
                                            data_base=self.data_base, line=self.if_line ).SWITCH( main_values=self.value,
                                                                            tabulation=self.tabulation + 1, _type_=_type_)
                                if self.error is None:
                                    self.history.append( 'switch' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else:  break
                            elif self.get_block == 'empty'      :
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append((self.normal_string, True))
                                else:  self.error = UnlessError.ERRORS( self.if_line ).ERROR4()
                            elif self.get_block == 'any'        :
                                self.store_value.append(self.normal_string)
                                self.space = 0
                                self.error      = main.SCANNER(self.value, self.data_base,
                                                            self.line).SCANNER(_id_ = 1, _type_= _type_, _key_=True)
                                if self.error is None: self.loop.append( (self.normal_string, True) )
                                else: break
                        else: break
                    else:
                        self.get_block, self.value, self.error = eUnless.EXTERNAL_BLOCKS(string=self.string,
                                        normal_string=self.normal_string, data_base=self.data_base,
                                                                        line=self.if_line).BLOCKS(  tabulation=self.tabulation)

                        if self.error is None:
                            if self.get_block   == 'end:' :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append((self.normal_string, False))
                                    break
                                else:
                                    self.error = UnlessError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                    break
                            elif self.get_block == 'else:':
                                if self.index_else < 1:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append( 'else' )
                                        self.loop.append((self.normal_string, False))
                                    else:
                                        self.error = UnlessError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = UnlessError.ERRORS( self.if_line ).ERROR3( 'else' )
                                    break
                            elif self.get_block == 'empty':
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append((self.normal_string, False))
                                else:
                                    self.error = UnlessError.ERRORS( self.if_line ).ERROR4()
                                    break
                        else:break
                else:
                    self.get_block, self.value, self.error = eUnless.EXTERNAL_BLOCKS(string=self.string,
                                            normal_string=self.normal_string, data_base=self.data_base,
                                                                    line=self.if_line).BLOCKS( tabulation=self.tabulation)

                    if self.error is None:
                        if self.get_block   == 'end:' :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.loop.append((self.normal_string, False))
                                break
                            else:
                                self.error = UnlessError.ERRORS( self.if_line ).ERROR2(self.history[ -1 ])
                                break
                        elif self.get_block == 'else:':
                            if self.index_else < 1:
                                if self.store_value:
                                    self.index_else             += 1
                                    self.key_else_activation    = True
                                    self.store_value            = []
                                    self.history.append( 'else' )
                                    self.loop.append((self.normal_string, False))
                                else:
                                    self.error = UnlessError.ERRORS( self.if_line ).ERROR2(self.history[ -1 ])
                                    break
                            else:
                                self.error = UnlessError.ERRORS( self.if_line ).ERROR3( 'else' )
                                break
                        elif self.get_block == 'empty':
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.loop.append((self.normal_string, False))
                            else:
                                self.error = UnlessError.ERRORS( self.if_line ).ERROR4()
                                break
                    else: break
            except KeyboardInterrupt:
                self.error = UnlessError.ERRORS( self.if_line ).ERROR4()
                break

        return self.loop, self.error
