from node import Node
import math

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''




def prune(node, examples):
  '''
  Takes in a trained tree and a validation set of examples.  Prunes nodes in order
  to improve accuracy on the validation data; the precise pruning strategy is up to you.
  '''

def test(node, examples):
  '''
  Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
  of examples the tree classifies correctly).
  '''


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''

def CHOOSE_ATTRIBUTE(example):
  dict = {}
  num = len(example)
  for data in example:
    if data['Class'] not in dict:
      dict[data['Class']] = 1
    else:
      dict[data['Class']] += 1
  Shannon = 0
  for eachClass in dict:
    P = dict[eachClass] / num
    Shannon += - P * math.log(P,2)

def shannon_value(example):
  Best = 1
  best_attr = None
  for feature in example[0]:
    if feature == 'Class':
      continue
    value = []
    for data in example:
      if data[feature] not in value:
        value.append(data[feature])
    info = 0
    n = 0
    for v in value:
      print(feature+"="+ str(v)+":")
      dict = {}
      for data in example:
        if data[feature] == v:
          if data['Class'] not in dict:
            dict[data['Class']] = 1
          else:
            dict[data['Class']] += 1
      shannon, num = calculate(dict)
      print(shannon)
      info += shannon * num
      n += num
    info = info / n
    print("When feature = "+ feature+" ,info = "+str(info))
    if info < Best:
      Best = info
      best_attr = feature
  return best_attr


def calculate(dict):
    value = dict.values()
    num = sum(value)
    S = 0
    for eachClass in dict:
      P = float( dict[eachClass]) / num
      S += - P * math.log(P,2)
    return S,num