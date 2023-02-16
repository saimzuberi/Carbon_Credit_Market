# Carbon Credit Coin - CCGA

## Description 
Tokenization of carbon credits refers to the process of representing carbon credits as digital tokens on a blockchain network. Each token represents one carbon credit and contains information about the credit, such as its origin, certification, and ownership.

By tokenizing carbon credits, it becomes easier to track and transfer them on a blockchain network. The use of blockchain technology ensures transparency and security in the trading of carbon credits, making it more efficient and trustworthy. Additionally, the use of blockchain technology can also reduce transaction costs and streamline the process of verifying and transferring carbon credits.

Overall, tokenization of carbon credits is seen as a promising solution to help reduce greenhouse gas emissions and combat climate change by creating a more transparent and efficient marketplace for carbon credits.

![Alt text](/CarbonCredit/Images/carbon_credit_lifecycle.png "Carbon Credit lifecycle")

Carbon credit tokens can be either fungible or non-fungible, depending on how they are designed.

Fungible tokens are interchangeable with each other, meaning that any token can be exchanged for any other token of the same type and value. This means that each token is identical in terms of value and characteristics, and there is no distinction between them.

In the case of carbon credit tokens, if they are designed as fungible tokens, then each token would represent an equal and interchangeable unit of carbon credit. For example, one token representing a metric ton of carbon dioxide equivalent (CO2e) emissions reduction would be interchangeable with any other token representing the same amount of CO2e emissions reduction.

On the other hand, non-fungible tokens (NFTs) are unique and cannot be exchanged for another token of the same type and value. Each NFT has a unique identification number and distinct attributes that differentiate it from other tokens. In the case of carbon credit tokens, if they are designed as non-fungible tokens, each token would represent a unique carbon credit with specific characteristics and provenance.

Overall, whether carbon credit tokens are fungible or non-fungible depends on their specific design and the use case they are intended for.

Based on this hypothese, i have build 3 systems. 
### a. Company Registeration System

The Company Registeration System allows for companies to come onboard and register themselves along with their carbon credits and are saved on the etherum block chain using ERC 721 tokeniztion (non fungible token)

![Alt text](/CarbonCredit/Images/Company%20Registeration%20System.png "Project Registeration System")

### b. Carbon Credit Audit System

The Audit system allow us to grade the provided carbon credit based on the criteria established and store the information along the company's provided carbon credit. 

This is analysis is currently being done on manual basis (check list taken from Canadian Carbon Credit Standard) but the future enhancement of this would include an AI based model to review and recommend the grade of the carbon credit. 

![Alt text](/CarbonCredit/Images/NSB%20Apprisal%20System.png "Project Apprisal System")

### c. Carbon Market 

The Carbon Credit Market is a combination of 
a. CCGACoin
b. CCGA Crowdsale
c. Carbon Credit Deployer 
d. Application allowing for purchase of carbon credit at fixed rate of 5 wei/carbon credit. 

![Alt text](/CarbonCredit/Images/Market_Place.png "Market Place")

### Business Model
The business model has been developed to take 2% commision on purchase of carbon credits coin 

# Requirment 

        Pillow==9.4.0
        python-dotenv==0.21.1
        streamlit==1.15.2
        web3==5.17.0

## Components
        Remix
        Ganache

##  Parameter Setup
The following parameters are required in .env file. 

        a. WEB3_PROVIDER_URI = address of ganache
        b. SMART_CONTRACT_ADDRESS = address of NFT Contract
        c. CROWDSALE_SMART_CONTRACT = Carbon Coin Crowdsale Contract Address
        d. MINTER_SMART_CONTRACT = Minter contract address




