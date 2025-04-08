from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dev_dbx.config.ConfigStore import *
from dev_dbx.functions import *

def transaction_summary(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("ACCOUNT_NAME"))

    return df1.agg(count(col("ACCOUNT_NAME")).alias("N_transactions"), sum(col("AMOUNT")).alias("SUM_transacation"))
