# modified from https://github.com/Eligijus112/twitter-genuine-tweets/blob/master/master.py

import tensorflow
import pandas as pd 
import numpy as np 
import os
from datetime import date
from datetime import datetime
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn import model_selection
# Import the main analysis pipeline
from pipeline import Pipeline
# Tensor creation class
from text_preprocessing import TextToTensor
# Reading the configuration file
import yaml
with open("conf.yml", 'r') as file:
    conf = yaml.safe_load(file).get('pipeline')

# Reading the stop words
stop_words = []
# try:
#     stop_words = pd.read_csv('data/stop_words.txt', sep='\n', header=None)[0].tolist()
# except Exception as e:
#     # This exception indicates that the file is missing or is in a bad format
#     print('Bad stop_words.txt file: {e}')

# Reading the data

#train = pd.read_csv('data/train.csv')[['text', 'target']]
#test = pd.read_csv('data/test.csv')
dfNewsTemp = pd.read_pickle('dfTrueFalseNews.pkl')
timestamp = datetime.now().strftime("%Y%m%d-%H%M")

def KfoldSplit(dataframe):
    train = dataframe.sample(frac=1)

    # Creating the input for the pipeline
    X_train = train['text'].tolist()
    Y_train = train['truthvalue'].tolist()
    X_test = train['text'].tolist()
    Y_test = train['truthvalue'].tolist()

    fit_history = []
    if conf.get('k_fold'):
        skfold = StratifiedKFold(n_splits=4, shuffle=True, random_state=42)
        acc = []
        f1 = []
        summarize= True
        for train_index, test_index in skfold.split(X_train, Y_train):
            # Fitting the model and forecasting with a subset of data
            k_results = Pipeline(
                X_train=np.array(X_train)[train_index],
                Y_train=np.array(Y_train)[train_index], 
                embed_path='glove.6B.300d.txt',
                embed_dim=300,
                X_test=np.array(X_train)[test_index],
                Y_test=np.array(Y_train)[test_index],
                max_len=conf.get('max_len'),
                epochs=conf.get('epochs'),
                batch_size=conf.get('batch_size')
            )
            if summarize:
                k_results.model.summary()
                summarize=False
            # Saving the accuracy
            acc += [k_results.acc]
            f1 += [k_results.f1]
            fit_history.append(k_results.fit_history.history)
            print(f'The accuracy score is: {acc[-1]}') 
            print(f'The f1 score is: {f1[-1]}') 
        print(f'Total mean accuracy is: {np.mean(acc)}')
        print(f'Total mean f1 score is: {np.mean(f1)}')
    return fit_history, k_results

def TrainTestSplit(dataframe):
    train = dataframe.sample(frac=1)
    fit_history = []
    # Creating the input for the pipeline
    X_train = train['text'].tolist()
    Y_train = train['truthvalue'].tolist()
    X_test = train['text'].tolist()
    Y_test = train['truthvalue'].tolist()

    acc = []
    f1 = []
    summarize= True
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(train['text'], train['truthvalue'],
        test_size=0.1, random_state=42, stratify=train['truthvalue'])
    
    # Fitting the model and forecasting with a subset of data
    k_results = Pipeline(
        X_train=X_train.to_list(), # np.array(X_train)[train_index],
        Y_train=Y_train.to_list(), # np.array(Y_train)[train_index], 
        embed_path='glove.6B.300d.txt',
        embed_dim=300,
        X_test= X_test.to_list(), 
        Y_test= Y_test.to_list(), 
        max_len=conf.get('max_len'),
        epochs= 20, #conf.get('epochs'),
        batch_size=conf.get('batch_size')
    )
    if summarize:
        k_results.model.summary()
        summarize=False
    # Saving the accuracy
    acc += [k_results.acc]
    f1 += [k_results.f1]
    fit_history.append(k_results.fit_history.history)
    print(f'The accuracy score is: {acc[-1]}') 
    print(f'The f1 score is: {f1[-1]}') 
    print(f'Total mean accuracy is: {np.mean(acc)}')
    print(f'Total mean f1 score is: {np.mean(f1)}')
    return fit_history, k_results    

splitfunc = TrainTestSplit # KfoldSplit  # or TrainTestSplit
fit_history, k_results = splitfunc(dfNewsTemp)

import pickle
filename = "deeplearningWithGlove300_{}_{}.history".format(splitfunc.__name__, timestamp)
with open(filename, 'wb') as f:
    pickle.dump(fit_history, f)
print ("Wrote ", filename )

if conf.get('save_model'):
    mfilename = "deeplearningWithGlove300_{}_{}.model".format(splitfunc.__name__, timestamp)
    k_results.model.save(mfilename)
    print ("Wrote ", mfilename )


# Running the pipeline with all the data
# results = Pipeline(
#     X_train=X_train,
#     Y_train= Y_train, 
#     embed_path='glove.6B.300d.txt',
#     embed_dim=300,
#     #stop_words=stop_words,
#     X_test=X_test,
#     Y_test=Y_test,
#     max_len=conf.get('max_len'),
#     epochs=conf.get('epochs'),
#     batch_size=conf.get('batch_size')
# )
#results.model.summary()
#fit_history.append(results.fit_history.history)



# Some sanity checks
# good = ["Fire in Vilnius! Where is the fire brigade??? #emergency"]
# bad = ["Sushi or pizza? Life is hard :(("]

# TextToTensor_instance = TextToTensor(
# tokenizer=results.tokenizer,
# max_len=conf.get('max_len')
# )

# # Converting to tensors
# good_nn = TextToTensor_instance.string_to_tensor(good)
# bad_nn = TextToTensor_instance.string_to_tensor(bad)

# # Forecasting
# p_good = results.model.predict(good_nn)[0][0]
# p_bad = results.model.predict(bad_nn)[0][0]

# print(f'Sentence: {good_nn} Score: {p_good}')
# print(f'Sentence: {bad_nn} Score: {p_bad}')

# # Saving the predictions
# test['prob_is_genuine'] = results.yhat
# test['target'] = [1 if x > 0.5 else 0 for x in results.yhat]
 
# # Saving the predictions to a csv file
# if conf.get('save_results'):
#     if not os.path.isdir('output'):
#         os.mkdir('output')    
#     test[['id', 'target']].to_csv(f'output/submission_{date.today()}.csv', index=False)

