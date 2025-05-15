import requests
import streamlit as st
import pandas as pd


st.title("PINCODE SEARCH")

pin=st.text_input("Enter the pin code")

if pin:
    url=f"https://api.postalpincode.in/pincode/{pin}"
    try:
        response=requests.get(url)
        if response.status_code==200:
            data=response.json()
            if data[0]['Status']=='Success':
                selected=st.selectbox("Select What you want", options=[
                    'Post Office Name', 'BranchType', 'Delivery Status', 'State', 'District'])

                post_offices=data[0]['PostOffice']

                if selected=="Post Office Name":
                    st.subheader("Post Office Name")
                    names=[po['Name'] for po in post_offices]
                    st.write(pd.DataFrame(names, columns=["Post Office Name"]))

                elif selected=="BranchType":
                    st.subheader("Post Office Name & Branch Type")
                    branch=[{'Post Office Name': po['Name'], 'Branch Type': po['BranchType']} for po in post_offices]
                    st.write(pd.DataFrame(branch))

                elif selected=="Delivery Status":
                    st.subheader("Delivery Status")
                    deliverystatus=[{'Post Office Name': po['Name'], 'Delivery Status': po['DeliveryStatus']} for po in post_offices]
                    st.write(pd.DataFrame(deliverystatus))

                elif selected=="State":
                    st.subheader("State")
                    states=[{'Post Office Name': po['Name'], 'State': po['State']} for po in post_offices]
                    st.write(pd.DataFrame(states))

                elif selected=="District":
                    st.subheader("District")
                    districts=[{'Post Office Name': po['Name'], 'District': po['District']} for po in post_offices]
                    st.write(pd.DataFrame(districts))

            else:
                st.error("No data found for this pincode or invalid pincode.")
        else:
            st.error(f"Failed to fetch data. HTTP status code:{response.status_code}")
    except Exception as e:
        st.error(f"An error occurred:{e}")
