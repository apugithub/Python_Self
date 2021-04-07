dct = {"tables": ["t1", "t2", "t3", "t4"], "sourcecolumns": ["t1.a","t2.b"],
       "linkages": ["link1", "link2", "link3"],"filter": ["1=1", "filter1", "filter2"], "broadcast": ["t1"]}


def fw(**kargs):
    # Error Handling in input
    if (len(kargs['linkages']) < len(kargs['tables']) - 1):
        print('Discrepancy in number of links and tables provided')

        '''sql.append("None")
        status.append("Failed")
        msg.append("Discrepancy in number of links and tables provided")'''

    else:
        # Framing broadcast string
        if not kargs['broadcast']:
            brdcst = ""
        else:
            brdcst = "/*+ broadcast(" + ','.join(i for i in kargs['broadcast']) + ")*/ "

        df = "select " + brdcst + ', '.join(i for i in kargs['sourcecolumns']) + \
             " from " + ' join '.join(i for i in kargs['tables']) + " on " + ' on '.join(
            i for i in kargs['linkages']) + " where " + ' and '.join(i for i in kargs['filter'])

        print (df)

        brdcst = "/*+ broadcast(" + ','.join(i for i in kargs['broadcast']) + ")*/ "
        #print (brdcst)
        #print (kargs['broadcast'])

fw(tables=dct["tables"], sourcecolumns=dct["sourcecolumns"], linkages=dct["linkages"], filter=dct["filter"], broadcast=dct["broadcast"])


