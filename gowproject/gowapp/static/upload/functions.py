def handle_uploaded_file(f):
    with open('gowapp/static/upload/'+f.name,'wb+') as destination:
        for k in f.chunks():
            destination.write(k)
        
        

