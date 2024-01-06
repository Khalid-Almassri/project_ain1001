# Note to Prof.:
# This assignment was so hard if it wasnt for the fact that you had already posted the project i would've
# thought that this was the project.

# Task-1: Load the historical data from the file orcl.csv into a list of dictionaries.

def load_data(file_path):
    # an empty list is initialized in here to store the data from the csv file as a dictionary
    data = []
    with open(file_path, 'r') as file:
        # read the header and split it into a list of column names
        header = file.readline().strip().split(',') 

        for line in file:
            # each line is split into a list of values
            values = line.strip().split(',')

            # a dictionary is created using the headers as keys and values as values 
            row_dict = dict(zip(header, values))

            # makes sure that each number/numerical value is converted to a float
            for key in row_dict:
                if key != 'Date':
                    row_dict[key] = float(row_dict[key])

            # adds the dictionary to the list of data created earlier
            data.append(row_dict)

    return data

# file path to the .csv file
file_path = 'C:\\Users\\Khalid Almassri\\Downloads\\orcl.csv'
historical_data = load_data(file_path)

# Task-2: Calculate two technical indicators:

# function to calculate Simple Moving Averages for a given window
def calculate_sma(data, window):
    sma_values = []
    for i in range(window - 1, len(data)):
        close_prices = [data[j]['Close'] for j in range(i - window + 1, i + 1)]
        sma = sum(close_prices) / window
        sma_values.append(sma)
    return sma_values

# function to calculate Relative Strength Index (RSI) for a given window
def calculate_rsi(data, window):
    rsi_values = []
    for i in range(window - 1, len(data)):
        close_prices = [data[j]['Close'] for j in range(i - window + 1, i + 1)]
        gain, loss = 0, 0

        for j in range(1, len(close_prices)):
            price_difference = close_prices[j] - close_prices[j - 1]
            if price_difference > 0:
                gain += price_difference
            else:
                loss += abs(price_difference)

        avg_gain = gain / window
        avg_loss = loss / window

        if avg_loss == 0:
            rsi = 100
        else:
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))

        rsi_values.append(rsi)

    return rsi_values

# calculate 5-day SMA
sma_5_day = calculate_sma(historical_data, 5)
# this was written to check if task 2 was complete but is now rendered useless with task 3 being completed
#print(sma_5_day)

# calculate 14-day RSI
rsi_14_day = calculate_rsi(historical_data, 14)
# refer to line no. 75
#print(rsi_14_day)

# Task-3: Write each indicator to a file: Moving Averages to the file orcl-sma.csv and RSI to the file orcl-rsi.csv.

# write 5-day SMA to orcl-sma.csv
with open('orcl-sma.csv', 'w') as sma_file:
    # takes the values from sma_5_day and adds it to the file created
    for value in sma_5_day:
        sma_file.write(f"{value}\n")

# write 14-day RSI to orcl-rsi.csv
with open('orcl-rsi.csv', 'w') as rsi_file:
    # refer to line 87
    for value in rsi_14_day:
        rsi_file.write(f"{value}\n")