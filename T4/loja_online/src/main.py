#RA:20.00089-8
import streamlit as st

from src.controllers.user_controller import UserController
from src.controllers.product_controller import ProductController
from src.controllers.cart_controller import CartController

Pcontroller = ProductController()

st.set_page_config(page_title="superloja", page_icon="assets/robin.png")

if "Login" not in st.session_state:
    st.session_state["Profile"] = "dados"
    st.session_state["Login"] = "negado"
    st.session_state["carrinho"] = ""
    st.session_state["Cart"] = CartController()
    st.session_state["Usuario"] = ""
    st.session_state["email"] = ""
    st.session_state["falta"] = ""
    

with st.sidebar:

    
    if st.session_state["Login"] == "negado" or st.session_state["Login"] == "errado":

        st.title("Login")
        st.markdown("***")

        email = st.text_input(
            label="Email",
        )

        password = st.text_input(
            label="Senha",
                type = "password"
        )
        st.text("")
        
        col1, col2 = st.columns(2)
        with col1:
            st.button(label= "Logar", on_click= UserController.check_login, args = (UserController(),email,password))

        with col2:
            st.button(label = "Registrar", on_click = UserController.sign_up_screen)
    
    if st.session_state['Login'] == 'errado':

        st.markdown("***")

        st.markdown("# Email ou senha errado(s)!")

        st.markdown("***")
        
    if st.session_state["Login"] == "registro":
        st.text("")
        st.text("")
        st.title("Cadastro")

        st.markdown("***")


        email = st.text_input(
            label="Email",
                key = 2,
        )

        name = st.text_input(
            label="Name",
                key = 1,
        )

        password = st.text_input(
            label="Senha",
                type = "password",
                    key = 3,
        )

        cpf = st.text_input(
            label="CPF",
                key = 4,
        )

        col1, col2 = st.columns(2)

        with col1:
            st.text("")
            st.button(label= "Cadastrar", on_click= UserController.sign_up, args = (UserController(),name, email, password, cpf))
        with col2:
            st.text("")
            st.button(label= "Voltar", on_click= UserController.login_screen)

    if st.session_state["Login"] == "aprovado":

        st.text("")
        st.markdown("***")
        st.title(f"Olá, {st.session_state['Usuario']}")
        st.markdown("***")
        st.button(label= "Logout", on_click= UserController.logout)
        st.markdown("***")

if "Login" in st.session_state:

    if st.session_state["Login"] == "aprovado":
        tab1, tab2, tab3, tab4 = st.tabs(["Perfil", "Home", "Carrinho", "Cadastrar Produto"])

        with tab1: 

            st.markdown("***")
            st.title("Perfil")
            st.markdown("***")
            st.text("")
            col1,col2 = st.columns(2)

            with col1:

                st.markdown("#")
                st.image("https://play-lh.googleusercontent.com/8ddL1kuoNUB5vUvgDVjYY3_6HwQcrg1K2fd_R8soD-e2QYj8fT9cfhfh3G0hnSruLKec")
                
            with col2:

                if st.session_state["Profile"] == "dados":
                    st.markdown("***")
                    st.markdown(f"### Nome: {st.session_state['Usuario']}")
                    st.markdown("***")
                    st.markdown(f"### Email: {st.session_state['Email']}")
                    st.markdown("***")
                    st.markdown(f"### CPF: {st.session_state['Cpf']}")
                    st.markdown("***")
                    st.button("Alterar dados", key = 7355608, on_click = UserController.change_login_data)


            if st.session_state["Profile"] == "change":



                password = st.text_input(
                    label="Nova Senha",
                        type = "password",
                            key = 56240,
                )
                
                
                
                email = st.text_input(
                    label="Novo Email",
                        key = 88888,
                )



                col3, col4 = st.columns(2)


                with col3:
                    st.button(label = "Voltar", key = 99427, on_click = UserController.go_back)
                
                with col4:
                    st.button(label= "Alterar", key = 578125, on_click= UserController.change_data, args = (UserController(), email, password))
        with tab2:

            st.title("Home")
            st.markdown("***")
            col1,col2 = st.columns(2,gap="large")

            
            for i in range(0, len(Pcontroller.get_products()) - 1, 2):
                with col1:

                    product = Pcontroller.get_product(index = i)
                    c = st.container()
                    c.markdown(f"## {product.get_name()}")
                    try:
                        c.image(f"{product.get_url()}")
                    except:
                        c.image("https://capitalaberto.com.br/wp-content/uploads/2019/04/naweb-1-1-300x300.png")

                    c.markdown(f"## R${product.get_price()}")

                    quantity1 = c.number_input(label = "", key = 100 * (i+1), format = "%i", step = 1,min_value = 1, max_value = product.get_amount())
                    c.button(label = f"Adicionar {product.get_name()}", key = 200 * (i+12), on_click= st.session_state["Cart"].add_product, args = (product, quantity1))
                with col2:

                    product = Pcontroller.get_product(index = i + 1)
                    c = st.container()
                    c.markdown(f"## {product.get_name()}")
                    try:
                        c.image(f"{product.get_url()}")
                    except:
                        c.image("https://capitalaberto.com.br/wp-content/uploads/2019/04/naweb-1-1-300x300.png")
                    c.markdown(f"## R${product.get_price()}")
                    quantity2 = c.number_input(label = "",  format = "%i", key = 300 * (i+83), step = 1,min_value = 1, max_value = product.get_amount())


                    c.button(label = f"Adicionar {product.get_name()}", key = 400 * (i+99), on_click= st.session_state["Cart"].add_product, args = (product, quantity2))

        with tab3:

            st.title("Carrinho")

            st.markdown("***")

            col1, col2, col3 = st.columns(3,gap="large")
            col1.markdown("### Produto")
            col2.markdown("### Preço")
            col3.markdown("### Quantidade")
            

            
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
                    c.markdown(f"### {product_names[i]}")


            with col2:

                c = st.container()
                for i in range(len(product_names)):
                    c.markdown(f"## R${product_prices[i]}")


            with col3:
                
                c = st.container()
                
                for i in range(len(product_names)):
                    c.markdown(f"## {product_qtt[i]}")


            st.markdown("***")
            
            valor_total = st.session_state["Cart"].get_total_price()
            
            st.markdown(f"## Valor total: R${valor_total:.3f} ")
            st.button(label = "Finalizar Pedido", key = 998, on_click= st.session_state["Cart"].clear_cart)
        
        with tab4:

            st.text("")
            st.text("")

            st.title("Cadastro De Produtos")

            st.markdown("***")
            
            name1 = st.text_input(
                label= "Name",
                    key = 44,
            )

            price1 = st.number_input(
                label="Preço",
                    key = 442,
            )

            url1 = st.text_input(
                label="URL Da Imagem",
                    key = 443,
            )

            amount1 = st.number_input(
                label = "Quantidade",
                    key = 444,
            )

            

            
            st.text("")
            st.button(label= "Cadastrar produto", on_click= ProductController.sign_product, args = (ProductController(), name1, price1, url1, amount1))
            
            st.markdown("### " + st.session_state["carrinho"])
        