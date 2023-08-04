import streamlit as st
import pandas as pd

#fileName = "/Users/fenghua.gao/temp/generated_files/output_table.csv"
#df = pd.read_csv(fileName,index_col=0)

st.write("Fenghua's test for streamlit")
st.title('My Title')
strinput=st.text_input("my input")

if strinput == 'mytest':
    st.write("enter")
else:
    st.write('NO')

#st.dataframe(df)
print("OK..",strinput)
