'''
Sample Input --
{"requests":"ACCOUNT_CAAS","tables": ["t1", "t2", "t3"], "sourcecolumns": ["t1.a","t2.b"], "linkages": ["link1", "link2"],"filter": ["1=1", "filter1", "filter2"], "broadcast": ["t1","t2"]}
{"requests":"TRADE_CAAS","tables": ["t4", "t5", "t6"], "sourcecolumns": ["t4.c","t5.d"], "linkages": ["link3"],"filter": ["filter3", "filter4", "filter5"], "broadcast": ["t4","t5"]}
{"requests":"ACCOUNT_CAAS","tables": ["tbl1", "tbl2", "tbl3"], "sourcecolumns": ["tbl1.a","tbl3.b"], "linkages": ["LNK1", "LNK2"],"filter": ["FLTR", "FLTR1", "FLTR2"], "broadcast": []}

'''

# jason import is required to convert string dictionary to dictionary
import json
import sys
import pytest


#def main():

sql = []
status = []
msg = []
rqst = []
final = [sql, status, msg, rqst]


with open("E:/hadoop/sample.json", "r") as file:
    dict_file = file.readlines()


def fw(**kargs):
    # Error Handling in input
    if (len(kargs['linkages']) < len(kargs['tables']) - 1):
        #print('Discrepancy in number of links and tables provided')

        sql.append("None")
        status.append("Failed")
        msg.append("Discrepancy in number of links and tables provided")
        rqst.append(kargs['requests'])

    else:
        # Framing broadcast string
        if not kargs['broadcast']:  #If broadcast list is empty
            brdcst = ""
        else:
            brdcst = "/*+ broadcast(" + ','.join(i for i in kargs['broadcast']) + ")*/ "

        # Main SQL statement formation
        df = "select " + brdcst + ', '.join(i for i in kargs['sourcecolumns']) + \
             " from " + ' join '.join(i for i in kargs['tables']) + " on " + ' on '.join(
             i for i in kargs['linkages']) + " where " + ' and '.join(i for i in kargs['filter'])

        sql.append(df)
        status.append("Success")
        msg.append("SQL Created Successfully")
        rqst.append(kargs['requests'])


for lines in dict_file:
    # Below try-except block will catch any issue in provided dictionaries
    try:
        # Convert dictionary string to dictionary
        dct = json.loads(lines)
        # Accessing dictionary elements and passing to the function
        fw(tables=dct["tables"], sourcecolumns=dct["sourcecolumns"], linkages=dct["linkages"],
           filter=dct["filter"], broadcast=dct["broadcast"], requests=dct["requests"])
    except Exception as x:
        sql.append("None")
        status.append("Failed")
        msg.append(x)

print(final)


# Creating output file first with append option
f = open("E:/hadoop/sample_op.txt","a")
# Writing to the same file converting the data as string
f.write(str(final))  # List can't be saved to a file
f.close()


# Executing main()
#if __name__=="__main__":
    #main()

# This is to run the pytest module in console itself
pytest.main(sys.argv)



################################## Execution of Unit Test cases #############################################

# Test 1: Dictionary validity check
def test_dict_check():
    for lines in dict_file:
        dct = json.loads(lines)
        assert type(dct) == dict


# Test 2: Required dict keys existance check
def test_dict_elements():
    for lines in dict_file:
        dct = json.loads(lines)
        assert (("tables" in dct) and ("sourcecolumns" in dct) and ("linkages" in dct) and ("filter" in dct)
                and ("broadcast" in dct) and ("requests" in dct))


# Test 3: Min no of linkages check
def test_required_no_linkages():
    for lines in dict_file:
        dct = json.loads(lines)
        assert len(dct['linkages']) == len(dct['tables']) - 1


# Test 4: Sourcecolumns must not be empty list
def test_source_column():
    for lines in dict_file:
        dct = json.loads(lines)
        assert len(dct['sourcecolumns']) >= 1


# Test 5: Number of elements in all lists (sql, status, msg, requests) are same
def test_final_list_elements():
    assert len(final[0]) == len(final[1]) == len(final[2]) == len(final[3])