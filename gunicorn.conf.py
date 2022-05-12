import multiprocessing
import os

bind = "0.0.0.0:" + os.getenv("PORT")
workers = 2

accesslog = "-"
errorlog = "-"
