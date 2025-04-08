from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from dev_dbx.config.ConfigStore import *
from dev_dbx.functions import *
from prophecy.utils import *
from dev_dbx.graph import *

def pipeline(spark: SparkSession) -> None:
    df_input_account = input_account(spark)
    df_input_account_type = input_account_type(spark)
    df_input_transaction = input_transaction(spark)
    df_by_account_type_id = by_account_type_id(spark, df_input_account_type, df_input_account, df_input_transaction)
    df_transaction_summary = transaction_summary(spark, df_by_account_type_id)
    out_agg_transaction(spark, df_transaction_summary)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("dev_dbx").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/dev_dbx")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/dev_dbx", config = Config)(pipeline)

if __name__ == "__main__":
    main()
