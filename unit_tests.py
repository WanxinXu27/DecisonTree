import ID3, parse, random
import numpy as np
import matplotlib.pyplot as plt


def testID3AndEvaluate():
  data = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1)]
  tree = ID3.ID3(data, 0)
  if tree != None:
    ans = ID3.evaluate(tree, dict(a=1, b=0))
    if ans != 1:
      print "ID3 test failed."
    else:
      print "ID3 test succeeded."
  else:
    print "ID3 test failed -- no tree returned"

def testPruning():
  data = [dict(a=1, b=1, c=1, Class=0), dict(a=1, b=0, c=0, Class=0), dict(a=0, b=1, c=0, Class=1), dict(a=0, b=0, c=0, Class=1), dict(a=0, b=0, c=1, Class=0)]
  validationData = [dict(a=0, b=0, c=1, Class=1)]
  tree = ID3.ID3(data, 0)
  print "treesize is",ID3.treeSize(tree)
  ID3.prune(tree, validationData)
  if tree != None:
    ans = ID3.evaluate(tree, dict(a=0, b=1, c=1))
    if ans != 1:
      print "pruning test failed."
    else:
      print "pruning test succeeded."
  else:
    print "pruning test failed -- no tree returned."


def testID3AndTest():
  trainData = [dict(a=1, b=0, c=0, Class=1), dict(a=1, b=1, c=0, Class=1), 
  dict(a=0, b=0, c=0, Class=0), dict(a=0, b=1, c=0, Class=1)]
  testData = [dict(a=1, b=0, c=1, Class=1), dict(a=1, b=1, c=1, Class=1), 
  dict(a=0, b=0, c=1, Class=0), dict(a=0, b=1, c=1, Class=0)]
  tree = ID3.ID3(trainData, 0)
  fails = 0
  if tree != None:
    acc = ID3.test(tree, trainData)
    if acc == 1.0:
      print "testing on train data succeeded."
    else:
      print "testing on train data failed."
      fails = fails + 1
    acc = ID3.test(tree, testData)
    if acc == 0.75:
      print "testing on test data succeeded."
    else:
      print "testing on test data failed."
      fails = fails + 1
    if fails > 0:
      print "Failures: ", fails
    else:
      print "testID3AndTest succeeded."
  else:
    print "testID3andTest failed -- no tree returned."

# inFile - string location of the house data file
def testPruningOnHouseData(inFile):
  withPruning = []
  withoutPruning = []
  data = parse.parse(inFile)
  for i in range(100):
    random.shuffle(data)
    train = data[:len(data)/2]
    valid = data[len(data)/2:3*len(data)/4]
    test = data[3*len(data)/4:]
  
    tree = ID3.ID3(train, 'democrat')
    acc = ID3.test(tree, train)
    print "training accuracy: ",acc
    acc = ID3.test(tree, valid)
    print "validation accuracy: ",acc
    acc = ID3.test(tree, test)
    print "test accuracy: ",acc
  
    ID3.prune(tree, valid)
    acc = ID3.test(tree, train)
    print "pruned tree train accuracy: ",acc
    acc = ID3.test(tree, valid)
    print "pruned tree validation accuracy: ",acc
    acc = ID3.test(tree, test)
    print "pruned tree test accuracy: ",acc
    withPruning.append(acc)
    tree = ID3.ID3(train+valid, 'democrat')
    acc = ID3.test(tree, test)
    print "no pruning test accuracy: ",acc
    withoutPruning.append(acc)
  print withPruning
  print withoutPruning
  print "average with pruning",sum(withPruning)/len(withPruning)," without: ",sum(withoutPruning)/len(withoutPruning)


def plotHouseVoting(inFile):
  accuracy_on_test_without_prune = []
  accuracy_on_test_with_prune = []
  data = parse.parse(inFile)
  for size in range(10,301):
    withPruning = []
    withoutPruning = []
    for i in range(100):
      random.shuffle(data)
      train = data[:size * 7 / 10]
      valid = data[size * 7 / 10: size]
      test = data[size:]
      tree = ID3.ID3(train + valid, 'democrat')
      acc = ID3.test(tree, test)
      withoutPruning.append(acc)
      tree = ID3.ID3(train, 'democrat')
      ID3.prune(tree, valid)
      acc = ID3.test(tree, test)
      withPruning.append(acc)
    print "training size: ", size
    accuracy_on_test_without_prune.append(sum(withoutPruning)/len(withoutPruning))
    print "accuracy on unpruned tree: ", sum(withoutPruning)/len(withoutPruning)
    accuracy_on_test_with_prune.append(sum(withPruning)/len(withPruning))
    print "accuracy on pruned tree: ", sum(withPruning)/len(withPruning)
  x = np.arange(10,301,1)
  plt.plot(x,accuracy_on_test_without_prune)
  plt.plot(x,accuracy_on_test_with_prune)
  plt.show()


if __name__ == "__main__":
  # testID3AndEvaluate()
  # testID3AndTest()
  # testPruningOnHouseData("house_votes_84.data")
  plotHouseVoting("house_votes_84.data")
