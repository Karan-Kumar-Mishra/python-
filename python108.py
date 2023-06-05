def searcher():
    import time
    book="This is a book on mr.zack "
    time.sleep(4)
    
    while True:
        text=(yield)
        if text in book:
            print("your text is in tine book")
        else:
            print("text is not in the book")
search=searcher()
print("search started")
next(search)
search.send("jack")
input("press any key")
search.send("jack and")

