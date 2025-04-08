from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dev_dbx.config.ConfigStore import *
from dev_dbx.functions import *

def out_agg_transaction(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`dev`.`prophecy_poc`.`out_agg_transaction`")
