# ========================
# Product Price Finder App
# ========================

# Imports
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables (e.g., GROQ API keys)
load_dotenv()

# Define the structured output schema using Pydantic
class Product(BaseModel):
    product_name: str = Field(description='The name of the product.')
    tentative_price_in_usd: int = Field(description='Estimated price of the product in USD.')

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ('system', 
     "You are a helpful assistant with deep expertise in product sales. "
     "Based on the user's input, extract the product name and its tentative price in USD (with a dollar sign)."),
    ('human', "{input}")
])

# Streamlit UI Setup
st.set_page_config(page_title="Product Price Finder", page_icon="🚀")
st.title("🔍 Product Price Finder with LLMs")

# Model selection dropdown
model_options = [
    'deepseek-r1-distill-llama-70b',
    'qwen-qwq-32b',
    'llama-3.1-8b-instant'
]
selected_model = st.selectbox("Select a Model:", model_options)

# Text input for product description
product_description = st.text_area("Enter Product Description:", placeholder="E.g., iPhone 15 Pro Max with 256GB storage...")

# Submit button
if st.button("Fetch Product Details"):

    # Validate inputs
    if not product_description.strip():
        st.warning("Please enter a valid product description.")
    else:
        # Load model and chain
        try:
            model = ChatGroq(model=selected_model)
            structured_output_model = model.with_structured_output(Product)
            processing_chain = prompt | structured_output_model

            # Run the model
            result: Product = processing_chain.invoke({'input': product_description})

            # Display results
            st.success("✅ Product Information Extracted Successfully:")
            st.write(f"**Product Name:** {result.product_name}")
            st.write(f"**Estimated Price:** ${result.tentative_price_in_usd}")

        except Exception as e:
            st.error(f"An error occurred while fetching details: {e}")
