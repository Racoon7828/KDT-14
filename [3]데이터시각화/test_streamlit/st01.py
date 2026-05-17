import streamlit as st, pandas as pd, seaborn as sns
st.title('Streamlit Exaple')
st.write('This is a simple streamlit app.')

df = sns.load_dataset('penguins')
# print(df)
df_group = df.groupby('species')['body_mass_g'].mean().reset_index()
# print(df_group)

st.bar_chart(df_group, x='species', y='body_mass_g')


















