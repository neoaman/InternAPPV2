from flask import Flask, render_template, request,Markup
import process as p
app = Flask(__name__)

@app.route("/" ,methods = ["GET","POST"])
def home():
    if (request.method == "POST"):
        i_name = request.form.get("inp1")
        i_mno = request.form.get("inp2")
        i_ug = request.form.get("inp3")
        i_ugy = request.form.get("inp4")
        i_pg = request.form.get("inp5")
        i_pgy = request.form.get("inp6")
        r_py = request.form.get("rat1")
        r_r = request.form.get("rat2")
        r_ds = request.form.get("rat3")
        c_ml = request.form.get("chb1")
        c_dl = request.form.get("chb2")
        c_nlp = request.form.get("chb3")
        c_sts = request.form.get("chb4")
        c_aws = request.form.get("chb5")
        c_sql = request.form.get("chb6")
        c_excel = request.form.get("chb8")
        print(i_name,i_mno,i_ug,i_ugy,i_pg,i_pgy,r_py,r_r,r_ds,c_ml,c_dl,c_nlp,c_sts,c_aws,c_sql,c_excel)
        overall_score = p.scoring(i_name,i_mno,i_ug,i_ugy,i_pg,i_pgy,r_py,r_r,r_ds,c_ml,c_dl,c_nlp,c_sts,c_aws,c_sql,c_excel)
        print(overall_score)
        if overall_score >= 40:
            output = Markup("""<div class="success">
        <h3>Congratulations !</h3>
        <span>Your profile has been shortlisted</span>
        <span> for Data Scientist </span>
       <a  href="/">  <span class ="btn0">OK</span> </a>
        
    </div>""")
        if overall_score < 40:
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


if __name__ == "__main__":
    app.run(debug=True)