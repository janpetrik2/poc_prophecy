# Databricks notebook source
# MAGIC %pip install faker

# COMMAND ----------

from faker import Faker
import pandas as pd
import csv
import random

fake = Faker('en_UK')

# COMMAND ----------

def generate_client_row(n):
    gender = 'F' if random.random() < 0.5 else 'M'
    return (
        f"{n+1}".zfill(12),
        fake.first_name_female() if gender == 'F' else fake.first_name_male(),
        fake.last_name_female() if gender == 'F' else fake.last_name_male(),
        fake.address().replace('\n', ', '),
        fake.ssn()
    )

def generate_client_table(n_records=100):

    df = spark.createDataFrame(
        [generate_client_row(n) for n in range(1, n_records)],
        ['CLIENT_ID', 'FIRSTNAME', 'LASTNAME', 'ADDRESS', 'SSN']
    )

    df.write.saveAsTable('dev.prophecy_poc.input_client', mode='overwrite')

# COMMAND ----------

generate_client_table()

# COMMAND ----------

def generate_account_type():
    account_types = [
        ('00000001', 'Standard account'),
        ('00000002', 'Saving account A'),
        ('00000003', 'Saving account B'),
        ('00000004', 'Saving account C'),
        ('00000005', 'Premium account')
    ]

    df = spark.createDataFrame(
        account_types,
        ['ACCOUNT_TYPE_ID', 'ACCOUNT_NAME']
    )

    df.write.saveAsTable('dev.prophecy_poc.input_account_type', mode='overwrite')

# COMMAND ----------

generate_account_type()

# COMMAND ----------

def generate_account(account_types_ids, client_ids):
    return (
        fake.bban(),
        fake.random_element(account_types_ids),
        fake.random_element(client_ids),
    )

def generate_account_table(n_records=110):
    df_account_type = spark.read.table('dev.prophecy_poc.input_account_type')
    account_types_ids = [row.ACCOUNT_TYPE_ID for row in df_account_type.select("ACCOUNT_TYPE_ID").collect()]

    df_clients = spark.read.table('dev.prophecy_poc.input_client')
    client_ids = [row.CLIENT_ID for row in df_clients.select("CLIENT_ID").collect()]

    df = spark.createDataFrame(
        [generate_account(account_types_ids, client_ids) for n in range(1, n_records)],
        ['ACCOUNT_ID', 'ACCOUNT_TYPE_ID', 'CLIENT_ID']
    )

    df.write.saveAsTable('dev.prophecy_poc.input_account', mode='overwrite')

# COMMAND ----------

generate_account_table()

# COMMAND ----------

def generate_transaction(account_ids):
    return (
        fake.uuid4(),
        fake.random_element(account_ids),
        fake.date_time_this_month(),
        fake.bban(),
        round(random.uniform(-50000, 50000),2),
    )

def generate_transaction_table(n_records=1000):
    df_account = spark.read.table('dev.prophecy_poc.input_account')
    account_ids = [row.ACCOUNT_ID for row in df_account.select("ACCOUNT_ID").collect()]

    df = spark.createDataFrame(
        [generate_transaction(account_ids) for n in range(1, n_records)],
        ['TRANSCATION_ID', 'ACCOUNT_ID', 'PAYMENT_DATETIME', 'OTHER_PARTY_ACCOUNT_ID', 'AMOUNT']
    )

    df.write.saveAsTable('dev.prophecy_poc.input_transaction', mode='overwrite')
    

# COMMAND ----------

generate_transaction_table()
