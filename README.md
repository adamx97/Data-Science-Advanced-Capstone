# Data-Science-Advanced-Capstone

Teacher's github repo for this class:
https://github.com/IBM/skillsnetwork/tree/master/coursera_capstone

Some docs:
* https://developer.ibm.com/articles/the-lightweight-ibm-cloud-garage-method-for-data-science/
* https://developer.ibm.com/articles/data-science-architectural-decisions-guidelines/


Real and Fake news Dataset:
https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset?select=True.csv

Excellent academic paper on previous work in this area:
Automatic Detection of Fake News Veronica Perez-Rosas 1, Bennett Kleinberg 2, Alexandra Lefevre 1 Rada Mihalcea 11 
Computer Science and Engineering, University of Michigan
Department of Psychology, University of Amsterdam vrncapr@umich.edu, b.a.r.kleinberg@uva.nl, mihalcea@umich.edu
Abstract 
The proliferation of misleading information in everyday access media outlets such as social media feeds, news blogs, and online newspapers have made it challenging to identify trustworthynews sources, thus increasing the need for computational tools able to provide insights into thereliability of online content.  In this paper, we focus on the automatic identification of fake con-tent in online news.  Our contribution is twofold.  First, we introduce two novel datasets for thetask of fake news detection, covering seven different news domains. We describe the collection,annotation, and validation process in detail and present several exploratory analyses on the iden-tification of linguistic differences in fake and legitimate news content.  Second, we conduct aset of learning experiments to build accurate fake news detectors, and show that we can achieveaccuracies of up to 76%.   In addition,  we provide comparative analyses of the automatic andmanual identification of fake news.
https://www.aclweb.org/anthology/C18-1287.pdf

Description of Claim Review, a factchecking centralized datafeed from a number of factchecking organizations:
https://www.storybench.org/how-claimreview-is-simplifying-the-process-of-fact-checking/

Video on using Keras to use sentiment analysis on IMDB reviews:
https://www.coursera.org/learn/ai/lecture/hQYsN/recurrent-neural-networks
 
Other  articles on classifying real/fake news:
https://opendatascience.com/how-to-build-a-fake-news-classification-model/

https://www.kaggle.com/anthonyc1/fake-news-classifier-final-project

FakeNewsNet scripts and description:
https://github.com/KaiDMML/FakeNewsNet
FakeNewsNet article using data above: 
http://sbp-brims.org/2018/proceedings/papers/challenge_papers/SBP-BRiMS_2018_paper_120.pdf

A paper: “Liar, Liar Pants on Fire”:A New Benchmark Dataset for Fake News Detection
“Liar, Liar Pants on Fire”:A New Benchmark Dataset for Fake News Detection William Yang Wang Department of Computer Science University of California, Santa BarbaraSanta Barbara, CA 93106 USAwilliam@cs.ucsb.edu

Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Short Papers), pages 422–426Vancouver, Canada, July 30 - August 4, 2017.c©2017 Association for Computational Linguisticshttps://doi.org/10.18653/v1/P17-2067Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Short Papers), pages 422–426Vancouver, Canada, July 30 - August 4, 2017.c©2017 Association for Computational Linguisticshttps://doi.org/10.18653/v1/P17-2067

https://www.aclweb.org/anthology/P17-2067.pdf

Another paper using the same dataset:
https://www.aclweb.org/anthology/W18-5513/


The Data Challenge in Misinformation Detection:Source Reputation vs. Content Veracity
Big Data and quality data for fake news and misinformation detection 
 https://www.aclweb.org/anthology/W18-5502.pdf

Contains a good discussion of the varieties of fake news and various modes of news bias through history.
https://journals.sagepub.com/doi/full/10.1177/2053951719843310
A paper discussing below datasets: 
Misinfo dataset: https://github.com/sfu-discourse-lab/MisInfoText 
https://github.com/sfu-discourse-lab/Misinformation_detection

Asr FT, Taboada M (2019) | 1,380 news articles | 4-way (false, true, mixture, no factual content) | Collected using a pivot Buzzfeed dataset. 
Focused on the US election topic. https://github.com/sfu-discourse-lab/Misinformation_detection/blob/master/buzzfeed-v02-originalLabels.txt.zip
These stories have been scraped from the web, but are skewed towards true stories (The 1380 stories are labelled as follows: Mixed: 170, Mostly False: 64, Mostly True: 1090, No factual content: 56).  These stories also seem to be poor training material as they have been adulterated by the scraping process that seemed to merge words together, especially words with apostrophes (ex: "I hope youdon mind my asking, butI curious" was recorded, rather than "I hope you don't mind my asking, but I'm curious.") This doesn't seem to be a suitable dataset. 


Asr FT, Taboada M (2019) | 33 news articles | 4-way (false, true, mixture, no factual content) | Collected using a pivot Buzzfeed dataset. 
A variety of topics. https://github.com/sfu-discourse-lab/Misinformation_detection/blob/master/buzzfeed-top.csv.zip
This selection from the top 50 Buzzfeed false stories has 34 stories, all are false, and contains story text that does not suffer from the adulteration described above.  

Asr FT, Taboada M (2019) | 312 news articles | 5-way (false to true) | Collected from Snopes. Balanced by label. A variety of topics. Includes stance information (articles for or against a labeled claim). https://github.com/sfu-discourse-lab/Misinformation_detection/blob/master/snopes_checked_v02.csv.zip
This is a collection of stories, as labelled by Snopes.com, with  full text that has not been adulterated by the scraping process.  The counts are: Mixed: 72, Mostly False: 53, False: 51, Mostly True: 72, True 65.

* Using a Relu activation function:
Probably start with it by default and explore from there:
https://machinelearningmastery.com/rectified-linear-activation-function-for-deep-learning-neural-networks/

* A Simple Way to Initialize Recurrent Networks of Rectified Linear Units (LSTM is a kind of RNN)
https://arxiv.org/abs/1504.00941

* Article on how to fix vanishing gradients problem:

our initial models may suffer from this:
"The vanishing gradients problem may be manifest in a Multilayer Perceptron by a slow rate of improvement of a model during training and perhaps premature convergence, e.g. continued training does not result in any further improvement. Inspecting the changes to the weights during training, we would see more change (i.e. more learning) occurring in the layers closer to the output layer and less change occurring in the layers close to the input layer."

https://machinelearningmastery.com/how-to-fix-vanishing-gradients-using-the-rectified-linear-activation-function/








