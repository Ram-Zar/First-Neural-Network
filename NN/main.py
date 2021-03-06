import matplotlib.pyplot as plt
import NN
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def Training():
    #training data
    data_file=open("C:/Users/Hp/Desktop/my python programs/mnist_train.csv",'r')
    data_list=data_file.readlines()
    data_file.close()
    #modification fo training data
    i=0
    for line in data_list:
        i+=1
        if (i==1000):
           print("1000 times done")
        elif (i==10000):
           print("10000 times done")
        elif (i==20000):
            print("20000 times done")
        elif (i==30000):
            print("30000 times done")
        elif (i==40000):
            print("40000 times done")
        elif (i==50000):
            print("50000 times done")        
        all_val_train=line.split(',')
        inputs=np.asfarray(all_val_train[1:])
        inputs=inputs/255.0*0.99+0.01
        targets=np.zeros(out_nodes)+0.01
        targets[int(all_val_train[0])]=0.99
        n.train(inputs,targets)
        pass
    np.savez_compressed("Data",n.ih,n.ho)
    pass
def Query(Flag):
    scorecard=[]
    data_file=open("C:/Users/Hp/Desktop/my python programs/mnist_test.csv",'r')
    data_list=data_file.readlines()
    data_file.close()
    #modification fo training data
    for line in data_list:
        all_val_ask=line.split(',')
        inputs=np.asfarray(all_val_ask[1:])
        correct=all_val_ask[0]
        # print("correct: ",correct)
        inputs=inputs/255.0*0.99+0.01
        output=n.query(inputs)
        netanswer=np.argmax(output)
        #print("net answer: ",netanswer)
        if (int(correct)==netanswer):
            scorecard.append(1)
        else:
            scorecard.append(0)
            pass
    i=0
    sum=0
    for record in scorecard:
        i+=1
        sum+=record
        pass
    rate=sum/float(i)*100
    if (Flag=="S"):
        return rate
    else:
        print("correctness: %.3f" % (rate),"%")

#def Rec_file(A,B,C):
   # np.savez("SData",A=A,B=B,C=C)
   # pass

def Statistic():
    score_lr=[]
    score_hnodes=[]
    score_eff=[]
    data_file=open("C:/Users/Hp/Desktop/my python programs/mnist_train.csv",'r')
    data_list=data_file.readlines()
    data_file.close()
    learn_rate=0.1
    for l_r in range(5):
        learn_rate+=0.1
        n.Set_learn_rate(learn_rate)
        score_lr.append(learn_rate) 
        for h_nodes in range(100,600,100):
            n.Set_hnodes(h_nodes)
            score_hnodes.append(h_nodes)
            i=0
            for line in data_list:
                i+=1
                if (i==1000):
                   print("1000 times done")
                elif (i==10000):
                   print("10000 times done")
                elif (i==20000):
                    print("20000 times done")
                elif (i==30000):
                    print("30000 times done\a")
                elif (i==40000):
                    print("40000 times done")
                elif (i==50000):
                    print("50000 times done")
                elif (i==60000):
                    print("\a")
                #modification fo training data      
                all_val_train=line.split(',')
                inputs=np.asfarray(all_val_train[1:])
                inputs=inputs/255.0*0.99+0.01
                targets=np.zeros(out_nodes)+0.01
                targets[int(all_val_train[0])]=0.99
                n.train(inputs,targets)
                pass
            rate=Query("S")
            score_eff.append(rate)
            pass
        pass
    ARR_LR=np.array(score_lr)
    ARR_H=np.array(score_hnodes)
    ARR_EF=np.array(score_eff)
    np.savez("SData",ARR_LR=ARR_LR,ARR_H=ARR_H,ARR_EF=ARR_EF)

def Statistic_view():
    s=150
    data=np.load("C:/Users/Hp/Desktop/my python programs/NN/NN/SData.npz")
    size1=data['ARR_H'].size
    size2=data['ARR_LR'].size
    LR_LIST=[]
    for i in range(size2):
        for j in range(size2):
            LR_LIST.append(data['ARR_LR'][i])
            pass
        pass
    X=np.array(LR_LIST).reshape(1,size1)
    print("LR:",data['ARR_LR'])
    Y=data['ARR_H']
    Z=data['ARR_EF']
    print("HN:\n",data['ARR_H'])
    print("EFF:\n",data['ARR_EF'])
    hf=plt.figure()
    ha=hf.add_subplot(111,projection='3d')
    ha.scatter(X,Y,Z,s=s,label="Statistic")
    plt.show()
def EpochTrain(epoch):
    for i in range(int(epoch)):
        print("Epoch ",i+1,":")
        Training()
        print("Epoch result: ")
        Query("None")
        pass
#main unformation
in_nodes=784
h_nodes=200
out_nodes=10
learn_rate=0.2
#NN object
n=NN.NN()
n._init_(in_nodes,h_nodes,out_nodes,learn_rate)
print("NN is ready to work\nFor exit press ENTER\ninput>>")
order=input()
while (order!=""):
    if (order=="training"):
        Training()
        print("Done.")
    elif (order=="query"):
       Query("None")
       print("Done.")
    elif (order=="statistic"):
        Statistic()
        Statistic_view()
    elif (order=="SView"):
        Statistic_view()
    elif (order=="EpochTrain"):
        print("\nEnter epoch:")
        epoch=input()
        EpochTrain(epoch)
    else:
        print("wrong input.Repeat")
    print("\ninput>>")
    order=input()
    pass

   

   



