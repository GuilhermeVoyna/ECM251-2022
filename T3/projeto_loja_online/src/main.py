
import pickle
from pathlib import Path
from unicodedata import name

import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator

from src.controllers.user_controller import UserController
from src.controllers.product_controller import ProductController


st.set_page_config(page_title="Stim", page_icon="https://preview.redd.it/9zax3dujvt081.png?width=640&crop=smart&auto=webp&s=b3c360bbab7f5f12e891687f6509d3207b7c91bb", layout="wide")


# --- USER AUTHENTICATION ---
names = UserController.get_names(UserController())
usernames = UserController.get_usernames(UserController())

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "Steam", "abcdef", cookie_expiry_days=30)

#usuario: adm
#senha: adm

name, authentication_status, username = authenticator.login("Login", "main")
if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    authenticator.logout("Logout")
    st.sidebar.title(f"Welcome *{name}*")
    st.sidebar.image("https://i.pinimg.com/736x/ea/8b/c0/ea8bc0fd9e2bf37e9ad09f056ff6ebc6.jpg")
    st.sidebar.markdown("***")
    st.sidebar.title(f"Super Loja *GAMER*")
    st.sidebar.markdown("***")
    
    tab1, tab2,tab3= st.tabs(["Games", "Product for gamers","Cart"])

    # --- GAMES AREA ---
    with tab1: 
            st.title("GAMES")

            st.markdown("***")
            st.text("")
            col1,col2 = st.columns(2,gap="large")

    with col1:
        index = 0
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        c.button(label = f"+ Cart", key = index)

    with col2:
        index = 1
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        c.button(label = f"+ Cart", key = index)
    with col1:
        index = 2
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        c.button(label = f"+ Cart", key = index)
    with col2:
        index = 3
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        c.button(label = f"+ Cart", key = index)

    # --- Product area ---
    with tab2: 
            st.title("Products")

            st.markdown("***")
            st.text("")
            col1,col2 = st.columns(2,gap="large")
    with col1:
        index = 4
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity4 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 0)
        c.button(label = f"+ Cart", key = index)

    with col2:
        index = 5
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity7 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 0)
        c.button(label = f"+ Cart", key = index)
    with col1:
        index = 6
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity5 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 0)
        c.button(label = f"+ Cart", key = index)
    with col2:
        index = 7
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity7 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 0)
        c.button(label = f"+ Cart", key = index)
    
    # --- Cart area ---