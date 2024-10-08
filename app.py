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
    col1, col2, col3, col4 = st.columns(4, gap="small")
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

    col1, col2, col3, col4 = st.columns(4, gap="small")
    companie = col1.text_input('Companie', value="", key='companie', placeholder='e.g. ADAKRON (fără "SRL")', max_chars=None, help='nu adaugati "SRL"')
    rez_denum = col2.text_input('Rezervare denumire:', value="", key='rez_denum', placeholder='', max_chars=None)

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([0.24, 0.24, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08], gap="small")
    loc_sed = col1.text_input('Localitate sediu', key='loc_sed', placeholder='e.g. BRAȘOV')
    str_sed = col2.text_input('Strada', key='str_sed', placeholder='e.g. NICOLAE LABIȘ')
    nr_sed = col3.text_input('Nr.', key='nr_sed', placeholder='xx')
    bl_sed = col4.text_input('Bl.', key='bl_sed', placeholder='xx')
    sc_sed = col5.text_input('Sc.', key='sc_sed', placeholder='xx')
    et_sed = col6.text_input('Et.', key='et_sed', placeholder='xx')
    ap_sed = col7.text_input('Ap.', key='ap_sed', placeholder='xx')
    cam_sed = col8.text_input('Camera/birou', key='cam_sed', placeholder='xx')

    col1, col2, col3, col4 = st.columns(4, gap="small")
    jud_sed = col1.text_input('Județ', key='jud_sed', placeholder='e.g. BRAȘOV')
    tara_sed = col2.text_input('Țara sediu:', value="România", key='tara_sed', placeholder='e.g. România', max_chars=None)

    st.divider()

    col1, col2, col3, col4 = st.columns(4, gap="small")
    cap_soc = col1.text_input('Capital social:', value="200", key='cap_soc')
    ap_num = col2.text_input('Aport numerar:', value="200", key='ap_num')
    parti_soc = col3.text_input('Părti sociale:', value="20", key='parti_soc')
    val_nom = col4.text_input('Valoare nominala:', value="10", key='val_nom')

    st.divider()

    col1, col2, col3, col4 = st.columns(4, gap="small")
    data_semn = col1.date_input('Data semnare:', datetime.date.today(), key='data_semn', help=None, format="DD.MM.YYYY", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 1, 1))

    st.divider()

    st.subheader('Contract de comodat')
    col1, col2, col3, col4 = st.columns(4, gap="small")
    nr_contr = col1.text_input('Nr. contract comodat', value="", key='nr_contr', placeholder='xx', max_chars=None, help='')
    per_comod = col2.text_input('Perioada comodat', value="", key='per_comod', placeholder='xx', max_chars=None, help='')

    st.divider()

    st.subheader('Declaratie sediu social')
    col1, col2, col3, col4 = st.columns(4, gap="small")
    cal_subsemn = col1.selectbox('Calitate subsemnat:', ("Asociat unic și administrator", "Asociat unic", "Asociat", "Administrator"), key='cal_subsemn', index=0, help=None)
    jud_trib = col2.text_input('Județ tribunal:', value="", key='jud_trib', placeholder='e.g. BRAȘOV', max_chars=None)

    st.divider()

    st.subheader('Obiectul de activitate al societății')
    col1, col2, col3, col4 = st.columns([0.505, 0.25, 0.125, 0.125], gap="small")
    dom_activ = col1.text_input('Domeniu de activiate:', value="", key='dom_activ', placeholder='e.g. xxxxxxxxxxxxxx', max_chars=None, help='')
    cod_dom = col2.text_input('Cod:', value="", key='cod_dom', placeholder='e.g. xxxxxxxxxxxxxx', max_chars=None, help='')
    col1, col2, col3, col4 = st.columns([0.505, 0.25, 0.125, 0.125], gap="small")
    activ_princip = col1.text_input('Activitate principală:', value="", key='activ_princip', placeholder='e.g. xxxxxxxxxxxxxx', max_chars=None, help='')
    cod_activ_p = col2.text_input('Cod:', value="", key='cod_activ_p', placeholder='e.g. xxxxxxxxxxxxxx', max_chars=None, help='')





