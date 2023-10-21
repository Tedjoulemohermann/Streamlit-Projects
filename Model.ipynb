{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a66de257",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-22-cd1ceaa3a085>:27: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().\n",
      "  clf.fit(X_train, y_train)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.9111111111111111\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['rf_model.sav']"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.model_selection import train_test_split\n",
    "import joblib\n",
    "\n",
    "# random seed\n",
    "seed = 42\n",
    "\n",
    "# Read original dataset\n",
    "iris_df = pd.read_csv(\"Streamlit_Datasets/iris.csv\")\n",
    "iris_df.sample(frac=1, random_state=seed)\n",
    "\n",
    "# selecting features and target data\n",
    "X = iris_df[['sepal_length','sepal_width', 'petal_length', 'petal_width']]\n",
    "y = iris_df[['species']]\n",
    "\n",
    "# split data into train and test sets\n",
    "# 70% training and 30% test\n",
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X, y, test_size=0.3, random_state=seed, stratify=y)\n",
    "\n",
    "# create an instance of the random forest classifier\n",
    "clf = RandomForestClassifier(n_estimators=100)\n",
    "\n",
    "# train the classifier on the training data\n",
    "clf.fit(X_train, y_train)\n",
    "\n",
    "# predict on the test set\n",
    "y_pred = clf.predict(X_test)\n",
    "\n",
    "# calculate accuracy\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "print(f\"Accuracy: {accuracy}\")  # Accuracy: 0.91\n",
    "\n",
    "# save the model to disk\n",
    "joblib.dump(clf, \"rf_model.sav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76cb2a7e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf91430e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
