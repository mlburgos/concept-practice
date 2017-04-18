# Enter your code here. Read input from STDIN. Print output to STDOUT

# docs = []
# out = ''
# while True:
#     try:
#         docs.append(raw_input().split(',')) 
#     except EOFError:
#         break

def find_missing_docs(docs):
    #print docs
    fieldd = docs[0]
    docs = docs[1:]

    # generate the set of application ids
    app_ids = set()

    # generate set of docTypes
    doc_types = set()

    for doc in docs:
        app_ids.add(doc[3])
        doc_types.add(doc[2])

    # generate a dictionary where the keys are the docTypes
    ids_by_docType = dict.fromkeys(doc_types)

    for doc_type in ids_by_docType:
        ids_by_docType[doc_type] = set()

    for doc in docs:
        ids_by_docType[doc[2]].add(doc[3])

    for_printing = []

    for doc_type in doc_types:
        if len(ids_by_docType[doc_type]) == len(app_ids):
            continue

        add_to_for_printing = [doc_type, []]

        for app_id in app_ids:
            if app_id not in ids_by_docType[doc_type]:
                add_to_for_printing[1].append(app_id)

        for_printing.append(add_to_for_printing)

    for_printing.sort()
    # print for_printing

    is_first = True
    for doc_type, ids in for_printing:

        ids.sort()

        if is_first:
            print doc_type
            is_first = False
        else:
            print '\n' + doc_type

        for app_id in ids:
                print app_id,





test_data = [['fname', 'owner', 'doctype', 'appid', 'len'],
             ['fname', 'owner', 'a', '1', 'len'],
             ['fname', 'owner', 'a', '2', 'len'],
             ['fname', 'owner', 'b', '1', 'len'],
             ['fname', 'owner', 'c', '2', 'len'],
             ['fname', 'owner', 'd', '1', 'len'],
             ['fname', 'owner', 'd', '3', 'len'],
             ]


# find_missing_docs(test_data)
