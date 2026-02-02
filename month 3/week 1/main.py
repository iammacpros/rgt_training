# import libraries
import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer

st.title("Gemma 3 Text Generation")
st.caption("Generating text using Gemma 3 model.")

# Load model
@st.cache_data
def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    return tokenizer, model

model_name = "google/gemma-3-270m-it"
tokenizer, model = load_model(model_name)

# function to generate text
def generate_text(prompt, max_length=200, num_return_sequences=1, temperature=0.8, top_k=50, top_p=0.95):
    
    # tokenize input prompt
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)

    # Generate text
    outputs = model.generate(**inputs, 
                            max_length=max_length, 
                            temperature=temperature, 
                            top_k=top_k, 
                            top_p=top_p, 
                            do_sample=True)

    # Decode all generated sequences
    generated_message = [tokenizer.decode(outputs[0], skip_special_tokens=True)]
    return generated_message

# prompts
prompts = [
    "Once upon a time in a distant land,",
    "Artificial intelligence is revolutionizing healthcare by",
    "What is the meaning of life?"]

# results
if 'results' not in st.session_state:
    st.session_state['results'] = [None] * len(prompts)

for i, prompt in enumerate(prompts):
    st.text_area(f"Input Prompt {i+1}", value=prompt, height=100)

    if st.session_state['results'][i] is None:
        with st.spinner(f"Generating text for Prompt {i+1}..."):
            st.session_state['results'][i] = generate_text(prompt)[0]
    st.text_area(f"Generated Text {i+1}", value=st.session_state['results'][i], height=300)


# Initialize settings in session state
if 'max_new_tokens' not in st.session_state:
    st.session_state['max_new_tokens'] = 150
if 'temperature' not in st.session_state:
    st.session_state['temperature'] = 0.7
if 'top_p' not in st.session_state:
    st.session_state['top_p'] = 0.9
if 'top_k' not in st.session_state:
    st.session_state['top_k'] = 30

# Sidebar for configuration
with st.sidebar:
    st.title("⚙️ Model Settings")
    model_name = "google/gemma-3-270m-it"
    st.info(f"Model: {model_name}")
    
    # Use local variables for sliders to avoid immediate updates to session state
    new_max_tokens = st.slider("Max New Tokens", 50, 512, st.session_state['max_new_tokens'])
    new_temp = st.slider("Temperature", 0.0, 1.5, st.session_state['temperature'])
    new_top_p = st.slider("Top P", 0.0, 1.0, st.session_state['top_p'])
    new_top_k = st.slider("Top K", 1, 100, st.session_state['top_k'])
    
    if st.button("Apply Settings"):
        st.session_state['max_new_tokens'] = new_max_tokens
        st.session_state['temperature'] = new_temp
        st.session_state['top_p'] = new_top_p
        st.session_state['top_k'] = new_top_k
        st.success("Settings applied!")

    # Show applied settings
    st.write("---")
    st.write("**Applied Settings:**")
    st.write(f"- Tokens: {st.session_state['max_new_tokens']}")
    st.write(f"- Temp: {st.session_state['temperature']}")
    st.write(f"- Top P: {st.session_state['top_p']}")
    st.write(f"- Top K: {st.session_state['top_k']}")


# function to generate text
def generate_texts(prompt):
    # Retrieve settings from session state
    max_tokens = st.session_state.get('max_new_tokens', 150)
    temp = st.session_state.get('temperature', 0.7)
    tp = st.session_state.get('top_p', 0.9)
    tk = st.session_state.get('top_k', 30)
    
    # tokenize input prompt
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)

    # Generate text
    outputs = model.generate(**inputs, 
                            max_new_tokens=max_tokens, 
                            temperature=temp, 
                            top_k=tk, 
                            top_p=tp, 
                            do_sample=True)

    # Decode all generated sequences
    generated_message = [tokenizer.decode(outputs[0], skip_special_tokens=True)]
    return generated_message


# User custom prompt
st.subheader("Try your own prompt")
user_prompt = st.text_input("Enter a custom prompt:")
if st.button("Generate Custom"):
    if user_prompt:
        with st.spinner("Generating..."):
            result = generate_texts(user_prompt)
            st.markdown(result[0])
            # st.write(result)
    else:
        st.warning("Please enter a prompt first.")
