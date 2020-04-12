# Mainali, Ashish
# axm3019
# 2020-03-27
#---------#---------#---------#---------#---------#--------#
# A simple calculator with variables.

import sys

#---------#---------#---------#---------#---------#--------#
# Lexical analysis section.

# TODO: Add the additional token categories here.
tokens = (
  'INTEGER', 'ID',
  'PLUS', 'ASSIGN',
  'LPAREN', 'RPAREN',
  )

# TODO: Add specifications for the new token categories here.
# Tokens
t_PLUS    = r'\+'
t_ASSIGN  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ID      = r'[a-z_][a-z0-9_]*'

# TODO: Put your definition for t_REAL here.

def t_INTEGER( t ) :
  r'\d+'
  t.value = int(t.value)
  return t

# Ignored characters
t_ignore = " \t"

def t_newline( t ) :
  r'\n+'
  t.lexer.lineno += t.value.count("\n")

def t_error( t ) :
  print( "Illegal character '%s'" % t.value[0] )
  t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

#---------#---------#---------#---------#---------#--------#
# Syntactic section.

# TODO: Add precedence and associativity rules for the
#       new operators here.
# Precedence rules for the arithmetic operators
precedence = (
  ( 'left',  'PLUS' ),
  )

# Dictionary of names (for storing variables)
names = dict()

def p_statement_assign( p ) :
  'statement : ID ASSIGN expression'
  names[ p[1] ] = p[3]
  print( f'{p[1]} = {p[3]}' )

def p_statement_expr( p ) :
  'statement : expression'
  print( p[1] )

# TODO: Update the production rule and processing to deal with
#       all of the new binary operators.
def p_expression_binop( p ) :
  '''expression : expression PLUS expression'''
  if   p[2] == '+' : p[0] = p[1] + p[3]

# TODO: Write a p_expression_unop() routine here to deal with
#       the unary operators.

def p_expression_group( p ) :
  'expression : LPAREN expression RPAREN'
  p[0] = p[2]

# TODO: Update the production rule to deal with REAL.
def p_expression_number( p ) :
  '''expression : INTEGER'''
  p[0] = p[1]

def p_expression_name( p ) :
  'expression : ID'

  try:
    p[0] = names[p[1]]

  except LookupError:
    print( "Undefined name '%s'" % p[1] )
    p[0] = 0

def p_error( p ) :
  print( "Syntax error at '%s'" % p.value )

# Build the parser
import ply.yacc as yacc
yacc.yacc()

#-----------------------------------------------------------
def main() :
  fName = sys.argv[ 1 ]
  print( 'processing expressions from ' + fName + ' ...' )

  with open( fName, 'r' ) as fp :
    lines = fp.read().replace( '\r', '' ).split( '\n' )

  for line in lines :
    if line != '' :
      print( f'{line} ==> ', end='' )
      yacc.parse( line )

if __name__ == '__main__' :
  main()

#-----------------------------------------------------------

