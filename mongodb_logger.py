from pymongo import MongoClient
import datetime

class MongoDBLogger:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db['job_logs']

    def log_job(self, job_id, status, result):
        log_entry = {
            'job_id': job_id,
            'status': status,
            'result': result,
            'timestamp': datetime.datetime.utcnow()
        }
        self.collection.insert_one(log_entry)

    def get_job_logs(self):
        return list(self.collection.find())

    def close(self):
        self.client.close()