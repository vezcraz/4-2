
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'assignment comma in integer is move operation stop string to value var\n\tevaluate : exp_assign\n\t\t\t | exp_move\n\t\t\t | exp_naming\n\t\t\t | exp_value\n\t\t\t | no_stop\n\t\t\t | empty\n\t\n\texp_assign : assignment integer to integer comma integer stop\n\t\n\texp_move : operation move stop\n\t\n\texp_naming : var string is integer comma integer stop\n\t\t\t   | var operation is integer comma integer stop\n\t\t\t   | var move is integer comma integer stop\n\t\t\t   | var var is integer comma integer stop\n\t\t\t   | var is is integer comma integer stop\n\t\t\t   | var assignment is integer comma integer stop\n\t\n\texp_value : value in integer comma integer stop\n\n\t\n\tno_stop : operation move\n            | assignment integer to integer comma integer\n            | var string is integer comma integer\n            | value in integer comma integer\n\t\n\tempty :\n\t'
    
_lr_action_items = {'assignment':([0,10,],[8,19,]),'operation':([0,10,],[9,17,]),'var':([0,10,],[10,14,]),'value':([0,],[11,]),'$end':([0,1,2,3,4,5,6,7,13,22,45,46,48,53,54,55,56,57,58,59,60,],[-20,0,-1,-2,-3,-4,-5,-6,-16,-8,-19,-17,-18,-15,-7,-12,-9,-13,-10,-11,-14,]),'integer':([8,20,21,23,24,25,26,27,28,37,38,39,40,41,42,43,44,],[12,29,30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,]),'move':([9,10,],[13,18,]),'string':([10,],[15,]),'is':([10,14,15,16,17,18,19,],[16,23,24,25,26,27,28,]),'in':([11,],[20,]),'to':([12,],[21,]),'stop':([13,45,46,47,48,49,50,51,52,],[22,53,54,55,56,57,58,59,60,]),'comma':([29,30,31,32,33,34,35,36,],[37,38,39,40,41,42,43,44,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'evaluate':([0,],[1,]),'exp_assign':([0,],[2,]),'exp_move':([0,],[3,]),'exp_naming':([0,],[4,]),'exp_value':([0,],[5,]),'no_stop':([0,],[6,]),'empty':([0,],[7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> evaluate","S'",1,None,None,None),
  ('evaluate -> exp_assign','evaluate',1,'p_evaluate','parser.py',9),
  ('evaluate -> exp_move','evaluate',1,'p_evaluate','parser.py',10),
  ('evaluate -> exp_naming','evaluate',1,'p_evaluate','parser.py',11),
  ('evaluate -> exp_value','evaluate',1,'p_evaluate','parser.py',12),
  ('evaluate -> no_stop','evaluate',1,'p_evaluate','parser.py',13),
  ('evaluate -> empty','evaluate',1,'p_evaluate','parser.py',14),
  ('exp_assign -> assignment integer to integer comma integer stop','exp_assign',7,'p_exp_assign','parser.py',19),
  ('exp_move -> operation move stop','exp_move',3,'p_exp_move','parser.py',26),
  ('exp_naming -> var string is integer comma integer stop','exp_naming',7,'p_exp_naming','parser.py',33),
  ('exp_naming -> var operation is integer comma integer stop','exp_naming',7,'p_exp_naming','parser.py',34),
  ('exp_naming -> var move is integer comma integer stop','exp_naming',7,'p_exp_naming','parser.py',35),
  ('exp_naming -> var var is integer comma integer stop','exp_naming',7,'p_exp_naming','parser.py',36),
  ('exp_naming -> var is is integer comma integer stop','exp_naming',7,'p_exp_naming','parser.py',37),
  ('exp_naming -> var assignment is integer comma integer stop','exp_naming',7,'p_exp_naming','parser.py',38),
  ('exp_value -> value in integer comma integer stop','exp_value',6,'p_exp_value','parser.py',44),
  ('no_stop -> operation move','no_stop',2,'p_fullStop','parser.py',51),
  ('no_stop -> assignment integer to integer comma integer','no_stop',6,'p_fullStop','parser.py',52),
  ('no_stop -> var string is integer comma integer','no_stop',6,'p_fullStop','parser.py',53),
  ('no_stop -> value in integer comma integer','no_stop',5,'p_fullStop','parser.py',54),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',61),
]
