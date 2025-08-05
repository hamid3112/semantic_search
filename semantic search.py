#!/usr/bin/env python
# coding: utf-8

# In[5]:


from sentence_transformers import SentenceTransformer
import streamlit as st
import numpy as np
from sentence_transformers import SentenceTransformer , util
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer('all-mpnet-base-v2')
sentences = [
    "I love playing football.",
    "Soccer is a fun sport to play.",
    "The weather is sunny today.",
    "He enjoys watching football games.",
    "It is raining outside.",
    "I prefer rainy days.",
    "Today is a cold and wet day."
]
sentence_embeding = model.encode(sentences , convert_to_tensor=True)
#streamlit
st.title("Semsantic Search With Sentence Embeddings")
query = st.text_input("Enter your query sentence:")
top_k = st.slider("Number of result to show" , min_value= 1 , max_value= 10 , value=3)
if query:
    query_embeding = model.encode(query , convert_to_tensor=True)
    cos_score = util.cos_sim(query_embeding , sentence_embeding)[0]
    cos_score = np.array(cos_score)
    top_result = np.argsort(cos_score)[::-1][:top_k]
    st.write(f"Top {top_k} similar sentence :")
    for idx in top_result :
        st.write(f" - {sentences[idx]} (score : {cos_score[idx]:.4f})")

