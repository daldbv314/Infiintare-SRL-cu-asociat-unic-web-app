import os
import io
import datetime
import streamlit as st
from zipfile import ZipFile
from pathlib import Path
from docxtpl import DocxTemplate
from dotenv import load_dotenv
from io import BytesIO



st.set_page_config(
    page_title='Înfiintare', 
    layout='wide',
)
st.title('Creează actele pentru înființare SRL cu asociat unic:')


    #--- HIDE STREAMLIT STYLE ---
    # hide_st_style = """
    #             <style>
    #             #MainMenu {visibility: hidden;}
    #             footer {visibility: hidden;}
    #             header {visibility: hidden;}
    #             </style>
    #             """
    # st.markdown(hide_st_style, unsafe_allow_html=True)

with st.form("Înființare", clear_on_submit=False):
        
    st.subheader('Act constitutiv:')
    col1, col2, col3, col4 = st.columns(4, gap="small")
    as1_nume = col1.text_input('Nume Asociat:', value="", key='as1_nume', placeholder='e.g. Popescu', max_chars=None)
    as1_prenume = col2.text_input('Prenume Asociat:', value="", key='as1_prenume', placeholder='e.g. Popescu', max_chars=None)
    as1_cetatean = col3.text_input('Cetațean:', value="român", key='as1_cetatean', placeholder='e.g. român')
    as1_data_n = col4.date_input('Data naștere:', datetime.date.today(), key='as1_data_n', help=None, format="DD.MM.YYYY", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 1, 1))
    as1_loc_n = col1.text_input('Localitate naștere:', value="", key='as1_loc_n', placeholder='e.g. BRAȘOV', max_chars=None)
    as1_jud_n = col2.text_input('Județ/sector naștere:', value="", key='as1_jud_n', placeholder='e.g. BRAȘOV', max_chars=None)
    as1_tara_n = col3.text_input('Țara naștere:', value="România", key='as1_tara_n', placeholder='e.g. România', max_chars=None)

    col1, col2, col3, col4, col5, col6, col7 = st.columns([0.25, 0.25, 0.1, 0.1, 0.1, 0.1, 0.1], gap="small")
    as1_loc_dom = col1.text_input('Localitate domiciliu', key='as1_loc_dom', placeholder='e.g. BRAȘOV')
    as1_str_dom = col2.text_input('Strada domiciliu', key='as1_str_dom', placeholder='e.g. NICOLAE LABIȘ')
    as1_nr_dom = col3.text_input('Nr.', key='as1_nr_dom', placeholder='xx')
    as1_bl_dom = col4.text_input('Bl.', key='as1_bl_dom', placeholder='xx')
    as1_sc_dom = col5.text_input('Sc.', key='as1_sc_dom', placeholder='xx')
    as1_et_dom = col6.text_input('Et.', key='as1_et_dom', placeholder='xx')
    as1_ap_dom = col7.text_input('Ap.', key='as1_ap_dom', placeholder='xx')

    col1, col2, col3, col4 = st.columns(4, gap="small")
    as1_jud_dom = col1.text_input('Județ/sector domiciliu', key='as1_jud_dom', placeholder='e.g. BRAȘOV')
    as1_tara_dom = col2.text_input('Țara domiciliu:', value="România", key='as1_tara_dom', placeholder='e.g. România', max_chars=None)

    col1, col2, col3, col4, col5, col6, col7 = st.columns([0.12, 0.13, 0.065, 0.18, 0.245, 0.13, 0.13], gap="small")
    as1_cnp = col1.text_input('CNP:', key='as1_cnp', max_chars=13)
    as1_tip_act = col2.selectbox('Tip act identitate:', ("CI", "Pașaport", "Permis de ședere"), key='as1_tip_act', index=0, help=None)
    as1_serie_act = col3.text_input('Serie:', value="", key='as1_serie_act', placeholder='', max_chars=None)
    as1_nr_act = col4.text_input('Nr.:', value="", key='as1_nr_act', placeholder='', max_chars=None)
    as1_act_elib_d = col5.text_input('Eliberat de:', value="", key='as1_act_elib_d', placeholder='e.g. SPCLEP BRAȘOV', max_chars=None)
    as1_data_elib = col6.date_input('Data eliberare:', datetime.date.today(), key='as1_data_elib', help=None, format="DD.MM.YYYY", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 1, 1))
    as1_data_exp = col7.date_input('Data expirare:', datetime.date.today(), key='as1_data_exp', help=None, format="DD.MM.YYYY", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 1, 1))

    st.divider()



    










