from flaskblog import create_app,db
app=create_app()
if __name__=="__main__":
    app.run(port=7000,debug=True)
    db.create_all()
