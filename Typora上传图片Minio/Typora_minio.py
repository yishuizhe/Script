import os  
import time  
import uuid  
import sys  
import requests  
from minio import Minio  
from minio.error import S3Error  
import warnings  

ip = ""
port = ""
accessKey = ""
secretKey = ""
isSSl = False
bucket = ""

warnings.filterwarnings('ignore')  
images = sys.argv[1:]  
minioClient = Minio(ip+":"+port,  
                    access_key=accessKey, secret_key=secretKey, secure=isSSl)  
result = "Upload Success:\n"  
date = time.strftime("%Y%m%d%H%M%S", time.localtime())  
  
for image in images:  
    file_type = os.path.splitext(image)[-1]  
    new_file_name = date + file_type  
    if image.endswith(".png") or image.endswith(".jpg") or image.endswith(".gif"):  
        content_type ="image/"+file_type.replace(".", "")  
    else:  
        content_type ="image/jpeg"  # 默认使用jpeg类型  
        continue  
    try:  
        with open(image, 'rb') as file_data:  
            minioClient.put_object(bucket_name=bucket, object_name=new_file_name, data=file_data, content_type=content_type)  
        if image.endswith("temp"):  
            os.remove(image)  
        result = result +"http://"+ip+":"+port+ "/"+bucket+"/"  + new_file_name + "\n"  
    except S3Error as err:  # 捕获S3Error异常  
        result = result + "error:" + err.message + "\n"  
print(result)
