from flask import Flask,render_template,request
from text_summary import summarizer
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/analyse', methods=['GET','POST'])
def analyse():
    if request.method=='POST':
       rawtext=request.form['rawtext'] 
       summary,original_txt,len_orig_txt,len_summary=summarizer(rawtext)
    return render_template(template_name_or_list)

if __name__=="__main__":
    app.run(debug=True)
    
