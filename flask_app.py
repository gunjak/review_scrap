from flask import Flask, render_template
from flask_cors import CORS,cross_origin
import scrap
import pymongo



app = Flask(__name__)
CORS(app)

try:
    @app.route('/',methods=['GET'])
    @cross_origin()
    def homepage():
        client = pymongo.MongoClient("mongodb+srv://KUMARI:123@cluster0.nbqmr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client['ineuron_data']
        db_data = db['coll'].find({})
        if db['coll'].count_documents({}) > 0:
            return render_template('results.html', detail=db_data)
        else:
            table = db['coll']
            try:
                course_d=scrap.courses_detail(scrap.get_course())
            except:
                print("error")
            table.insert_many(course_d)
        return render_template('results.html', detail=course_d)


except:
    print("error")


if __name__ == "__main__":
    app.run(port=8000,debug=True)

