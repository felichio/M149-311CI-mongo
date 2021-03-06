from pymongo import MongoClient
from bson.objectid import ObjectId
import json




def get_fifty_most_upvoted_requests(db, start_date):
    result = db.requests.aggregate([
        {"$match": {"$expr": {"$eq": ["$creation_date", {"$dateFromString": {"dateString": start_date}}]}}},
        {"$match": {"upvoted_by": {"$exists": True}}}, 
        {"$project": {"_id": {"$toString": "$_id"}, "upvotes": {"$size": "$upvoted_by"}}},
        {"$sort": {"upvotes": -1}},
        {"$limit": 50}
    ])

    return json.dumps(list(result))


# print(get_fifty_most_upvoted_requests7("2016-05-18"))