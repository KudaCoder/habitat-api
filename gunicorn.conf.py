import multiprocessing
import os

bind = "0.0.0.0:" + os.getenv("PORT")
workers = multiprocessing.cpu_count() * 2 + 1

accesslog = "-"
errorlog = "-"
