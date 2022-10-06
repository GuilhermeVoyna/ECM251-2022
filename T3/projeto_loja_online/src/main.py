
import pickle
from pathlib import Path
from unicodedata import name

import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth
from controllers.cart_controller import CartController  # pip install streamlit-authenticator

from src.controllers.user_controller import UserController
from src.controllers.product_controller import ProductController
import hashing

st.set_page_config(page_title="Stim", page_icon="https://preview.redd.it/9zax3dujvt081.png?width=640&crop=smart&auto=webp&s=b3c360bbab7f5f12e891687f6509d3207b7c91bb", layout="wide")


# --- USER AUTHENTICATION ---
names = UserController.get_names(UserController())
usernames = UserController.get_usernames(UserController())

# load hashed passwords

try:
    file_path = Path(__file__).parent / "hashed_pw.pkl"
    file_path.open("rb")
except:
    hashing

with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "Steam", "abcdef", cookie_expiry_days=30)

#usuario: adm
#senha: adm

name, authentication_status, username = authenticator.login("Login", "main")
if authentication_status == False:
    st.error("Username/password is incorrect")
    st.session_state["Cart"] = CartController()

if authentication_status == None:
    st.warning("Please enter your username and password")
    
    st.session_state["Cart"] = CartController()

if authentication_status:
    authenticator.logout("Logout")
    st.sidebar.title(f"Welcome *{name}*")
    if username == "adm":
        st.sidebar.image("https://images.fineartamerica.com/images/artworkimages/medium/3/among-us-imposter-master-arcade-transparent.png")
        st.sidebar.markdown("***")
        st.sidebar.title(f"Loja suspeita . . .")
        st.sidebar.markdown("***")
    else:
        st.sidebar.image("https://pfpmaker.com/_nuxt/img/profile-3-1.3e702c5.png")
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
        quantity0 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"+ Cart", key = index, on_click= st.session_state["Cart"].add_product, args = (product, quantity0))
    with col2:
        index = 1
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity1 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"+ Cart", key = index, on_click= st.session_state["Cart"].add_product, args = (product, quantity1))
    with col1:
        index = 2
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity2 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"+ Cart", key = index, on_click= st.session_state["Cart"].add_product, args = (product, quantity2))
    with col2:
        index = 3
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity3 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"+ Cart", key = index, on_click= st.session_state["Cart"].add_product, args = (product, quantity3))

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
        quantity4 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"+ Cart", key = index, on_click= st.session_state["Cart"].add_product, args = (product, quantity4))

    with col2:
        index = 5
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity5 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"+ Cart", key = index, on_click= st.session_state["Cart"].add_product, args = (product, quantity5))
    with col1:
        index = 6
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity6 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"+ Cart", key = index, on_click= st.session_state["Cart"].add_product, args = (product, quantity6))
    with col2:
        index = 7
        product = ProductController.get_product(ProductController(),index)
        c = st.container()
        c.markdown(f"## {product.get_name()}")
        c.image(f"{product.get_url()}", width = 300)
        c.markdown(f"## R${product.get_price()}")
        quantity7 = c.number_input(label = " "*index, format = "%i", step = 1,min_value = 1)
        c.button(label = f"+ Cart", key = index, on_click= st.session_state["Cart"].add_product, args = (product, quantity7))
    
    # teste

    def novo_carro():
        st.session_state["Cart"] = CartController()

    # --- Cart area ---
    with tab3:
            st.title("Carrinho")

            st.markdown("***")

            col1, col2, col3,col4 = st.columns(4,gap="large")
            col1.markdown("### Item")
            col2.markdown("### Price")
            col3.markdown("### Unities")
        
            
            
            
            product_qtt = []
            product_names = []
            product_prices = []
            for produquantity in st.session_state["Cart"].get_cart().get_products():
                product_names.append(produquantity[0].get_name())
                product_prices.append(produquantity[0].get_price())
                product_qtt.append(produquantity[1])
                    
            with col1:
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_names[i]}")
            with col2:
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### R${product_prices[i]}")
            with col3:
                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"#### {product_qtt[i]}")
            with col4:
                c.button(label = f"Clear", key = 666, on_click= novo_carro)


            st.markdown("***")
            valor_total = st.session_state["Cart"].get_total_price()
            st.markdown(f"## Total: ${valor_total:.3f} \n you have to pay in dollars 🤑")
            c1 = st.container()
            c1.button(label = f"Pay", key = 6666, on_click= novo_carro)
            st.markdown("***")
                        