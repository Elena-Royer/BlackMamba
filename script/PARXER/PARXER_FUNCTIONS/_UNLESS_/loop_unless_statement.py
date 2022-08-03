import cython
from script                                             import control_string
from script.STDIN.WinSTDIN                              import stdin
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import end_else_elif
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.PARXER.PARXER_FUNCTIONS._IF_                import if_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.LEXER.FUNCTION                              import main
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try:  from CythonModules.Windows                        import fileError as fe 
except ImportError: from CythonModules.Linux            import fileError as fe
try:  from CythonModules.Linux                          import loop_for
except ImportError: from CythonModules.Windows          import loop_for

ke = bm.fg.rbg(255, 255,0)

@cython.cclass
class EXTERNAL_UNLESS_FOR_STATEMENT:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int
                ):
        
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def UNLESS_STATEMENT(self, 
                        bool_value      : bool, 
                        tabulation      : int   = 0, 
                        loop_list       : any   = None, 
                        _type_          : str   = 'conditional',
                        keyPass         : bool  = False
                        ):
        
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.bool_value             = bool_value
        self.boolean_store          = [self.bool_value]
        self.index_else             = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'unless' ]
        self.before                 = end_else_elif.CHECK_VALUES( self.data_base ).BEFORE()
        self.loop_list              = loop_list
        self.next_line              = None

        ############################################################################
        self.keyPass                = keyPass 
        self.max_emtyLine           = 5
        ############################################################################
        
        if self.keyPass is False:
            for j, _string_ in enumerate(self.loop_list):
                if j != self.next_line:
                    
                    self.if_line                        += 1
                    self.line                           += 1
                    
                    self.normal_string, self.active_tab = _string_
                    self.string                         = self.normal_string

                    if self.string:
                        if self.active_tab is True:
                            self.get_block, self.value, self.error = end_else_elif.INTERNAL_BLOCKS( self.string,
                                            self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )

                            if self.error  is None:
                                if self.get_block   == 'begin:'     :
                                    self.next_line  = j + 1
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    
                                    if self.history[ -1 ] in ['else']:
                                        if self.bool_value is False :
                                            self.error = comment.COMMENT_LOOP_STATEMENT( self.master, self.data_base, 
                                                                self.line ).COMMENT( self.tabulation + 1,  self.loop_list[ j + 1 ], 
                                                                                         keyPass = self.keyPass) 
                                            if self.error is None: pass
                                            else: pass
                                        else: pass
                                    else: 
                                        self.error = comment.COMMENT_LOOP_STATEMENT( self.master, self.data_base, 
                                                                        self.line ).COMMENT( self.tabulation + 1,  self.loop_list[ j + 1 ],
                                                                                            keyPass = self.keyPass ) 
                                        if self.error is None: pass
                                        else: break

                                elif self.get_block == 'if:'        :
                                    self.next_line  = j + 1
                                    if self.history[ -1 ] in [ 'else' ]:
                                        if self.bool_value is False:
                                            self.error = if_statement.INTERNAL_IF_LOOP_STATEMENT(  self.master,
                                                    self.data_base, self.line).IF_STATEMENT( self.value, self.tabulation + 1,
                                                                                        self.loop_list[ j + 1 ], _type_ = _type_, keyPass = self.keyPass)
                                            if self.error is None:
                                                self.store_value.append( self.normal_string )
                                                self.history.append( 'if' )
                                                self.space = 0
                                            else: break
                                        else:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'if' )
                                            self.space = 0
                                    else:
                                        self.error = if_statement.INTERNAL_IF_LOOP_STATEMENT( self.master,
                                                    self.data_base, self.line).IF_STATEMENT( self.value, self.tabulation + 1,
                                                    self.loop_list[ j + 1 ],  _type_ = _type_, keyPass = self.keyPass)
                                        if self.error is None:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'if' )
                                            self.space = 0
                                        else: break
                                        
                                elif self.get_block == 'unless:'    :
                                    self.next_line  = j + 1
                                    if self.history[ -1 ] in [ 'else' ]:
                                        if self.bool_value is False:
                                            self.error = INTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                                self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                self.loop_list[ j + 1 ], _type_ = _type_, keyPass = self.keyPass )
                                            if self.error is None:
                                                self.store_value.append( self.normal_string )
                                                self.history.append( 'unless' )
                                                self.space = 0
                                            else: break
                                        else:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'unless' )
                                            self.space = 0
                                    else:
                                        self.error = INTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                                self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                self.loop_list[ j + 1 ], _type_ = _type_, keyPass = self.keyPass )
                                        if self.error is None:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'unless' )
                                            self.space = 0
                                        else: break

                                elif self.get_block == 'try:'       :
                                    self.next_line = j + 1
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'try' )
                                    self.space = 0
                                    
                                    if self.data_base[ 'pass' ] is None: pass 
                                    else: self.keyPass = True
                                    
                                    if self.history[ -1 ] in [ 'else' ]:
                                        if self.bool_value is False:
                                            self.error = try_statement.INTERNAL_TRY_FOR_STATEMENT( self.master,
                                                    self.data_base, self.line).TRY_STATEMENT( self.tabulation + 1,
                                                                    self.loop_list[ self.next_line], keyPass = self.keyPass, _type_ = _type_ )
                                        if self.error is None:  self.keyPass    = False
                                    else:
                                        self.error = try_statement.INTERNAL_TRY_FOR_STATEMENT( self.master,
                                                    self.data_base, self.line).TRY_STATEMENT( self.tabulation + 1,
                                                                    self.loop_list[ self.next_line], keyPass = self.keyPass, _type_ = _type_ )
                                    if self.error is None: pass
                                    else: break

                                elif self.get_block == 'switch:'    :
                                    self.next_line  = j + 1
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    
                                    if self.history[ -1 ] in ['else']:
                                        if self.bool_value is False :
                                            self.error = switch_statement.SWITCH_LOOP_STATEMENT( self.master , self.data_base,
                                                            self.line ).SWITCH( self.value, self.tabulation + 1, self.loop_list[ j + 1 ],
                                                                               _type_ = _type_, keyPass = self.keyPass)
                                            
                                            if self.error is None: pass
                                            else: pass
                                        else: pass
                                    else: 
                                        self.error = switch_statement.SWITCH_LOOP_STATEMENT( self.master , self.data_base,
                                                            self.line ).SWITCH( self.value, self.tabulation + 1, self.loop_list[ j + 1 ],
                                                                               _type_ = _type_, keyPass = self.keyPass)
                                        if self.error is None: pass
                                        else: break

                                elif self.get_block == 'empty'      :
                                    if self.space <= self.max_emtyLine :
                                        self.space += 1
                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break

                                elif self.get_block == 'any'        :
                                    self.store_value.append(self.normal_string)
                                    if self.bool_value is False:
                                        if self.data_base[ 'pass' ] is None:
                                            self.error = self.lex_par.LEXER_AND_PARXER(self.value, self.data_base,
                                                                self.line).ANALYZE( _id_=1, _type_= _type_ )
                                            if self.error is None:
                                                self.space = 0
                                            else: break
                                        else:
                                            self.keyPass = True
                                            self.error = main.SCANNER(self.value, self.data_base,
                                                    self.line).SCANNER(_id_=1, _type_= _type_, _key_=True)

                                            if self.error is None: self.space = 0
                                            else: break
                                    else:
                                        self.error = main.SCANNER(self.value, self.data_base,
                                                    self.line).SCANNER(_id_=1, _type_= _type_, _key_=True)

                                        if self.error is None: self.space = 0
                                        else: break
                            else:  break
                        else:
                            self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )

                            if self.error is None:
                                if self.get_block   == 'end:' :
                                    if self.store_value:
                                        del self.store_value[ : ]
                                        del self.history[ : ]
                                        del self.boolean_store[ : ]
                                        break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                        break

                                elif self.get_block == 'else:':
                                    if self.index_else < 1:
                                        if self.store_value:
                                            self.index_else             += 1
                                            self.key_else_activation    = True
                                            self.store_value            = []
                                            self.history.append( 'else' )
                                            self.bool_key               = None

                                            for _bool_ in self.boolean_store:
                                                if _bool_ == True:
                                                    self.bool_key = True
                                                    break
                                                else: self.bool_key = False

                                            if self.bool_key is True: self.bool_value = False
                                            else: self.bool_value = True

                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR3( 'else' )
                                        break

                                elif self.get_block == 'empty':
                                    if self.space <= self.max_emtyLine : self.space += 1
                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break
                            else: break
                    else: pass 
                else:
                    self.if_line        += 1
                    self.line           += 1
                    self.next_line      = None

            self.after      = end_else_elif.CHECK_VALUES( self.data_base ).AFTER()
            self.error      = end_else_elif.CHECK_VALUES( self.data_base ).UPDATE( self.before, self.after, self.error )
        else: pass 
        
        return self.error

