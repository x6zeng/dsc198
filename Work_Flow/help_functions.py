# this python file assumes you already imported following pacakges:
# sys, os, numpy, pandas

# load data

def load_transaction():
    # load the whole transaction dataset
    transaction_path = os.path.join("data", "train_transaction.csv")
    train_transaction = pd.read_csv(transaction_path)
    return train_transaction

def load_transaction_nonv():
    # load the transaction dataset except v-columns
    transaction = load_transaction()
    nonv = transaction.loc[:, ~transaction.columns.str.contains("V")]
    del transaction # release memory
    return nonv

def load_transaction_v():
    # only load the v data in transaction
    transaction = load_transaction()
    v = transaction.loc[:, transaction.columns.str.contains("V")]
    del transaction
    return v

def load_label():
    transaction = load_transaction()
    label = transaction['isFraud']
    del transaction
    return label

# missing value

def missing_value_summary(df, k=0.5):
    # give a summary on the missing columns which missing percentage >= k
    for col in df: # col stands for column name
        missing_perc = np.average(df[col].isnull())
        if missing_perc >= k:
            print(col, "missing percentage is", missing_perc)

def missing_value_list(df, k=0.5):
    # return a true false list based on missing percentage and threshold k
    lst = [True if np.average(df[col].isnull()) >= k else False for col in df]
    return lst