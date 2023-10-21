{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fcfbc2a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "\n",
    "def predict(data):\n",
    "    clf = joblib.load(\"rf_model.sav\")\n",
    "    return clf.predict(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "869120fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "#from prediction.py import predict\n",
    "\n",
    "\n",
    "st.title('Classifying Iris Flowers')\n",
    "st.markdown('Toy model to play to classify iris flowers into \\\n",
    "     (setosa, versicolor, virginica) based on their sepal/petal \\\n",
    "    and length/width.')\n",
    "\n",
    "st.header(\"Plant Features\")\n",
    "col1, col2 = st.columns(2)\n",
    "\n",
    "with col1:\n",
    "    st.text(\"Sepal characteristics\")\n",
    "    sepal_l = st.slider('Sepal lenght (cm)', 1.0, 8.0, 0.5)\n",
    "    sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 0.5)\n",
    "\n",
    "with col2:\n",
    "    st.text(\"Pepal characteristics\")\n",
    "    petal_l = st.slider('Petal lenght (cm)', 1.0, 7.0, 0.5)\n",
    "    petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 0.5)\n",
    "\n",
    "st.text('')\n",
    "if st.button(\"Predict type of Iris\"):\n",
    "    result = predict(\n",
    "        np.array([[sepal_l, sepal_w, petal_l, petal_w]]))\n",
    "    st.text(result[0])\n",
    "\n",
    "\n",
    "st.text('')\n",
    "st.text('')\n",
    "st.markdown(\n",
    "    '`Create by` [santiviquez](https://twitter.com/santiviquez) | \\\n",
    "         `Code:` [GitHub](https://github.com/santiviquez/iris-streamlit)')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d941c941",
   "metadata": {},
   "source": [
    "streamlit run C:\\Users\\HERMANN\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52b9a7f3",
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
