# Import required libraries
import streamlit as st
import pandas as pd
from col_groups import comments, allowed_columns

comment_columns = comments

# Load your data into a DataFrame
df = pd.read_excel('data/AI-Survey-Results-tr.xlsx')
df2 = pd.read_excel('data/AI-Survey-Results-tr-Tools-Tasks-Complete.xlsx')

# Set the dashboard to wide mode for easier viewing
st.set_page_config(layout="wide")

# Predefined password
PASSWORD = "guild1962"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("Authentication Required")
    password = st.text_input("Enter the password", type="password")
    login_button = st.button("Login")

    if login_button:
        if password == PASSWORD:
            st.session_state["authenticated"] = True
            st.rerun()  # Immediately rerun the app to bypass the login screen
        else:
            st.error("Incorrect password. Please try again.")
else:

# Set title for the app
    st.title("2024 DGC AI Survey Explorer")

    # Add tabs to the dashboard
    tab1, tab2, tab3 = st.tabs(["Crosstab Generator", "User Comments", "Tasks, Tools & Training"])

    with tab1:
        # Initialize session state to keep track of selected columns
        if "column1" not in st.session_state:
            st.session_state["column1"] = df.columns[2]
        if "column2" not in st.session_state:
            st.session_state["column2"] = df.columns[12]

        # Dropdowns to select columns for the crosstab with default selections
        column1 = st.selectbox(
            "Select the first column",
            allowed_columns,  # Use the list of allowed columns here
            index=allowed_columns.index(st.session_state["column1"]) if st.session_state["column1"] in allowed_columns else 2,
            key="selectbox_column1"
        )

        column2 = st.selectbox(
            "Select the second column",
            allowed_columns,  # Use the list of allowed columns here
            index=allowed_columns.index(st.session_state["column2"]) if st.session_state["column2"] in allowed_columns else 12,
            key="selectbox_column2"
        )

        # Optional button to flip columns
        if st.button("Flip Crosstab Columns", key="flip_button"):
            # Swap the selected columns
            st.session_state["column1"], st.session_state["column2"] = st.session_state["column2"], st.session_state["column1"]
            column1 = st.session_state["column1"]
            column2 = st.session_state["column2"]

        # Filter out NaN values from the unique values of column1
        column1_values = df[column1].dropna().unique()
        column1_values = st.multiselect(
            f"Filter values in '{column1}' (optional)", column1_values, default=column1_values, key="multiselect_column1"
        )

        # Filter out NaN values from the unique values of column2
        column2_values = df[column2].dropna().unique()
        column2_values = st.multiselect(
            f"Filter values in '{column2}' (optional)", column2_values, default=column2_values, key="multiselect_column2"
        )

        # Checkbox to display values as percentages
        show_percentage = st.checkbox("Show as percentage", key="checkbox_percentage")

        # Dropdown to choose percentage calculation method
        percentage_method = "Row"
        if show_percentage:
            percentage_method = st.radio("Calculate percentages by", ("Row", "Column"), key="radio_percentage_method")

        # Generate the crosstab
        if st.button("Generate Crosstab", key="generate_crosstab"):
            # Filter the DataFrame based on selected values
            filtered_df = df[df[column1].isin(column1_values) & df[column2].isin(column2_values)]
            
            # Calculate the crosstab
            crosstab_result = pd.crosstab(filtered_df[column1], filtered_df[column2])

            num_rows = crosstab_result.shape[0]
            row_height = 34  # Approximate height per row in pixels
            max_height = 20000  # Set a max height to avoid overly tall tables
            calculated_height = min(max_height, num_rows * row_height + 50)  # Add buffer for header
            
            # If percentage option is selected, normalize by row or column totals based on user choice
            if show_percentage:
                if percentage_method == "Row":
                    crosstab_result = crosstab_result.div(crosstab_result.sum(axis=1), axis=0) * 100
                else:
                    crosstab_result = crosstab_result.div(crosstab_result.sum(axis=0), axis=1) * 100
                crosstab_result = crosstab_result.round(2)
                crosstab_result = crosstab_result.style.format("{:.2f}%")
            else:
                crosstab_result = crosstab_result

            # Display the crosstab with increased size
            st.write("Crosstab Result:")
            st.dataframe(crosstab_result, use_container_width=True, height=calculated_height)
            
    # Create the second tab for displaying user comments
    with tab2:
        st.header("Comments")

        # Dropdown to select the field to filter comments by
        filter_field = st.selectbox("Select a field to filter comments by", [None] + [col for col in df.columns if col not in comment_columns], key="selectbox_filter_field")
        
        # Multiselect to choose specific values in the selected field
        if filter_field:
            filter_values = st.multiselect(
                f"Select values in '{filter_field}' to filter comments",
                options=df[filter_field].dropna().unique(), key="multiselect_filter_values"
            )
            # Apply filter to the DataFrame
            filtered_df = df[df[filter_field].isin(filter_values)] if filter_values else df
        else:
            filtered_df = df  # No filter applied if no field is selected

        # Dropdown to select which comment field to display
        selected_comment_field = st.selectbox("Select a comment field to display", comment_columns, key="selectbox_comment_field")

        # Display comments from the selected comment field based on the filtered rows
        if selected_comment_field:
            st.subheader(f"Comments for '{selected_comment_field}'")
            comments = filtered_df[selected_comment_field].dropna()
            
            # Display each filtered comment as an individual item
            for idx, comment in enumerate(comments, 1):
                st.write(f"{idx}. {comment}")


    with tab3:
        st.header("AI Tools, Tasks, and Training")

        # Fixed columns for the crosstab
        column1 = "AI"
        column2 = "Response"

        # Display the columns being used for the crosstab
        st.write(f"Crosstab will be generated using the '{column1}' and '{column2}' columns.")

        # Step 1: Select a single value from the 'Type' column
        type_options = df2['Type'].dropna().unique()  # Get unique values in the 'Type' column
        selected_type = st.selectbox("Select a Type", type_options, key="selectbox_type")

        # Filter the dataframe based on the selected type
        filtered_df = df2[df2['Type'] == selected_type]

        # Step 2: Additional filter selection
        filter_columns = [col for col in filtered_df.columns if col not in [column1, column2, 'Type']]

        # Select a column to filter by
        selected_filter_column = st.selectbox("Select a column to filter by (optional)", filter_columns, key="selectbox_filter_column")

        # Select values to filter within the chosen column
        if selected_filter_column:
            filter_values = filtered_df[selected_filter_column].dropna().unique()
            selected_filter_values = st.multiselect(
                f"Filter values for '{selected_filter_column}'", filter_values, default=filter_values.tolist(), key="filter_values_multiselect"
            )

            # Apply the selected filter to the dataframe
            if selected_filter_values:
                filtered_df = filtered_df[filtered_df[selected_filter_column].isin(selected_filter_values)]

        # Checkbox to display values as percentages
        show_percentage = st.checkbox("Show as percentage", key="checkbox_percentage_task")

        # Dropdown to choose percentage calculation method
        percentage_method = "row"  # Default to 'row'
        if show_percentage:
            percentage_method = st.radio("Calculate percentages by", ("row", "column"), key="radio_percentage_method_task")

        # Step 3: Generate the crosstab
        if st.button("Generate Crosstab", key="generate_crosstab_task"):
            if filtered_df.empty:
                st.warning("No data available after filtering. Please adjust your filters.")
            else:
                # Calculate the crosstab
                crosstab_result = pd.crosstab(filtered_df[column1], filtered_df[column2])

                num_rows = crosstab_result.shape[0]
                row_height = 35  # Approximate height per row in pixels
                max_height = 20000  # Set a max height to avoid overly tall tables
                calculated_height = min(max_height, num_rows * row_height + 50)  # Add buffer for header

                # If percentage option is selected, normalize by row or column totals
                if show_percentage:
                    if percentage_method == "row":
                        crosstab_result = crosstab_result.div(crosstab_result.sum(axis=1), axis=0) * 100
                    else:
                        crosstab_result = crosstab_result.div(crosstab_result.sum(axis=0), axis=1) * 100
                    crosstab_result = crosstab_result.round(2)
                    crosstab_result = crosstab_result.style.format("{:.2f}%")

            # Display the crosstab with dynamic height
            st.write("Crosstab Result:")
            st.dataframe(crosstab_result, use_container_width=True, height=calculated_height)