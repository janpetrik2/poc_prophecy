from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dev_dbx.config.ConfigStore import *
from dev_dbx.functions import *

def input_account_type(spark: SparkSession) -> DataFrame:
    return spark.read.table("`dev`.`prophecy_poc`.`input_account_type`")
