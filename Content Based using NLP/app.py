import streamlit as st 
import pickle
import pandas as pd

st.title(":carrot: Instacart Store ")
st.write('*Content Based Recommedation Engine*- NLP ')
st.write('### **Find similar products at our store**') 

products_dict= pickle.load(open('top_products.pkl','rb'))
main_df= pd.DataFrame(products_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

product_selection= st.selectbox('Product',main_df['product_name'].values)

def recommend(product_name):
    product_index= main_df[main_df['product_name']==product_name].index[0]
    distances=similarity[product_index]
    products_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommendations_products=[]
    recommendations_aisle=[]
    recommendations_department=[]
    for i in products_list:
        recommendations_products.append(main_df.iloc[i[0]].product_name)
        recommendations_aisle.append(main_df.iloc[i[0]].aisle)
        recommendations_department.append(main_df.iloc[i[0]].department)
    return recommendations_products,recommendations_aisle,recommendations_department

# if st.button('Recommend'):
#     products,aisle,department=recommend(product_selection)
#     for i in recommendations:
#         st.write(i)
    #st.write(product_selection)
if st.button('Recommend'):
    products, aisles, departments = recommend(product_selection)
    
    for i in range(len(products)):
        st.write(f"**{products[i]}**, Aisle: *{aisles[i]}*, Department: *{departments[i]}*")
