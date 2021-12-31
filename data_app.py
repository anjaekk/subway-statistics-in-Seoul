from datetime import datetime
import streamlit as st
import pandas as pd
import numpy as np

st.title('서울교통공사 지하철 월별 하차 인원')


@st.cache
def load_data(nrows):
    df = pd.read_csv('./monthly_subway_statistics_in_seoul.csv', encoding='cp949', nrows=nrows)
    return df

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('호선별 하차 수')
line_data = data.groupby('호선').sum()
line_data['sum_line'] = line_data.iloc[4:].sum(axis=1)
print(line_data)

hist_values = np.histogram(line_data['sum_line'], bins=9, range=(1,10))
st.bar_chart(hist_values)

# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)