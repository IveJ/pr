"""
AUTO ML for finance example.



"""

pip install requests
pip install tabulate
pip install "colorama>=0.3.8"
pip install futurepip install -f "); background-size: 1px 1px; background-position: 0px calc(1em + 1px);">http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py. h2o



"""
If you are already having anaconda installed you could directly proceed with the conda command;
"""


conda install -c h2oai h2o=3.20.0.1


"""
Note: When installing H2O from pip in OS X El Capitan, users must include the --user flag. For example -

pip install -f "); background-size: 1px 1px; background-position: 0px calc(1em + 1px);">http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o --user

For R and Hadoop installation please refer to the official documentation "); background-size: 1px 1px; background-position: 0px calc(1em + 1px);">here.

Getting Started

Start the H2O.ai instance by importing h2o.ai and H2OAutoML instance.
"""


import h2o
from h2o.automl import H2OAutoML
h2o.init()


"""
If the setup was successful then will see the following cluster information.

In this example, we are going to use a dataset from DataHack Practice problem "); background-size: 1px 1px; background-position: 0px calc(1em + 1px);">Loan Prediction III

The goal here is to predict whether or not a loan will be paid by the customer wherein we are provided with details like — Gender, Marital Status, Education, and others.

First, let’s import the training set and check out .head() and the datatypes of the data frame.
"""



df = h2o.import_file('train_u6lujuX_CVtuZ9i.csv')
df.head()

.head() method frame


"""
Let’s check the datatypes with .describe() method.

As you can see in this example, the datatype of our target variable — Loan_Status is enum type. If it's referred as int type, then you must change the data type to enum using the following command :
"""


df[target] = df[target].asfactor()


"""
Note: Failing to do so makes AutoML think this is a regression problem which comes at a great cost if you are running models for 10+ hours.

So, gotta be careful there. I wonder whether H2O.ai developers can convert this automatically in backend if the target y has nunique==2 .

Now we have to separate the features and target variables. AutoML functions take features and the target in x and yvariables.
"""


y = "Loan_Status"
x = ['Gender','Married','Education','ApplicantIncome',
'LoanAmount','CoapplicantIncome','Loan_Amount_Term',
'Credit_History','Property_Area']


aml = H2OAutoML(max_models = 30, max_runtime_secs=300, seed = 1)
aml.train(x = x, y = y, training_frame = df)


"""
You can then configure values for max_runtime_secs and/or max_models to set explicit time or number-of-model limits on your run. The model will train on the parameters provided. For this tutorial, we are training the models with few features and for about 2 mins.

Once the model is trained, you can access the Leaderboard. The leader model is stored at aml.leader and the leaderboard is stored at aml.leaderboard The leaderboard stores the snapshot of the top models. The top models are usually the stacked ensembles as they can easily outperform a single trained model. To view the entire leaderboard, specify the rowsargument of the head() method as the total number of rows:
"""


lb = aml.leaderboard
lb.head()
lb.head(rows=lb.nrows) # Entire leaderboard

"""
The best model scored 0.77431 AUC. That’s a great score given that we have not done preprocessing or model tuning of any sort!

Prediction and Saving the model

You could use the best leader model to make prediction. This can be done by using the following command:

preds = aml.predict(test)

The next step would be to save the trained model. There are two ways to save the leader model — binary format and MOJO format. If you’re taking your leader model to production, then it is suggested to use MOJO format since it’s optimized for production use.

h2o.save_model(aml.leader, path = "./Loan_Pred_Model_III_shaz13")Our take on AutoML

AutoML is here to stay. I am eager to see the direction where it goes to further advancements in data science. A single automated mixer certainly cannot outperform a human creative mind when it comes to feature engineering but in my experience, AutoML is worth exploring.

Although AutoML alone won’t get you top spot in machine learning competitions, it is definitely worth considering as an addition alongside your blended and stacked models. In recent competitions, the AutoML model boosted my score considerably which led me to explore and concentrate on the blending part. I highly recommend checking out H2O.ai’s AutoML. And, do let me know what do you think about it and your experiences with other automated modelling functions.
"""



o
