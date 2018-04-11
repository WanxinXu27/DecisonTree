from node import Node
import math

def ID3(examples, default):
  '''
  Takes in an array of examples, and returns a tree (an instance of Node) 
  trained on the examples.  Each example is a dictionary of attribute:value pairs,
  and the target class variable is a special attribute with the name "Class".
  Any missing attributes are denoted with a value of "?"
  '''
  if len(examples) == 0:
    return None
  AllClass = [element['Class'] for element in examples]
  dict = {}
  for i in AllClass:
    if i not in dict:
      dict[i] = 1
    else:
      dict[i] += 1
  if len(dict) == 1:
    [k] = dict.keys()
    return k
  if len(examples[0]) == 1:
    return majority(examples)
  best = CHOOSE_ATTRIBUTE(examples)
  value = count([element[best] for element in examples])
  root = Node()
  root.label = best
  for v in value:
    examples_v = split(examples,best,v)
    root.children[v] = ID3(examples_v,0)
  return root




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
  if a not in Node()





def CHOOSE_ATTRIBUTE(example):
  H_prior = {}
  for element in example:
    if element['Class'] not in H_prior:
      H_prior[element['Class']] = 1
    else:
      H_prior[element['Class']] += 1
  Best,num_class = calculate(H_prior)
  print("info of H_prior = " + str(Best))
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

def count(data):
  dict = {}
  for i in data:
    if i not in dict:
      dict[i] = 1
    else:
      dict[i] += 1
  return dict.keys()

def split(examples,attribute,value):
  res = []
  for element in examples:
    if element[attribute] == value:
      dict = {}
      for keys in element:
        if keys == attribute:
          continue
        dict[keys] = element[keys]
      res.append(dict)
  return res

def majority(examples):
  l = [element['Class'] for element in examples]
  dict = {}
  for i in l:
    if i not in dict:
      dict[i] = 1
    else:
      dict[i] += 1
  count = 0
  maj = None
  for keys in dict:
    if dict[keys] > count:
      count = dict[keys]
      maj = keys
  return maj