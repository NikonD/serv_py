from app.diagrams import diagram_module
from flask import render_template , redirect ,request , session ,jsonify ,json
from .forms import EditInds
import app.database.smdb

dm = app.database.smdb.DataManager()

rec_gi = dm.GetGroupIndicators()


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

# TODO move this urls in roles/methodist/
@diagram_module.route('/load_group_inds' , methods=['GET' , 'POST'])
def load_group_inds():
    EI = EditInds()
    EI.gen_select(rec_gi)
    if request.method == 'POST':
        # rec_i = dm.GetIndicators()
        return render_template('roles/methodist/edit_indicators.html'  , record_gi = rec_gi , ei = EI)

@diagram_module.route('/load_inds' , methods=['GET' , 'POST'])
def load_inds():
    EI = EditInds()
    EI.gen_select(rec_gi)
    if request.method == 'POST':
        data = request.values
        rec = dm.GetIndicators(int(data['select']))
        print(rec)
        return render_template('roles/methodist/table_inds.html' , inds=rec , ei=EI)

@diagram_module.route('/add_group_inds' , methods=['GET' , 'POST'])
def add_group_inds():
    if request.method == 'POST':
        data = request.values
        print(data['name_group_ind'])
        dm.AddGroupInds(data['name_ind'])
        record_gi = dm.GetGroupIndicators()
        return jsonify(record_gi)

@diagram_module.route('/del_group_inds' , methods=['GET' , 'POST'])
def del_group_inds():
    if request.method == 'POST':
        data = request.values
        dm.DelGroupInds(int(data['ind_group_id']))
        record_gi = dm.GetGroupIndicators()
        return jsonify(record_gi)

@diagram_module.route('/add_inds' , methods=['GET' , 'POST'])
def add_inds():
    if request.method == 'POST':
        data = request.values
        print(data['select']+"|"+data['name'])
        # print(type(int(data['select'])))
        dm.AddInds(int(data['select']) , data['name'])
        return "add"


@diagram_module.route('/del_inds' , methods=['GET' , 'POST'])
def del_inds():
    if request.method == 'POST':
        data = request.values
        dm.DelInds(int(data['ind_id']))
        return jsonify(data)