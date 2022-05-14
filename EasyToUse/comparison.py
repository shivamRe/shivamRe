import difflib 
first_file = 'file1' 
scnd_file = 'file2' 
fstFileLine = open(first_file).readlines( ) 
scndFileLine = open(scnd_file).readlines( )
diffrence = difflib.HtmlDiff( ).make_file(fstFileLine,scndFileLine,first_file,scnd_file) 
diff_report = open('ComparisionReport.html','w') 
diff_report.write(diffrence) 
diff_report.close( )
