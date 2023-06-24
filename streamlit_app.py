import streamlit
import pandas
import requests
import snowflake.connector 
from urllib.error import URLError 


streamlit.title("My healthy dinner")

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 🥑🍞Hard-Boiled Free-Range Egg')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Honeydew'])
fruit_show = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruit_show)



def get_fruitvice_data(this_fruit_choice):

    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return  fruityvice_normalized


streamlit.header("Fruity Fruit Advice")
try:
    fruit_choice = streamlit.text_input('What fruit wud you like info about ?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information")
    else:  
        back_from_function = get_fruitvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
  
except URLError as e:
  streamlit.error()
      

#streamlit.write('The user entered ', fruit_choice)



#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

## asked to delete streamlit.text(fruityvice_response.json())


# write your own comment -what does the next line do? 

# write your own comment - what does this do?



streamlit.write('The user entered ', fruit_choice)

streamlit.stop()



"""
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit list contains :")
streamlit.dataframe(my_data_rows)
"""
streamlit.header("The fruit list contains :")
# snowflake related function 
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from fruit_load_list")
       return my_cur.fetchall()
# Add a button to load fruit list 
if streamlit.button('Get Fruit Load List'):
	my_cnx = 	snowflake.connector.connect(**streamlit.secrets["snowflake"])
	my_data_rows = get_fruit_load_list()
	streamlit.dataframe(my_data_rows)

fruit_choice2 = streamlit.text_input('What fruit would you like to add ?','  ')

#streamlit.write('Thanks for adding', fruit_choice2)


#my_cur.execute("insert into fruit_load_list values ('from streamlit')");