@cython.cclass
class INTERNAL_UNLESS_FOR_STATEMENT:
    def __init__(self,
                master      : any, 
                data_base   : dict, 
                line        : int
                ):
        
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def UNLESS_STATEMENT(self, 
                        bool_value      : bool, 
                        tabulation      : int   = 0, 
                        loop_list       : any   = None, 
                        _type_          : str   = 'conditional',
                        keyPass         : bool  = False
                        ):
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.bool_value             = bool_value
        self.boolean_store          = [self.bool_value]
        self.index_else             = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'unless' ]
        self.before                 = end_else_elif.CHECK_VALUES( self.data_base ).BEFORE()
        self.loop_list              = loop_list
        self.next_line              = None

        ############################################################################
        self.keyPass                = keyPass 
        self.max_emtyLine           = 5
        ############################################################################
        
        if self.keyPass is False:
            for j, _string_ in enumerate( self.loop_list ):
                if j != self.next_line:

                    self.if_line                        += 1
                    self.line                           += 1
                    
                    self.normal_string, self.active_tab = _string_
                    self.string                         = self.normal_string

                    if self.string:
                        if self.active_tab is True:

                            self.get_block, self.value, self.error = end_else_elif.INTERNAL_BLOCKS( self.string,
                                            self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )

                            if self.error  is None:
                                if   self.get_block == 'begin:'     :
                                    self.next_line  = j + 1
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    
                                    if self.history[ -1 ] in ['else']:
                                        if self.bool_value is False :
                                            self.error = comment.COMMENT_LOOP_STATEMENT( self.master, self.data_base, 
                                                                            self.line ).COMMENT( self.tabulation + 1,  self.loop_list[ j + 1 ]) 
                                            if self.error is None: pass
                                            else: pass
                                        else: pass
                                    else: 
                                        self.error = comment.COMMENT_LOOP_STATEMENT( self.master, self.data_base, 
                                                                        self.line ).COMMENT( self.tabulation + 1,  self.loop_list[ j + 1 ]) 
                                        if self.error is None: pass
                                        else: break
                                
                                elif self.get_block == 'if:'        :
                                    self.next_line  = j + 1
                                    if self.history[ -1 ] in [ 'else' ]:
                                        if self.bool_value is False:
                                            self.error = if_statement.EXTERNAL_IF_LOOP_STATEMENT(  self.master,
                                                    self.data_base, self.line).IF_STATEMENT( self.value, self.tabulation + 1,
                                                                                        self.loop_list[ j + 1 ], _type_ = _type_)
                                            if self.error is None:
                                                self.store_value.append( self.normal_string )
                                                self.history.append( 'if' )
                                                self.space = 0
                                            else: break
                                        else:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'if' )
                                            self.space = 0
                                    else:
                                        self.error = if_statement.EXTERNAL_IF_LOOP_STATEMENT( self.master,
                                                    self.data_base, self.line).IF_STATEMENT( self.value, self.tabulation + 1,
                                                    self.loop_list[ j + 1 ],  _type_ = _type_ )
                                        if self.error is None:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'if' )
                                            self.space = 0
                                        else: break
                                    
                                elif self.get_block == 'unless:'    :
                                    self.next_line  = j + 1
                                    if self.history[ -1 ] in [ 'else' ]:
                                        if self.bool_value is False:
                                            self.error = EXTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                                self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                self.loop_list[ j + 1 ], _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append( self.normal_string )
                                                self.history.append( 'unless' )
                                                self.space = 0
                                            else: break
                                        else:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'unless' )
                                            self.space = 0
                                    else:
                                        self.error = EXTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                                self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                self.loop_list[ j + 1 ], _type_ = _type_ )
                                        if self.error is None:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'unless' )
                                            self.space = 0
                                        else: break
                                        
                                elif self.get_block == 'try:'       :
                                    self.next_line = j + 1
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'try' )
                                    self.space = 0
                                    
                                    if self.data_base[ 'pass' ] is None: pass 
                                    else: self.keyPass = True
                                    
                                    if self.history[ -1 ] in [ 'else' ]:
                                        if self.bool_value is False:
                                            self.error = try_statement.EXTERNAL_TRY_FOR_STATEMENT( self.master,
                                                    self.data_base, self.line).TRY_STATEMENT( self.tabulation + 1,
                                                                    self.loop_list[ self.next_line], keyPass = self.keyPass, _type_ = _type_ )
                                        if self.error is None:  self.keyPass    = False
                                    else:
                                        self.error = try_statement.EXTERNAL_TRY_FOR_STATEMENT( self.master,
                                                    self.data_base, self.line).TRY_STATEMENT( self.tabulation + 1,
                                                                    self.loop_list[ self.next_line], keyPass = self.keyPass, _type_ = _type_ )
                                    if self.error is None: pass
                                    else: break

                                elif self.get_block == 'switch:'    :
                                    self.next_line  = j + 1
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    
                                    if self.history[ -1 ] in ['else']:
                                        if self.bool_value is False :
                                            self.error = switch_statement.SWITCH_LOOP_STATEMENT( self.master , self.data_base,
                                                            self.line ).SWITCH( self.value, self.tabulation + 1, self.loop_list[ j + 1 ],
                                                                               _type_ = _type_, keyPass = self.keyPass)
                                            if self.error is None: pass
                                            else: pass
                                        else: pass
                                    else: 
                                        self.error = switch_statement.SWITCH_LOOP_STATEMENT( self.master , self.data_base,
                                                            self.line ).SWITCH( self.value, self.tabulation + 1, self.loop_list[ j + 1 ],
                                                                               _type_ = _type_, keyPass = self.keyPass)
                                        if self.error is None: pass
                                        else: break

                                elif self.get_block == 'empty'      :
                                    if self.space <= self.max_emtyLine:
                                        self.space += 1
                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break

                                elif self.get_block == 'any'        :
                                    self.store_value.append(self.normal_string)
                                    if self.bool_value is False:
                                        self.error = self.lex_par.LEXER_AND_PARXER(self.value, self.data_base,
                                                            self.line).ANALYZE( _id_=1, _type_='conditional' )

                                        if self.error is None:
                                            self.space = 0
                                        else:
                                            self.error = self.error
                                            break
                                    else:
                                        self.keyPass = True
                                        self.error = main.SCANNER(self.value, self.data_base,
                                                    self.line).SCANNER(_id_=1, _type_='conditional', _key_=True)

                                        if self.error is None:
                                            self.space = 0
                                        else:
                                            break

                            else:break
                        else:
                            self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )

                            if self.error is None:
                                if self.get_block   == 'end:' :
                                    if self.store_value:
                                        del self.store_value[ : ]
                                        del self.history[ : ]
                                        del self.boolean_store[ : ]

                                        break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                        break
                                
                                elif self.get_block == 'else:':
                                    if self.index_else < 1:
                                        if self.store_value:
                                            self.index_else             += 1
                                            self.key_else_activation    = True
                                            self.store_value            = []
                                            self.history.append( 'else' )
                                            self.bool_key               = None

                                            for _bool_ in self.boolean_store:
                                                if _bool_ == True:
                                                    self.bool_key = True
                                                    break
                                                else: self.bool_key = False

                                            if self.bool_key is True: self.bool_value = False
                                            else: self.bool_value = True

                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR3( 'else' )
                                        break

                                elif self.get_block == 'empty':
                                    if self.space <= self.max_emtyLine : self.space += 1
                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break
                            
                            else: break
                    else: pass
                else:
                    self.if_line        += 1
                    self.line           += 1
                    self.next_line      = None

            self.after      = end_else_elif.CHECK_VALUES( self.data_base ).AFTER()
            self.error      = end_else_elif.CHECK_VALUES( self.data_base ).UPDATE( self.before, self.after, self.error )
        else: pass 
        
        return self.error

class ERRORS:
    def __init__(self, line: int):
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white,
                                                                                    self.cyan, string) + error
        return self.error+self.reset

    def ERROR1(self, string: str = 'else'):
        error = '{}is already defined. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. {}<< {} >> {}block '.format(self.white,
                                                                                self.cyan, string, self.green) + error
        return self.error+self.reset

    def ERROR2(self, string):
        error = '{}no values {}in the previous statement {}<< {} >> {}block. {}line: {}{}'.format(self.green, self.white, self.cyan, string, self.green,
                                                                                             self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax '.format( self.white ) + error

        return self.error+self.reset

    def ERROR3(self, string: str = 'else'):
        error = 'due to {}many {}<< {} >> {}blocks. {}line: {}{}'.format(self.green, self.cyan, string, self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax '.format( self.white ) + error

        return self.error+self.reset

    def ERROR4(self):
        self.error =  fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format(self.yellow,
                                                                                    self.white, self.yellow, self.line )
        return self.error+self.reset
    
    def ERROR5(self, _str_ : str = 'if'):
        error = '{}close the opening statement {}<< {} >> . {}line: {}{}'.format(self.yellow, self.blue, _str_, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. '.format( self.white ) + error

        return self.error+self.reset