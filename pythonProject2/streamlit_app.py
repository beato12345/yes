import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import requests

st.set_page_config(page_title="My Webpage", page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name)as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")



st.subheader("Hi, I am Yash :wave:")
st.title("How to be physically fit?")
st.write("I will teach you today how to be physically fit")
st.write("[Learn More >](https://www.roblox.com/games/14570378822/Bodybuilder-Simulator)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i do")
        st.write("##")
        st.write(
            """
                On my Website I am giving tips for people who:

                - Want improve their life style.
                - Want to impress their crush.
                - Want to remove excessive body fats.
                - Want to be physically healthy.
                - Want to know the importance of exercising.

                If this sound interesting to you, Carefully analyze and read all tips that i would suggest so you can be physically healthy.
                """
        )
        st.write(
            "[You be like this if you follow my tips carefully.](https://www.google.com/search?sca_esv=599792272&rlz=1C1CHZN_enPH1085PH1085&q=best+muscles&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiOmZmGyumDAxXqS2wGHXVmArMQ0pQJegQIDhAB&biw=954&bih=935&dpr=1#imgrc=GEdfoxFJSDQfmM)")


        lottie_coding =("https://lottie.host/03fe581a-6e46-4dea-8d40-6568b5fcd9fb/x0eRhynVpz.json")
        img_contact_form = Image.open("images/chiken.png.jpg")
        img_lottie_animation = Image.open("images/chicken2.png.webp")

        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
        with text_column:
            st.subheader("To gain muscles, egg is a must")
            st.write(
                """
                Egg is very essential in gaining muscles,Muscles need protein to repair and grow.
                Eggs are rich in high quality protein, supplying all 9 essential amino acids and are therefore an ideal choice for post-workout nutrition.                     
                The greater your muscle mass, the more calories you burn, even when resting.
                """
            )
            st.markdown(
                "[Watch for proof...](https://www.youtube.com/watch?v=SoAIuq8fyEg&pp=ygUTY2hpY2tlbiBsaWZlIHJvYmxveA%3D%3D)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
        with text_column:
            st.subheader("Jogging everyday")
            st.write(
                """
                It will make you feel good and help you to become the fittest version of yourself. 
                 Running increases your core body temperature and prompts it to start shedding extra body fat.
                 The more consistent you are with it, the more calories you burn. Moreover, running every day helps your body build lean muscles.
                 """
            )
            st.markdown(
                "[if you do this tip everyday,this will be the result](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2Fbodybuilder--424956914816613292%2F&psig=AOvVaw0reEbeD5U2f154z9I9mThn&ust=1705845955497000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCNCf08SR7IMDFQAAAAAdAAAAABAD)")

            with st.container():
                st.write("---")
                st.write("##")

                contact_form = """
                <form action="https://formsubmit.co/yashbeato27@gmail.com" method="POST">
                     <input type="hidden" name="_captcha" value="false">
                     <input type="text" name="name" placeholder="Your name" required>
                     <input type="email" name="email" placeholder="Your email" required>
                     <textarea name="message" placeholder="Your message here" required></textarea>
                     <button type="submit">Send</button>
                </form>
                """
                left_column, right_column = st.columns(2)
                with left_column:
                    st.markdown(contact_form, unsafe_allow_html=True)
                    with right_column:
                        st.empty()





 





