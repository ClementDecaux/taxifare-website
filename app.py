import streamlit as st
from datetime import datetime
import requests as rq


url = 'https://taxifare-api-x86-ax5ukvkh2q-ew.a.run.app'




date_input = st.date_input('Date', value=None, min_value=None, max_value=None,
                              key=None, help=None, on_change=None, disabled=False)

time_input = st.time_input('Time', value=None, key=None, help=None, on_change=None, disabled=False)

passenger_count = st.number_input('Passenger Count', 0, 10, 1)

pickup_time = datetime.combine(date_input, time_input)

data_new = dict(pickup_datetime=[pickup_time],
                pickup_longitude=[40.7614327],
                pickup_latitude=[-73.9798156],
                dropoff_longitude=[40.6513111   ],
                dropoff_latitude=[-73.8803331],
                passenger_count=[passenger_count])

if st.button('click me'):
    response = rq.get(f'{url}/predict', params=data_new)
    st.write(response.content)
