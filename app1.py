import streamlit as st
import pickle
import numpy as np

log_model = pickle.load(open('log.pkl','rb'))
dec_model = pickle.load(open('dec.pkl','rb'))
ran_model = pickle.load(open('ran.pkl','rb'))

def classify(num):
    if num == 1:
        return 'Cancer Type : Malignant [Malignant cells are cancerous and they can spread rapidly in the body.]'
    else:
        return 'Cancer Type : Benign [Benign tumors are not cancerous, they cannot spread or they can grow very slowly.]'

def main():
    import streamlit as st
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;"> BREAST CANCER PREDICTION APP </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("""
             **This app predicts the type of breast cancer !** 
""")
  
    activities=['Random Forest Classifier', 'SVM','Logistic Regression','Decision Tree Classifier']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    
    st.write("""
           
           """)
    Clump_Thickness = st.slider('Select Clump Thickness', 0,10)
    Uniformity_Cell_Size = st.slider('Select Uniformity Cell Size', 0,10)
    Uniformity_Cell_Shape  = st.slider('Select Uniformity Cell Shape', 0,10)
    Marginal_Adhesion = st.slider('Select Marginal Adhesion', 0,10)
    Single_Epithelial_Size = st.slider('Select Single Epithelial Size', 0,10)
    Bare_Nuclei = st.slider('Select Bare Nuclei', 0,10)
    Bland_Chromatin = st.slider('Select Bland Chromatin', 0,10)
    Normal_Nucleoli = st.slider('Select Normal Nucleoli', 0,10)
    Mitoses = st.slider('Select Mitoses', 0,10)
    
    
    
    inputs=[[Clump_Thickness,Uniformity_Cell_Size,Uniformity_Cell_Shape,Marginal_Adhesion,Single_Epithelial_Size,Bare_Nuclei,Bland_Chromatin,Normal_Nucleoli,Mitoses]]

    if st.button('Classify'):
        if option=='Random Forest Classifier':
            st.success(classify(ran_model.predict(inputs)))
        elif option=='Logistic Regression':
            st.success(classify(log_model.predict(inputs)))
        else:
           st.success(classify(ran_model.predict(inputs)))

if __name__=='__main__':
    main()
