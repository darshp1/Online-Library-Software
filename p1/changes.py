@app.route('/changes',methods=['GET','POST'])
def changes():
	if request.method=="POST":
		uname=request.form.get("un",None)
		bname=request.form.get("bn",None)
		if uname and bname:
			me1 = t1(book_name1=bname, user_name1=uname)
			db.session.add(me1)
			db.session.commit()
			return render_template("done.html",title="done")
		else:
			me1 = t1(book_name1="problem", user_name1="occured")
			db.session.add(me1)
			db.session.commit()
			return render_template("done.html",title="done")
	return render_template("changes.html",title="changes")