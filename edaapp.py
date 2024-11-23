import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# Load the dataset with a specified encoding
data = pd.read_csv('cleaned_data_2024.csv', encoding='latin1')

# Page 1: Dashboard
def dashboard():
    st.image('logo.PNG', use_column_width=True)

    st.subheader("💡 Abstract:")

    inspiration = '''
    The Edmonton Food Drive, organized by the Church of Jesus Christ of Latter Day Saints seeks to bring the community together in a shared effort to care for those in need. Through the generosity of donations and the compassion of volunteers, they aim to provide essential food to families facing difficult times.
    Through this project we discovered how technology tools can be utilised to improve decision making processes and add value to lifes'''
    

    st.write(inspiration)

    st.subheader("👨🏻‍💻 What our Project Does?")

    what_it_does = '''
    The Edmonton Food Drive project initiative leverages machine learning to streamline the management of food donations in Edmonton Alberta. Its goal is to enhance the efficiency of drop off and pick up operations and optimize resource allocation leading to a more effective and impactful food drive campaign.
    '''

    st.write(what_it_does)


# Page 2: Exploratory Data Analysis (EDA)
def exploratory_data_analysis():
    st.title("Exploratory Data Analysis")
    # Rename columns for clarity
    data_cleaned = data.rename(columns={
        'date': 'Date',
        'drop_off_location': 'Location',
        'stake': 'Stake',
        'route_number/name': 'Route number',
        'time_spent_collecting_donations': 'Time to Complete (min)',
        '#_of_adult_volunteers_who_participated_in_this_route': 'Number of Adult Volunteers',
        '#_of_youth_volunteers_who_participated_in_this_route': 'Number of Youth Volunteers',
        '#_of_doors_in_route': 'Number of Doors in Route',
        '#_of_donation_bags_collected': 'Donation Bags Collected',
        'did_you_complete_more_than_one_route': 'How many routes did you complete',
        'Number of routes completed': 'Routes Completed',
        'ward': 'Ward',
        'Form Completion Time': 'Form Completion Time',
        'Total volunteers': 'Total Volunteers'
      
    })

    # Visualize the distribution of numerical features using Plotly
    fig = px.histogram(data_cleaned, x='Number of Adult Volunteers', nbins=20, labels={'Number of Adult Volunteers': 'Adult Volunteers'})
    st.plotly_chart(fig)

    fig = px.histogram(data_cleaned, x='Number of Youth Volunteers', nbins=20, labels={'Number of Youth Volunteers': 'Youth Volunteers'})
    st.plotly_chart(fig)

    fig = px.histogram(data_cleaned, x='Donation Bags Collected', nbins=20, labels={'Donation Bags Collected': 'Donation Bags Collected'})
    st.plotly_chart(fig)

    fig = px.histogram(data_cleaned, x='Time to Complete (min)', nbins=20, labels={'Time to Complete (min)': 'Time to Complete'})
    st.plotly_chart(fig)

# Page 3: Machine Learning Modeling
def machine_learning_modeling():
    st.title("Machine Learning Modeling")
    st.write("Enter the details to predict donation bags:")

    # Input fields for user to enter data
    # completed_routes = st.slider("Completed More Than One Route", 0, 1, 0)
    routes_completed = st.slider("Routes Completed", 1, 10, 5)
    time_spent = st.slider("Time Spent (minutes)", 10, 300, 60)
    adult_volunteers = st.slider("Number of Adult Volunteers", 1, 50, 10)
    doors_in_route = st.slider("Number of Doors in Route", 10, 500, 100)
    youth_volunteers = st.slider("Number of Youth Volunteers", 1, 50, 10)

    # Predict button
    if st.button("Predict"):
        # Load the trained model
        #model = joblib.load('random_forest_classifier_model.pkl')
        model = joblib.load('best_model.sav')
        
        # Prepare input data for prediction
        input_data = [[routes_completed, time_spent, adult_volunteers, doors_in_route, youth_volunteers]]

        # Make prediction
        prediction = model.predict(input_data)

        # Display the prediction
        st.success(f"Predicted Donation Bags: {prediction[0]}")

        # You can add additional information or actions based on the prediction if needed
# Page 4: Neighbourhood Mapping
# Read geospatial data





# Page 5: Data Collection
def data_collection():
    st.title("Data Collection")
    st.write("Please fill out the Google form to contribute to our Food Drive!")
    google_form_url = "https://forms.gle/Sif2hH3zV5fG2Q7P8"#YOUR_GOOGLE_FORM_URL_HERE
    st.markdown(f"[Fill out the form]({google_form_url})")

# Main App Logic
def main():
    st.sidebar.title("Food Drive App")
    app_page = st.sidebar.radio("Select a Page", ["Dashboard", "EDA", "ML Modeling", "Neighbourhood Mapping", "Data Collection"])

    if app_page == "Dashboard":
        dashboard()
    elif app_page == "EDA":
        exploratory_data_analysis()
    elif app_page == "ML Modeling":
        machine_learning_modeling()
    elif app_page == "Data Collection":
        data_collection()

if __name__ == "__main__":
    main()
