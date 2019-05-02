from app.diagrams import diagram_module
from flask import render_template , redirect ,request , session ,jsonify ,json
import app.database.smdb

dm = app.database.smdb.DataManager()

@diagram_module.route('/load_diagrams' , methods=['GET' , 'POST'])
def load_diagrams():

    if request.method=='POST':
        dict={"ind1":1488 , "ind2":8841}
        rec = dm.GetTeacherRateByIin('t0001')
        # TODO json response
        response = []
        d = {"_1":1 , "_2":2}
        d["_1"] = {"her":1111 , "niga":12314}
        # print(d)
        data = {"ind":str(),"val":float()}
        for r in rec:
            data["ind"]=r[0]
            data["val"]=r[1]
            response.append(data)
        # return (json.dumps(rec))
        print(rec)
        return jsonify(rec)
    return 0