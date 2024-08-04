from PIL import Image
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Chart Explanation", page_icon="📈")

st.header("Chart Explanation from AI")
template = "This is an image of a chart of a blockchain data, kindly explain it to me, MUST BE VERY DETAILED, if it isn't an image of a chart tell me you can't help me with it"
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

image = st.file_uploader("Select Chart Image to get explanation for")
if image is not None:
    st.success("Image uploaded successfully")        
    with st.spinner("Asking AI..."):
        try:
            pil_image = Image.open(image)
            response = model.generate_content([template, pil_image])
            pic, texts = st.columns([0.3, 0.7], gap="small")
            
            with pic:
                st.subheader("Uploaded Image")
                st.image(pil_image)
                
            with texts:
                st.subheader("AI Explanation")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"Error reading Image: {e}")
   