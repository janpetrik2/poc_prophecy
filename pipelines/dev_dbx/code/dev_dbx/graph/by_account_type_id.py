from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dev_dbx.config.ConfigStore import *
from dev_dbx.functions import *

def by_account_type_id(spark: SparkSession, in0: DataFrame, in1: DataFrame, in2: DataFrame) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.ACCOUNT_TYPE_ID") == col("in1.ACCOUNT_TYPE_ID")), "inner")\
        .join(in2.alias("in2"), (col("in1.ACCOUNT_ID") == col("in2.ACCOUNT_ID")), "inner")
