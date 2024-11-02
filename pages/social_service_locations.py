import streamlit as st
import pandas as pd
import pydeck as pdk
from utility import check_password

#check if password is correct
if not check_password():
    st.stop()

data = {
    "SSO Location": [
        "Ang Mo Kio", "Bedok", "Boon Lay", "Bukit Batok", "Bukit Merah", "Bukit Panjang",
        "Clementi", "Chua Chu Kang", "Geylang Serai", "Hougang", "Jalan Besar", "Jurong East",
        "Kreta Ayer", "Pasir Ris", "Punggol", "Queenstown", "Sembawang", "Sengkang", "Serangoon",
        "Taman Jurong", "Tampines", "Toa Payoh", "Woodlands", "Yishun"
    ],
    "Address": [
        "6A Ang Mo Kio St 53, Ang Mo Kio 3G Centre, Singapore 569208",
        "21 Bedok North St 1, #01-02, Singapore 469659",
        "NKF Integrated Renal Centre, 500 Corporation Road, #01-01, Singapore 649808",
        "Blk 369 Bukit Batok St 31, #01-505, Singapore 650369",
        "Bukit Merah Community Hub, 3779 Jalan Bukit Merah, #01-01, Singapore 159462",
        "Blk 232 Pending Road, #01-29, Singapore 670232",
        "Blk 358 Clementi Ave 2, #01-285, Singapore 120358",
        "8A Teck Whye Lane, Singapore 681008",
        "10 Eunos Road 8, Singapore Post Centre, #12-02, Singapore 408600",
        "Blk 662 Hougang Ave 4, #01-413, Singapore 530662",
        "Jalan Besar Community Club, 69 Jellicoe Road, #01-03, Singapore 208737",
        "Devan Nair Institute for Employment and Employability, 80 Jurong East Street 21, #01-07, Singapore 609607",
        "Kreta Ayer Community Club, 28A Kreta Ayer Road, #01-03, Singapore 088995",
        "120 Pasir Ris Central, Pasir Ris Sports Centre, #01-16, Singapore 519640",
        "ServiceSG Centre One Punggol, One Punggol Drive, #01-01, Singapore 828629",
        "Block 40 Margaret Drive, #02-01, Singapore 140040",
        "Blk 315 Sembawang Vista, #01-173, Singapore 750315",
        "Blk 261C Sengkang East Way, #01-506, Singapore 543261",
        "Blk 332 Serangoon Ave 3, #01-257, Singapore 550332",
        "301A Corporation Drive, Singapore 619773",
        "ServiceSG Centre, Our Tampines Hub, 1 Tampines Walk, #01-21, Singapore 528523",
        "490 Lor 6 Toa Payoh, HDB Hub Bizthree, #07-11, Singapore 310490",
        "900 South Woodlands Drive, Woodlands Civic Centre, #06-13, Singapore 730900",
        "Blk 746 Yishun Street 72, #01-127, Singapore 760746"
    ],
    "Latitude": [
        1.3691, 1.3273, 1.3459, 1.3483, 1.2829, 1.3771, 1.3005, 1.3840, 1.3190, 1.3741,
        1.3070, 1.3330, 1.2800, 1.3730, 1.4050, 1.2940, 1.4450, 1.3910, 1.3560, 1.3380,
        1.3540, 1.3330, 1.4320, 1.4290
    ],
    "Longitude": [
        103.8498, 103.9305, 103.7190, 103.7500, 103.8030, 103.7715, 103.7640, 103.7470, 103.8980,
        103.8842, 103.8600, 103.7420, 103.8400, 103.9490, 103.9020, 103.8030, 103.8180, 103.8950,
        103.8700, 103.7240, 103.9400, 103.8500, 103.7860, 103.8350
    ]
}

df = pd.DataFrame(data)

st.title("Map of Social Service Offices in Singapore")

map_view = pdk.ViewState(
    latitude=1.3521,  # Central latitude for Singapore
    longitude=103.8198,  # Central longitude for Singapore
    zoom=11,
    pitch=50,
)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position="[Longitude, Latitude]",
    get_radius=200,
    get_color=[0, 0, 255],
    pickable=True,
)

st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=map_view,
    layers=[layer],
    tooltip={"text": "{SSO Location}\n{Address}"}
))

st.title("Addresses of Social Service Offices:")
st.dataframe(df[["SSO Location", "Address"]])

st.markdown("""
**Disclaimer**

IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalized advice. Please visit www.msf.gov.sg for the latest information
""")