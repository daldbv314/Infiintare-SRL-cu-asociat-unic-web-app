import os
import io
import datetime
import streamlit as st
from zipfile import ZipFile
from pathlib import Path
from docxtpl import DocxTemplate
from dotenv import load_dotenv
from io import BytesIO
import locale

locale.setlocale(locale.LC_ALL, 'ro_RO')

def main():

    st.set_page_config(
        page_title='Înfiintare', 
        layout='wide',
    )
    st.title('Creează actele pentru înființare SRL cu asociat unic:')


        #--- HIDE STREAMLIT STYLE ---
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)



    def var_dictionary():
        var_dict = {
            'as1_nume': as1_nume,
            'as1_prenume': as1_prenume,
            'as1_cetatean': as1_cetatean,
            'as1_data_n': as1_data_n,
            'as1_loc_n': as1_loc_n,
            'as1_jud_n': as1_jud_n,
            'as1_tara_n': as1_tara_n,
            'as1_loc_dom': as1_loc_dom,
            'as1_str_dom': as1_str_dom,
            'as1_nr_dom': as1_nr_dom,
            'as1_bl_dom': as1_bl_dom,
            'as1_sc_dom': as1_sc_dom,
            'as1_et_dom': as1_et_dom,
            'as1_ap_dom': as1_ap_dom,
            'as1_jud_dom': as1_jud_dom,
            'as1_tara_dom': as1_tara_dom,
            'as1_cnp': as1_cnp,
            'as1_tip_act': as1_tip_act,
            'as1_serie_act': as1_serie_act,
            'as1_nr_act': as1_nr_act,
            'as1_act_elib_d': as1_act_elib_d,
            'as1_data_elib': as1_data_elib,
            'as1_data_exp': as1_data_exp,
            'companie': companie,
            'rez_denum': rez_denum,
            'loc_sed': loc_sed,
            'str_sed': str_sed,
            'nr_sed': nr_sed,
            'bl_sed': bl_sed,
            'sc_sed': sc_sed,
            'et_sed': et_sed,
            'ap_sed': ap_sed,
            'cam_sed': cam_sed,
            'jud_sed': jud_sed,
            'tara_sed': tara_sed,
            'cap_soc': cap_soc,
            'ap_num': ap_num,
            'parti_soc': parti_soc,
            'val_nom': val_nom,
            'data_semn': data_semn,
            'dsz1': dsz1,
            'dsz2': dsz2,
            'dsl1': dsl1,
            'dsl2': dsl2,
            'dsa1': dsa1,
            'dsa2': dsa2,
            'dsa3': dsa3,
            'dsa4': dsa4,
            'nr_contr': nr_contr,
            'per_comod': per_comod,
            'cal_subsemn': cal_subsemn,
            'jud_trib': jud_trib,
            'cod_caen': cod_caen,
            'dom_activ': dom_activ,
            'cod_activ_p': cod_activ_p,
            'activ_princip': activ_princip,
            'cod_activ_s1': cod_activ_s1,
            'activ_sec1': activ_sec1,
            'cod_activ_s2': cod_activ_s2,
            'activ_sec2': activ_sec2,
            'cod_activ_s3': cod_activ_s3,
            'activ_sec3': activ_sec3,
            'cod_activ_s4': cod_activ_s4,
            'activ_sec4': activ_sec4,
            'cod_activ_s5': cod_activ_s5,
            'activ_sec5': activ_sec5,
            'cod_activ_s6': cod_activ_s6,
            'activ_sec6': activ_sec6,
            'cod_activ_s7': cod_activ_s7,
            'activ_sec7': activ_sec7,
            'cod_activ_s8': cod_activ_s8,
            'activ_sec8': activ_sec8,
            'cod_activ_s9': cod_activ_s9,
            'activ_sec9': activ_sec9,
            'cod_activ_s10': cod_activ_s10,
            'activ_sec10': activ_sec10,
            'cod_activ_s11': cod_activ_s11,
            'activ_sec11': activ_sec11,
            'cod_activ_s12': cod_activ_s12,
            'activ_sec12': activ_sec12,
            'cod_activ_s13': cod_activ_s13,
            'activ_sec13': activ_sec13,
            'cod_activ_s14': cod_activ_s14,
            'activ_sec14': activ_sec14,
            'cod_activ_s15': cod_activ_s15,
            'activ_sec15': activ_sec15,
            'cod_activ_s16': cod_activ_s16,
            'activ_sec16': activ_sec16,
            'cod_activ_s17': cod_activ_s17,
            'activ_sec17': activ_sec17,
            'cod_activ_s18': cod_activ_s18,
            'activ_sec18': activ_sec18,
            'cod_activ_s19': cod_activ_s19,
            'activ_sec19': activ_sec19,
            'cod_activ_s20': cod_activ_s20,
            'activ_sec20': activ_sec20,
            'impoz_prof_bool': impoz_prof_bool,
            'impoz_prof': impoz_prof,
            'impoz_prof_data': impoz_prof_data,
            'ipz1': ipz1,
            'ipz2': ipz2,
            'ipl1': ipl1,
            'ipl2': ipl2,
            'ipa1': ipa1,
            'ipa2': ipa2,
            'ipa3': ipa3,
            'ipa4': ipa4,
            'per_fisc_i_p': per_fisc_i_p,
            'pfipT': pfipT,
            'pfipA': pfipA,
            'impoz_venit_m': impoz_venit_m,
            'ivz1': ivz1,
            'ivz2': ivz2,
            'ivl1': ivl1,
            'ivl2': ivl2,
            'iva1': iva1,
            'iva2': iva2,
            'iva3': iva3,
            'iva4': iva4,
            'tva': tva,
            'cae1': cae1,
            'cae2': cae2,
            'cae3': cae3,
            'cae4': cae4,
            'cae5': cae5,
            'cae6': cae6,
            'cae7': cae7,
            'cae8': cae8,
            'scop_tva': scop_tva,
            'reg_norm_tva': reg_norm_tva,
            'per_fisc_tva': per_fisc_tva,
            'pftL': pftL,
            'pftT': pftT
            
        }

        return var_dict    

    def doc01():
        doc01_path = Path.cwd() / "Templates" / "01-Act-constitutiv-(asociat-unic)-template-v2.docx"
        doc01_doc = DocxTemplate(doc01_path)
        context = var_dictionary()
        doc01_doc.render(context)
        doc01_bytes = BytesIO()
        doc01_doc.save(doc01_bytes)
        return doc01_bytes.getvalue()

    def doc02():
        doc02_path = Path.cwd() / "Templates" / "02-Anexa_1_inregistrare_fiscala-template-v2.docx"
        doc02_doc = DocxTemplate(doc02_path)
        context = var_dictionary()
        doc02_doc.render(context)
        doc02_bytes = BytesIO()
        doc02_doc.save(doc02_bytes)
        return doc02_bytes.getvalue()

    def doc03():
        doc03_path = Path.cwd() / "Templates" / "03-Anexa_2_investitie_straina-v2.docx"
        doc03_doc = DocxTemplate(doc03_path)
        context = var_dictionary()
        doc03_doc.render(context)
        doc03_bytes = BytesIO()
        doc03_doc.save(doc03_bytes)
        return doc03_bytes.getvalue()

    def doc04():
        doc04_path = Path.cwd() / "Templates" / "04-Contract-comodat-sediu-social(asociat-unic)-template-v2.docx"
        doc04_doc = DocxTemplate(doc04_path)
        context = var_dictionary()
        doc04_doc.render(context)
        doc04_bytes = BytesIO()
        doc04_doc.save(doc04_bytes)
        return doc04_bytes.getvalue()

    def doc05():
        doc05_path = Path.cwd() / "Templates" / "05-Declaratie-indeplinire-conditii-functionare-template-v2.docx"
        doc05_doc = DocxTemplate(doc05_path)
        context = var_dictionary()
        doc05_doc.render(context)
        doc05_bytes = BytesIO()
        doc05_doc.save(doc05_bytes)
        return doc05_bytes.getvalue()

    def doc06():
        doc06_path = Path.cwd() / "Templates" / "06-Declaratie-sediu-social-template-v2.docx"
        doc06_doc = DocxTemplate(doc06_path)
        context = var_dictionary()
        doc06_doc.render(context)
        doc06_bytes = BytesIO()
        doc06_doc.save(doc06_bytes)
        return doc06_bytes.getvalue()

    def create_zip_archive():
        # Generate the content for each document
        doc01_content = doc01()
        doc02_content = doc02()
        doc03_content = doc03()
        doc04_content = doc04()
        doc05_content = doc05()
        doc06_content = doc06()


        # Create an in-memory zip file
        with io.BytesIO() as zip_buffer:
            with ZipFile(zip_buffer, 'w') as zipf:
                # Add each doc to the archive
                zipf.writestr(f"{companie}-01-Act-constitutiv-(asociat-unic)-template-v2.docx", doc01_content)
                zipf.writestr(f"{companie}-02-Anexa_1_inregistrare_fiscala-template-v2.docx", doc02_content)
                zipf.writestr(f"{companie}-03-Anexa_2_investitie_straina-v2.docx", doc03_content)
                zipf.writestr(f"{companie}-04-Contract-comodat-sediu-social(asociat-unic)-template-v2.docx", doc04_content)
                zipf.writestr(f"{companie}-05-Declaratie-indeplinire-conditii-functionare-template-v2.docx", doc05_content)
                zipf.writestr(f"{companie}-06-Declaratie-sediu-social-template-v2.docx", doc06_content)
                # Get the zip archive content as bytes
            zip_bytes = zip_buffer.getvalue()
        return zip_bytes


    with st.form("Înființare", clear_on_submit=False):
            
        st.subheader('Act constitutiv:')
        col1, col2, col3, col4 = st.columns(4, gap="small")
        as1_nume = col1.text_input('Nume Asociat:', value="", key='as1_nume', placeholder='e.g. Popescu', max_chars=None)
        as1_prenume = col2.text_input('Prenume Asociat:', value="", key='as1_prenume', placeholder='e.g. Ștefan', max_chars=None)
        as1_cetatean = col3.text_input('Cetațean:', value="român", key='as1_cetatean', placeholder='e.g. român')
        as1_data_n_tmp = col4.date_input('Data naștere:', datetime.date.today(), key='as1_data_n_tmp', help=None, format="DD.MM.YYYY", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 1, 1))
        as1_data_n = as1_data_n_tmp.strftime("%d.%m.%Y")
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
        as1_data_elib_tmp = col6.date_input('Data eliberare:', datetime.date.today(), key='as1_data_elib_tmp', help=None, format="DD.MM.YYYY", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 1, 1))
        as1_data_elib = as1_data_elib_tmp.strftime("%d.%m.%Y")
        as1_data_exp_tmp = col7.date_input('Data expirare:', datetime.date.today(), key='as1_data_exp_tmp', help=None, format="DD.MM.YYYY", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 1, 1))
        as1_data_exp = as1_data_exp_tmp.strftime("%d.%m.%Y")

        st.divider()

        col1, col2, col3, col4 = st.columns(4, gap="small")
        companie = col1.text_input('Denumire companie:', value="", key='companie', placeholder='e.g. ADAKRON (fără "SRL")', max_chars=None, help='nu adaugati "SRL"')
        rez_denum = col2.text_input('Numar și dată rezervare denumire:', value="", key='rez_denum', placeholder='', max_chars=None)

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
        data_semn_tmp = col1.date_input('Data semnare:', datetime.date.today(), key='data_semn_tmp', help=None, format="DD.MM.YYYY", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 1, 1))
        data_semn = data_semn_tmp.strftime("%d.%m.%Y")

        st.divider()

        st.subheader('Contract de comodat')
        col1, col2, col3, col4 = st.columns(4, gap="small")
        nr_contr = col1.text_input('Nr. contract comodat', value="", key='nr_contr', placeholder='99', max_chars=None, help='')
        per_comod = col2.text_input('Perioada comodat', value="", key='per_comod', placeholder='99', max_chars=None, help='Adaugati doar numarul. e.g. 99')

        st.divider()

        st.subheader('Declaratie sediu social')
        col1, col2, col3, col4 = st.columns(4, gap="small")
        cal_subsemn = col1.selectbox('Calitate subsemnat:', ("Asociat unic și administrator", "Asociat unic", "Asociat", "Administrator"), key='cal_subsemn', index=0, help=None)
        jud_trib = col2.text_input('Județ tribunal:', value="", key='jud_trib', placeholder='e.g. BRAȘOV', max_chars=None)

        st.divider()

        st.subheader('Obiectul de activitate al societății')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_caen = col1.text_input('Cod CAEN:', value="", key='cod_caen', placeholder='e.g. 620', max_chars=3, help='')
        dom_activ = col2.text_input('Domeniu de activiate:', value="", key='dom_activ', placeholder='e.g. Activități de servicii in tehnologia informației', max_chars=None, help='')

        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_p = col1.text_input('Cod CAEN:', value="", key='cod_activ_p', placeholder='e.g. 6201', max_chars=4, help='')
        activ_princip = col2.text_input('Activitate principală:', value="", key='activ_princip', placeholder='e.g. Activități de realizare a soft-ului la comandă (software orientat client)', max_chars=None, help='')

        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s1 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s1', placeholder='e.g. 6202', max_chars=4, help='')   
        activ_sec1 = col2.text_input('Activitate secundară:', value="", key='activ_sec1', placeholder='e.g. Activități de consultanță in tehnologia informației', max_chars=None, help='')    
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s2 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s2', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')   
        activ_sec2 = col2.text_input('Activitate secundară:', value="", key='activ_sec2', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')    
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s3 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s3', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')   
        activ_sec3 = col2.text_input('Activitate secundară:', value="", key='activ_sec3', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')   
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s4 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s4', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')   
        activ_sec4 = col2.text_input('Activitate secundară:', value="", key='activ_sec4', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')   
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s5 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s5', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')   
        activ_sec5 = col2.text_input('Activitate secundară:', value="", key='activ_sec5', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')   
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s6 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s6', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')   
        activ_sec6 = col2.text_input('Activitate secundară:', value="", key='activ_sec6', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s7 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s7', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')   
        activ_sec7 = col2.text_input('Activitate secundară:', value="", key='activ_sec7', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s8 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s8', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec8 = col2.text_input('Activitate secundară:', value="", key='activ_sec8', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s9 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s9', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec9 = col2.text_input('Activitate secundară:', value="", key='activ_sec9', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s10 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s10', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec10 = col2.text_input('Activitate secundară:', value="", key='activ_sec10', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s11 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s11', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec11 = col2.text_input('Activitate secundară:', value="", key='activ_sec11', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s12 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s12', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec12 = col2.text_input('Activitate secundară:', value="", key='activ_sec12', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s13 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s13', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec13 = col2.text_input('Activitate secundară:', value="", key='activ_sec13', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s14 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s14', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec14 = col2.text_input('Activitate secundară:', value="", key='activ_sec14', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s15 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s15', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec15 = col2.text_input('Activitate secundară:', value="", key='activ_sec15', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s16 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s16', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec16 = col2.text_input('Activitate secundară:', value="", key='activ_sec16', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s17 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s17', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec17 = col2.text_input('Activitate secundară:', value="", key='activ_sec17', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s18 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s18', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec18 = col2.text_input('Activitate secundară:', value="", key='activ_sec18', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s19 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s19', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec19 = col2.text_input('Activitate secundară:', value="", key='activ_sec19', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')
        col1, col2, col3, col4 = st.columns([0.25, 0.505, 0.125, 0.125], gap="small")
        cod_activ_s20 = col1.text_input('Cod CAEN:', value="", key='cod_activ_s20', label_visibility='collapsed', placeholder='e.g. xxxx', max_chars=4, help='')
        activ_sec20 = col2.text_input('Activitate secundară:', value="", key='activ_sec20', label_visibility='collapsed', placeholder='e.g. xxxxxxxxxxxxxxxxxxxx', max_chars=None, help='')

        st.divider()

        st.subheader('Anexa 1: cerere de înregistrare fiscală')

        col1, col2, col3, col4 = st.columns(4, gap="small")
        impoz_prof_bool = col1.checkbox("Impozit Profit")
        impoz_prof_data_tmp = col2.date_input('Incepând cu:', datetime.date.today(), key='impoz_prof_data_tmp', help=None, format="DD.MM.YYYY", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 1, 1))
        impoz_prof_data = impoz_prof_data_tmp.strftime("%d.%m.%Y")
        per_fisc_i_p = col3.selectbox('Perioada fiscală:', ("Trimestrială", "Anuală"), key='per_fisc_i_p', index=None, help=None)

        st.divider()

        col1, col2, col3, col4 = st.columns(4, gap="small")
        impoz_venit_m_bool = col1.checkbox("Impozit venit micro")
        impoz_venit_m_data_tmp = col2.date_input('Incepând cu:', datetime.date.today(), key='impoz_venit_m_data_tmp', help=None, format="DD.MM.YYYY", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 1, 1))
        impoz_venit_m_data = impoz_venit_m_data_tmp.strftime("%d.%m.%Y")

        st.divider()

        col1, col2, col3, col4 = st.columns(4, gap="small")
        tva_bool = col1.checkbox("TVA")
        c_a_est = col2.number_input('Cifra de afaceri estimată:', key='c_a_est', min_value=0, max_value=99999999, label_visibility="visible", help='în LEI')
        col1, col2, col3, col4 = st.columns(4, gap="small")
        scop_tva_bool = col1.checkbox("Înregistrare în scopuri de TVA")
        reg_norm_tva_bool = col2.checkbox("Aplicarea regimului normal de TVA")
        per_fisc_tva = col3.selectbox('Perioada fiscală:', ("Lunară", "Trimestrală"), key='per_fisc_tva', index=None, help=None)

        st.divider()

        st.write(' ')
        submitted = st.form_submit_button("Pas 1: Crează documentele", type="primary")

    if submitted:
            with st.spinner("Se generează documentele..."):
                clean_data_semn = str(data_semn).replace('.', '')
                dsz1 = clean_data_semn[0]
                dsz2 = clean_data_semn[1]
                dsl1 = clean_data_semn[2]
                dsl2 = clean_data_semn[3]
                dsa1 = clean_data_semn[4]
                dsa2 = clean_data_semn[5]
                dsa3 = clean_data_semn[6]
                dsa4 = clean_data_semn[7]

                if impoz_prof_bool:
                    impoz_prof = 'X'
                else:
                    impoz_prof = ''
                
                clean_impoz_prof_data = str(impoz_prof_data).replace('.', '')
                ipz1 = clean_impoz_prof_data[0]
                ipz2 = clean_impoz_prof_data[1]
                ipl1 = clean_impoz_prof_data[2]
                ipl2 = clean_impoz_prof_data[3]
                ipa1 = clean_impoz_prof_data[4]
                ipa2 = clean_impoz_prof_data[5]
                ipa3 = clean_impoz_prof_data[6]
                ipa4 = clean_impoz_prof_data[7]

                if per_fisc_i_p == 'Trimestrială':
                    pfipT = 'X'
                else:
                    pfipT = ''
                if per_fisc_i_p == 'Anuală':
                    pfipA = 'X'
                else:
                    pfipA = ''            


                if impoz_venit_m_bool:
                    impoz_venit_m = 'X'
                else:
                    impoz_venit_m = ''

                clean_impoz_venit_m_data = str(impoz_venit_m_data).replace('.', '')
                ivz1 = clean_impoz_venit_m_data[0]
                ivz2 = clean_impoz_venit_m_data[1]
                ivl1 = clean_impoz_venit_m_data[2]
                ivl2 = clean_impoz_venit_m_data[3]
                iva1 = clean_impoz_venit_m_data[4]
                iva2 = clean_impoz_venit_m_data[5]
                iva3 = clean_impoz_venit_m_data[6]
                iva4 = clean_impoz_venit_m_data[7]

                if tva_bool:
                    tva = 'X'
                else:
                    tva = ''

                # Reverse the string to start from the last digit
                c_a_est_reversed = str(c_a_est)[::-1]
                # Maximum number of variables (cae1 to cae8)
                cae_max_length = 8
                cae1 = cae2 = cae3 = cae4 = cae5 = cae6 = cae7 = cae8 = None
                # Dynamically assign digits to the variables
                for i in range(cae_max_length):
                    var_name = f"cae{i+1}"
                    if i < len(c_a_est_reversed):
                        # Assign the corresponding digit if it exists
                        globals()[var_name] = int(c_a_est_reversed[i])  # Use globals to create variable
                    else:
                        # Assign an empty string if there are no more digits
                        globals()[var_name] = ''
                # At this point, the variables cae1, cae2, ..., cae8 are defined and can be used

                if scop_tva_bool:
                    scop_tva = 'X'
                else:
                    scop_tva = ''

                if reg_norm_tva_bool:
                    reg_norm_tva = 'X'
                else:
                    reg_norm_tva = ''

                if per_fisc_tva == 'Lunară':
                    pftL = 'X'
                else:
                    pftL = ''

                if per_fisc_tva == 'Trimestrală':
                    pftT = 'X'
                else:
                    pftT = ''
                
                zip_archive = create_zip_archive()
            st.success("Succes! Documentele pot fi descărcate acum de mai jos!")
            st.download_button(label="Pas 2: Downloadează", data=zip_archive, file_name=f"{companie}-acte-înființare-SRL-{datetime.date.today()}.zip", mime="docx", type="primary")

if __name__ == "__main__":
    main()
