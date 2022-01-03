from datetime import datetime
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# st.title('서울교통공사 지하철 월별 하차 인원')


df = pd.read_csv('./monthly_subway_statistics_in_seoul.csv', encoding='cp949')
df.index = df['연번']
if st. button('data copyright link'):
    st.write('https://www.data.go.kr/data/15044247/fileData.do')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

# st.subheader('2021 역별 하차 인원')
option = st.selectbox(
    'Select Line', 
    (df['역명']))

station_data = df.loc[(df['역명']==option)]

station_data = station_data[station_data.columns.difference(['연번', '호선', '역번호', '역명'])]
s_index = station_data.index.tolist()
st.line_chart(station_data.loc[s_index[0]], use_container_width=True)


# st.subheader('2호선 월별 하차 인원')




# st.subheader('호선별 하차 수')
# line_data = data.groupby('호선').sum()
# line_data['sum_line'] = line_data.iloc[4:].sum(axis=1)
# print(line_data)

# hist_values = np.histogram(line_data['sum_line'], bins=9, range=(1,10))
# st.bar_chart(hist_values)

# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)