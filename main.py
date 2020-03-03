from flask import Flask, render_template, request,Markup
import process as p
import model as m
from flask_restful import Resource, Api
app = Flask(__name__)

api = Api(app)
@app.route("/" ,methods = ["GET","POST"])
def home():
    if (request.method == "POST"):
        i_name = request.form.get("inp1")
        i_mno = request.form.get("inp2")
        i_ug = request.form.get("inp3")
        try:
            i_ugy = int(request.form.get("inp4"))
        except:
            # Assining the least year
            i_ugy = 2018
        i_pg = request.form.get("inp5")
        
        try:
            i_pgy = int(request.form.get("inp6"))
        except:
            # Assigning the least year
            i_pgy = 2018
        try:
            r_py = int(request.form.get("rat1"))
        except:
            r_py = "0"
        try:
            r_r = int(request.form.get("rat2"))
        except:
            r_r = "0"
        try:
            r_ds = int(request.form.get("rat3"))
        except:
            r_ds = "0"
        c_ml = request.form.get("chb1")
        c_dl = request.form.get("chb2")
        c_nlp = request.form.get("chb3")
        c_sts = request.form.get("chb4")
        c_aws = request.form.get("chb5")
        c_sql = request.form.get("chb6")
        c_excel = request.form.get("chb8")
        print(i_name,i_mno,i_ug,i_ugy,i_pg,i_pgy,r_py,r_r,r_ds,c_ml,c_dl,c_nlp,c_sts,c_aws,c_sql,c_excel)    
        testdata = ['Unknown',r_py,r_r,r_ds,max(i_ugy,i_pgy),[c_ml,c_dl,c_nlp,c_sts,c_aws,c_sql,c_excel].count('on')*3]
        print(testdata)
        result = m.final_model(testdata)
        print(result)
        # overall_score = p.scoring(i_name,i_mno,i_ug,i_ugy,i_pg,i_pgy,r_py,r_r,r_ds,c_ml,c_dl,c_nlp,c_sts,c_aws,c_sql,c_excel)
    #     print(overall_score)
        if result == "Yes":
            output = Markup("""<div class="success">
        <h3>Congratulations !</h3>
        <span>Your profile has been shortlisted</span>
        <span> for Data Scientist </span>
       <a  href="/">  <span class ="btn0">OK</span> </a>
        
    </div>""")
        if result == "No":
            output = Markup("""
            <div class="failure">
        <h3>Sorry !</h3>
        <span>Your profile did not qualify for</span>
        <span> further discussion </span>
        <a  href="/">  <span class ="btn0">OK</span> </a>
    </div>
            """)
        return render_template('index.html',output = output)
        

    return render_template('index.html',output = " ")

@app.route("/manual/<strt>", methods = ["GET","POST"])
def manual(strt):
    testdata = strt.split('-')
    i_ugy = int(testdata[0])    
    r_py = int(testdata[1])
    r_r = int(testdata[2])
    r_ds = int(testdata[3])
    o_skill = int(testdata[4])
        
    testdata2 = ['Unknown',r_py,r_r,r_ds,i_ugy,o_skill]
    result,proba = m.final_model(testdata2)
    if result == "Yes":
        output = {"Candidate_Info":{"Python_rating":r_py,"R_rating":r_r,"Data_Science_Rating":r_ds,"Passout_Year":i_ugy,"Other_Skill_Scores":o_skill},"Selected":"Yes"}
    if result == "No":
        output = {"Candidate_Info":{"Python_rating":r_py,"R_rating":r_r,"Data_Science_Rating":r_ds,"Passout_Year":i_ugy,"Other_Skill_Scores":o_skill},"Selected":"No"}     

    return output

class Info(Resource):
    def get(self,i_ugy,rt,o_skill):
        i_ugy = int(i_ugy)
        rt = rt.split("-")    
        r_py = int(rt[0])
        r_r = int(rt[1])
        r_ds = int(rt[2])
        o_skill = int(o_skill)
        testdata2 = ['Unknown',r_py,r_r,r_ds,i_ugy,o_skill]
        result,proba = m.final_model(testdata2)
        if result == "Yes":
            output = {"Candidate_Info":{"Python_rating":r_py,"R_rating":r_r,"Data_Science_Rating":r_ds,"Passout_Year":i_ugy,"Other_Skill_Scores":o_skill},"Selected":"Yes","Probability_Selection":1-proba[0]}
        if result == "No":
            output = {"Candidate_Info":{"Python_rating":r_py,"R_rating":r_r,"Data_Science_Rating":r_ds,"Passout_Year":i_ugy,"Other_Skill_Scores":o_skill},"Selected":"No","Probability_Rejection":proba[0]}     
        return output

api.add_resource(Info, '/Info/<i_ugy>/<rt>/<o_skill>')

        



if __name__ == "__main__":
    app.run(debug=True)