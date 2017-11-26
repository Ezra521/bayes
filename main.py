data = [
        [1, 1, 'yes'],
        [1, 0, 'no' ],
        [0, 1, 'no' ],
        [0, 0, 'no' ],
        [2, 2, 'tt']
        ]#初始的数据集
la = ['no surfacing', 'flippes']


# 计算条件概率
def ConProb(DataSet, Feature):
    tarVar = {}  # 统计各个类的数量
    featureCount = {}  # 每个特征值在每个类中出现的数量
    retProb = {}
    tarList = []  # 目标属性集合
    featurList = []  # feature的列表

    for row in DataSet:
        tarVar[row[-1]] = tarVar.setdefault(row[-1], 0) + 1#该循环判断该字典的出现的次数

        flag = tuple([row[-1], row[Feature]])
        featureCount[flag] = featureCount.setdefault(flag, 0) + 1
        tarList.append(row[-1])  #
        featurList.append(row[Feature])
    tarList = list(set(tarList))
    featurList = list(set(featurList))

    for k in tarList:
        retProb[k] = {}

        for v in featurList:
            flag_temp = tuple([k, v])
            temp = tarVar[k] + len(featurList)  # 此处避免0概率的发生加上了属性值的个数
            if flag_temp in featureCount.keys():
                retProb[k][v] = (featureCount[flag_temp] + 1) / temp
            else:
                retProb[k][v] = 1 / temp

    return (retProb)


# 返回每个属性中的值在每个类中出现的概率
def TrainNB(DataSet, label):
    SampleNum = len(DataSet)#得到所有情况的总数
    classProb = {}
    classCount = {}#存放yes和no的数量。输出的字典
    for row in DataSet:
        classCount[row[-1]] = classCount.setdefault(row[-1], 0) + 1#这个循环完成了yes和no的数据字典的构建
        #print(classCount)
    for k in classCount.keys():
        classProb[k] = classCount[k] / SampleNum  # 每个类出现的概率

    ProbSample = {}
    for la in label:
        adrr = label.index(la)
        ProbSample[la] = ConProb(DataSet, adrr)
    return (ProbSample, classProb)


##classfy
def classify(ProbSample, classProb, testData, testLabel):
    maxConP = 0.0
    reClass = ''
    for k in classProb.keys():
        conP = 1.0
        # print(k)
        for la in testLabel:
            flag = testLabel.index(la)
            # print(la)
            conP = conP * ProbSample[la][k][testData[flag]]

        conP = conP * classProb[k]
        if (maxConP < conP):
            maxConP = conP
            reClass = k
    return (reClass)


test, p = TrainNB(data, la) #返回的是一个元组

#print(test,p)
# print(test)
# print(p)
testNum = input("请输入测试样本用逗号隔开:")
testData = []
for i in testNum.split(','):
    testData.append(int(i))

#result = classify(test, p, [1, 1], la)
result = classify(test, p, testData, la)
print("testResult:", result)