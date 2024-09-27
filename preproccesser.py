import re
import pandas as pd
def preprocess(data):
    pattern = re.compile(r'(\d{2}/\d{2}/\d{2}), (\d{2}:\d{2}) - ([^:]+): (.*)')

    # Find all matches in the data
    matches = pattern.findall(data)

    # Create a DataFrame
    df = pd.DataFrame(matches, columns=['Date', 'Time', 'User', 'Message'])
    df[['Day', 'Month', 'Year']] = df['Date'].str.split('/', expand=True)

    # Convert year to four digits
    df['Year'] = '20' + df['Year']

    # Split time into hour and minute
    df[['Hour', 'Minute']] = df['Time'].str.split(':', expand=True)

    df['Month Name'] = df['Month'].apply(lambda x: pd.to_datetime(str(x), format='%m').strftime('%B'))

    # Combine the date and time columns into a single datetime column
    df['DateTime'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])
    # Extract day name
    df['Day Name'] = df['DateTime'].dt.day_name()

    # Reorder columns
    df = df[['Year', 'Month', 'Day', 'Hour', 'Minute', 'User', 'Message','Date','Day Name','Month Name']]
    return df
