from sensor.exception import SensorException
import sys
import os
from dotenv import load_dotenv

from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection

load_dotenv()

if __name__ == "__main__":
    try:
        file_path = os.getenv("DATA_FILE_PATH")
        database_name = os.getenv("MONGO_DB_NAME")
        collection_name = os.getenv("MONGO_COLLECTION_NAME")

        dump_csv_file_to_mongodb_collection(
            file_path,
            database_name,
            collection_name
        )

    except Exception as e:
        raise SensorException(e, sys)





# from sensor.exception import SensorException
# import sys
# import os

# from sensor.logger import logging

# from sensor.utils import dump_csv_file_to_mongodb_collection


# # def test_exception():
    
# #     try:
# #         logging.info("Hi, Error aane wali hai named as division by zero wali")
# #         a = 1/0
# #     except Exception as e:
# #         raise SensorException(e, sys)  


# if __name__ == "__main__":
#     file_path=r"D:\Priyansh_Workspace\Projects\Project_2\APS_Guard\dataset\aps_failure_training_data1.csv"
#     database_name="ineuron"
#     collection_name="sensor"
#     dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)


#     # try:
#     #     test_exception()
#     # except Exception as e:
#     #     print(e)