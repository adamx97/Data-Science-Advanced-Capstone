import matplotlib.pyplot as plt

def ChartModelHistory(fithistory, longdim=15, shortdim=10, horizontal=True):
    history_dict = fithistory.history
    history_dict.keys()
    if horizontal: 
        plt.figure(1, figsize=(longdim, shortdim))
        plt.subplot(121)
    else: 
        plt.figure(1, figsize=(shortdim,longdim))
        plt.subplot(211)


    acc = history_dict['accuracy']
    val_acc = history_dict['val_accuracy']
    loss = history_dict['loss']
    val_loss = history_dict['val_loss']

    epochs = range(1, len(acc) + 1)

    # "bo" is for "blue dot"
    plt.plot(epochs, loss, 'bo', label='Training loss')
    # b is for "solid blue line"
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    # zip joins x and y coordinates in pairs
    for x,y in zip(epochs,val_loss):

        label = "{:.2f}".format(y)

        plt.annotate(label, # this is the text
                    (x,y), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center
    plt.legend()

    if horizontal:
        plt.subplot(122)
    else:
        plt.subplot(212)
    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    for x,y in zip(epochs,val_acc):

        label = "{:.2f}".format(y)

        plt.annotate(label, # this is the text
                    (x,y), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.legend()

    plt.show()