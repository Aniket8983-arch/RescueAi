
import streamlit as st
from streamlit_folium import st_folium

from modules.ai_engine import generate_first_aid
from modules.location_service import get_coordinates
from modules.hospital_map import get_nearby_hospitals
from modules.map_display import show_map


# --------------------------------
# PAGE CONFIG
# --------------------------------
st.set_page_config(
    page_title="AI First Aid Assistant",
    page_icon="🚑",
    layout="wide"
)

# --------------------------------
# CUSTOM CSS
# --------------------------------
st.markdown("""
<style>

.main {
    background-color: #f4f6fb;
}

h1 {
    color: #1f4e79;
}

h2, h3 {
    color: #003366;
}

.stButton>button {
    border-radius: 12px;
    background-color: #1976d2;
    color: white;
    height: 3em;
    width: 100%;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #0d47a1;
}

.card {
    padding:20px;
    border-radius:10px;
    background-color:white;
    box-shadow:0px 2px 6px rgba(0,0,0,0.1);
}

.hero {
    padding:30px;
    border-radius:12px;
    background:linear-gradient(90deg,#1976d2,#42a5f5);
    color:white;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------
# SESSION STATE
# --------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "email" not in st.session_state:
    st.session_state.email = ""

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "map_data" not in st.session_state:
    st.session_state.map_data = None

if "selected_hospital" not in st.session_state:
    st.session_state.selected_hospital = None

if "emergency" not in st.session_state:
    st.session_state.emergency = ""


# --------------------------------
# LOGIN PAGE
# --------------------------------
def login_page():

    st.title("🚑 AI First Aid Assistant")

    st.subheader("Login")

    email = st.text_input("Email")
    username = st.text_input("Username")

    if st.button("Login"):

        if email and username:

            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.email = email
            st.rerun()

        else:

            st.warning("Please enter both email and username")


if not st.session_state.logged_in:
    login_page()
    st.stop()


# --------------------------------
# HEADER
# --------------------------------
col1, col2, col3 = st.columns([6,3,1])

with col1:
    st.title("🚑 AI First Aid Assistant")

with col2:
    st.text_input("Search emergencies")

with col3:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

st.write(f"👤 Logged in as **{st.session_state.username}**")


# --------------------------------
# NAVIGATION
# --------------------------------
nav1, nav2, nav3 = st.columns(3)

if nav1.button("🏠 Home"):
    st.session_state.page = "Home"

if nav2.button("🩺 Emergency AI"):
    st.session_state.page = "Emergency"

if nav3.button("🏥 Nearby Hospitals"):
    st.session_state.page = "Maps"

st.divider()


# --------------------------------
# HOME PAGE
# --------------------------------
if st.session_state.page == "Home":

    st.markdown("""
    <div class="hero">
    <h2>AI First Aid Assistant</h2>
    <p>Instant emergency guidance and nearby hospital locator powered by AI.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Quick Emergency Help")

    # Row 1
    col1, col2, col3, col4 = st.columns(4)

    if col1.button("🔥 Burn"):
        st.session_state.emergency = "Person has a burn injury"
        st.session_state.page = "Emergency"

    if col2.button("😮‍💨 Choking"):
        st.session_state.emergency = "Person choking"
        st.session_state.page = "Emergency"

    if col3.button("🐍 Snake Bite"):
        st.session_state.emergency = "Person bitten by snake"
        st.session_state.page = "Emergency"

    if col4.button("🦴 Fracture"):
        st.session_state.emergency = "Possible bone fracture"
        st.session_state.page = "Emergency"


    # Row 2
    col5, col6, col7, col8 = st.columns(4)

    if col5.button("💔 Heart Attack"):
        st.session_state.emergency = "Symptoms of heart attack"
        st.session_state.page = "Emergency"

    if col6.button("🧠 Stroke"):
        st.session_state.emergency = "Possible stroke symptoms"
        st.session_state.page = "Emergency"

    if col7.button("☠ Poisoning"):
        st.session_state.emergency = "Possible poisoning"
        st.session_state.page = "Emergency"

    if col8.button("⚡ Electric Shock"):
        st.session_state.emergency = "Person received electric shock"
        st.session_state.page = "Emergency"


# --------------------------------
# EMERGENCY AI PAGE
# --------------------------------
elif st.session_state.page == "Emergency":

    st.header("🩺 AI Emergency Assistant")

    emergency = st.text_area(
        "Describe the emergency",
        value=st.session_state.get("emergency","")
    )

    if st.button("Get First Aid Instructions"):

        if emergency:

            with st.spinner("Analyzing situation..."):

                response = generate_first_aid(emergency)

            st.success("Emergency guidance generated")

            st.markdown(response)

        else:

            st.warning("Please describe the emergency")


# --------------------------------
# MAP PAGE
# --------------------------------
elif st.session_state.page == "Maps":

    st.header("🏥 Nearby Hospitals")

    city = st.text_input("Enter your city")

    if st.button("Find Nearby Hospitals"):

        lat, lon = get_coordinates(city)

        if lat:

            hospitals = get_nearby_hospitals(lat, lon)

            if not hospitals:

                st.warning("No hospitals found nearby.")

            else:

                st.session_state.map_data = {
                    "lat": lat,
                    "lon": lon,
                    "hospitals": hospitals
                }

                st.session_state.selected_hospital = None

        else:

            st.error("City not found")


    if st.session_state.map_data:

        map_col, info_col = st.columns([2,1])

        with map_col:

            map_object = show_map(
                st.session_state.map_data["lat"],
                st.session_state.map_data["lon"],
                st.session_state.map_data["hospitals"]
            )

            map_data = st_folium(
                map_object,
                width=800,
                height=500,
                key="hospital_map",
                returned_objects=["last_object_clicked"]
            )

            if map_data and map_data.get("last_object_clicked"):

                lat_click = map_data["last_object_clicked"]["lat"]
                lon_click = map_data["last_object_clicked"]["lng"]

                for hospital in st.session_state.map_data["hospitals"]:

                    if abs(hospital["lat"] - lat_click) < 0.0005 and abs(hospital["lon"] - lon_click) < 0.0005:

                        st.session_state.selected_hospital = hospital
                        break


        with info_col:

            st.subheader("Hospital Information")

            if st.session_state.selected_hospital:

                hospital = st.session_state.selected_hospital

                st.markdown(f"### {hospital['name']}")

                st.write(f"📍 {hospital['address']}")

                if hospital["phone"]:
                    st.write(f"📞 {hospital['phone']}")

            else:

                st.info("Click a hospital marker on the map to see details.")

