@app.route('/Search_Book',methods=['GET','POST'])
@login_required 
def Search_Book():
	bname="d"
	if request.method == "POST":
		bname=request.form.get("jd",None)
		s_book=request.form.get("searchbooks",None)

		if s_book:
			return render_template("searchbook.html", s_book = s_book)
		else:
			return "hello"
	return render_template('searchbook.html', title='Search Books')


