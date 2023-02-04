import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
from PIL import Image

load_dotenv(Path('SAMPLE.env'))

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/artregistry_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract


# Load the contract
contract = load_contract()
# Load Header File 
header = Image.open('contracts/Images/_Header.jpeg')
st.image(header, caption='HeaderFile')

st.title("Carbon Credit Appraisal System")
st.write("Choose your account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

################################################################################
# Register New NsB Project 
################################################################################
st.markdown("## Register New Carbon Efficient Project")

artwork_name = st.text_input("Enter the name of the Project")
artist_name = st.text_input("Enter the Location")
initial_appraisal_value = st.text_input("Enter the initial expected removal of Carbon from Atmosphere")
artwork_uri = st.text_input("Enter the URI to the Project ESG Report")

if st.button("Register Project"):
    tx_hash = contract.functions.registerArtwork(
        address,
        artwork_name,
        artist_name,
        int(initial_appraisal_value),
        artwork_uri
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
st.markdown("---")


################################################################################
# Appraise Art
################################################################################
st.markdown("## Appraise NSB Project")

tokens = contract.functions.totalSupply().call()

token_id = st.selectbox("Choose an NsB Project ID", list(range(tokens)))

new_appraisal_value = st.text_input("Estimate of GHG reductions")

new_NSP_summary = st.text_input('''Enter Category a. Better management of forests b. Avoiding releases of methane gas c. Action to protect forests or grasslands d. Switching to chemicals in refrigeration systems e. Composting organic waste f. Tree planting g. Capturing methane gas generated from livestock h. Increasing the amount of carbon stored in agricultural i. Using crypto mining exhust for heating purpose j. Electricity generation from Solar/bio fule  k. Others ''')
GHG_entitlement = st.text_input("Enter Entitlement Details")
land = st.text_input("Is the project on private land or '\n' Reserve land or \nIndigenous traditional territory or \nCrown Land")
baseline_senario = st.text_input("The baseline scenario (also known as the business-as-usual case) \n is a description of the activities and GHG emissions that would \n have occurred without the implementation of the offset project.")
project_senario = st.text_input("The project scenario is a description of the activities and an \n estimate of the GHG emission reductionor removals \n that will be achieved by the offset project, according to the offset protocol")
source = st.text_input("Enter process that releases GHGs into the atmosphere. \n Sources can include fuel combustion or fertilizer use.")
sink = st.text_input(" Enter process that removes GHGs from the atmosphere. \n Sinks include the capture and storage of carbon in plants, trees and soils.") 
reservoir = st.text_input(" Enter component details that has the capacity to accumulate, store and release GHGs. \n Reservoirs can include plants, trees and soils.")
additionality = st.text_input(" A project proponent will have to demonstrate that the GHG reductions \n achieved by the project would not have \n achieved by the project would \n not have occurred without the project, i.e. they are additional. ")
Leakage = st.text_input(" Leakage occurs if an activity or demand\n for the products of an activity shift to another location \n when the project is implemented. This causes increases in GHGs elsewhere.")
risk_mitigation = st.text_input ("For projects that increase the capture and storage of carbon in plants, trees, soil, or geologic formations, project proponents will need to assess the risk that the carbon will later be released into the atmosphere due to unforeseeable events.")
verification = st.text_input ("Details of how the offset project has been implemented in accordance with its protocol and the rules of the offset system.")

report_uri = new_NSP_summary + new_NSP_summary + GHG_entitlement + land + baseline_senario + project_senario + source + sink + reservoir + additionality + Leakage + risk_mitigation + verification

if st.button("Appraise NsB Project"):

    # Use the token_id and the report_uri to record the appraisal
    tx_hash = contract.functions.newAppraisal(
        token_id,
        int(new_appraisal_value),
        report_uri
    ).transact({"from": w3.eth.accounts[0]})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write(receipt)
st.markdown("---")

################################################################################
# Get Appraisals
################################################################################
st.markdown("## Get the appraisal report history")
art_token_id = st.number_input("Artwork ID", value=0, step=1)
if st.button("Get Appraisal Reports"):
    appraisal_filter = contract.events.Appraisal.createFilter(
        fromBlock=0,
        argument_filters={"tokenId": art_token_id}
    )
    appraisals = appraisal_filter.get_all_entries()
    if appraisals:
        for appraisal in appraisals:
            report_dictionary = dict(appraisal)
            st.markdown("### Appraisal Report Event Log")
            st.write(report_dictionary)
            st.markdown("### Appraisal Report Details")
            st.write(report_dictionary["args"])
    else:
        st.write("This Project has no new appraisals")
