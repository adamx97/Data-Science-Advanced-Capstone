import model_evaluation_utils as meu
import pickle
import matplotlib.pyplot as plt
import statistics


gh = None

def GetFromPickle (filename):
    with open(filename, 'rb') as f:
        d =  pickle.load(f)
    return d

def GetEpochAverages(metric):
    epochavg = {}
    epochs = len(metric[0])
    for r in range(0, epochs):
        epoch_mean = statistics.mean([i[r] for i in metric])
        epochavg["Epoch_" +str(r)] = epoch_mean
    return epochavg, list(epochavg.values())

#history = GetFromPickle("deeplearningWithGlove300.history")
#history = GetFromPickle("deeplearningWithGlove300-20200922-1658.history")
#history = GetFromPickle("deeplearningWithGlove300-20200922-1745.history")
#history = GetFromPickle("deeplearningWithGlove300-20200922-1759.history")
#history = GetFromPickle("deeplearningWithGlove300-20200923-1258.history")
#history = GetFromPickle("deeplearningWithGlove300_TrainTestSplit_-20200923-1409.history")
history = GetFromPickle("deeplearningWithGlove300_TrainTestSplit_-20200923-1416.history")

#print (history)

loss_all =  [i['loss'] for i in history]
val_loss_all = [i['val_loss'] for i in history]
acc_all = [i['accuracy'] for i in history]
val_acc_all =  [i['val_accuracy'] for i in history]

d, avg_loss = GetEpochAverages(loss_all)
d, avg_val_loss = GetEpochAverages(val_loss_all)
d, avg_acc = GetEpochAverages(acc_all)
d, avg_val_acc = GetEpochAverages(val_acc_all)

print ("Accuracy: {}".format(GetEpochAverages(acc_all)))
print ("Validation Accuracy: {}".format(GetEpochAverages(val_acc_all)))
print ("Loss: {}".format(GetEpochAverages(loss_all)))
print ("Validation Loss: {}".format(GetEpochAverages(val_loss_all)))



colors = 'bgrcmyk'

plt.figure(1)
plt.subplot(121) #rows/cols/index
epochs = range(1, len(history[0]['accuracy']) + 1)

plt.plot(epochs, avg_val_loss, 'k', marker='s', markersize=10, linestyle=':', label='Validation loss --Averaged')
plt.plot(epochs, avg_loss, 'k', marker='x', markersize=14, linestyle=':', label='Training loss --Averaged')
for i,fold in enumerate(history):
    history_dict = fold
    color = colors[i]

    acc = history_dict['accuracy']
    val_acc = history_dict['val_accuracy']
    loss = history_dict['loss']
    val_loss = history_dict['val_loss']

    epochs = range(1, len(acc) + 1)

    # "bo" is for "blue dot"
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    
    plt.plot(epochs, loss, color +'o', marker='+', linestyle=':', label='Training loss (fold %s)' % i)
    # b is for "solid blue line"
    plt.plot(epochs, val_loss, color, marker='D', linestyle=':',label='Validation loss (fold %s)' % i)
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    

#plt.show()
plt.subplot(122)
plt.plot(epochs, avg_val_acc, 'k', marker='s', markersize=10, linestyle=':', label='Validation Accuracy-Averaged')
plt.plot(epochs, avg_acc, 'k', marker='x', markersize=14, linestyle=':', label='Training Accuracy-Averaged')
for i,fold in enumerate(history):
    history_dict = fold
    color = colors[i]

    acc = history_dict['accuracy']
    val_acc = history_dict['val_accuracy']

    
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    # "bo" is for "blue dot"
    plt.plot(epochs, acc, color, marker='+', linestyle=':', label='Training accuracy (fold %s)' % i)
    # b is for "solid blue line"
    plt.plot(epochs, val_acc, color, marker = 'D',linestyle=':', label='Validation accuracy (fold %s)' % i)
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

plt.show()




#print (epochacc)
    # acc = history_dict['accuracy']
    # val_acc = history_dict['val_accuracy']
    # loss = history_dict['loss']
    # val_loss = history_dict['val_loss']

