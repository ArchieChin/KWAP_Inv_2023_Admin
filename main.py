# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:53:38 2023

@author: archi
"""

import streamlit as st
from deta import Deta

deta = Deta("c0ky03c3_FeGypxDjVhTDCQU96cfUqLkstZLvo6Bb")
db = deta.Base("current_question")

st.title("KWAP 2023 Investment Retreat - Admin")
key = "8brqm6kqm281"
if st.button("Question 1"):
    output = db.put({"question":1}, key)
    f"Currently showing Question {output["question"]}"
    
if st.button("Question 2"):
    output = db.insert({"question":2}, key)
    f"Currently showing Question {output["question"]}"
    
if st.button("Question 3"):
    output = db.insert({"question":3}, key)
    f"Currently showing Question {output["question"]}"
    
