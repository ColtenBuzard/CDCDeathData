#Functions to set parameters easier

#--------------GROUP BY------------
#----Top level grouping for our data-----
def group_By(param1,param2 ='*None*',param3='*None*',param4='*None*',param5='*None*'):
    #List of valid answers for the group_By function
    valid = {'cregion','cdivision','hregion','state','county','2013urban','2006urban',
    'age','gender','hispanicorigin','race','year','month','weekday','autopsy','placeofdeath','15leadingcauses',
    '15leadingcauses(infants)','icdchapter','icdsub-chapter','causeofdeath','113causelist',
    '130causelist(infants)','injuryintent','injurymechanism','drug/alcohol','*None*'
    }
    params = {param1,param2,param3,param4,param5}

    #if not in the valid list, throw error
    for i in params:
        if i not in valid:
            raise ValueError("\n \n You must group by one of these: \n %r." % valid + '\n')

    #takes the function paramater and converts it to the correct code for our query
    codematch = {'cregion':'D76.V10-level1','cdivision':'D76.V10-level2','hregion':'D76.V27-level1','state':'D76.V9-level1',
    'county':'D76.V9-level2','2013urban':'D76.V19','2006urban':'D76.V11','age':'D76.V5','gender':'D76.V7',
    'Hispanic Origin':'D76.V17','race':'D76.V8','year':'D76.V1-level1','month':'D76.V1-level2','weekday':'D76.V24','autopsy':'D76.V20',
    'placeofdeath':'D76.V21','15leadingcauses':'D76.V28','15leadingcauses(infants)':'D76.V29','icdchapter':'D76.V2-level1',
    'icdsub-chapter':'D76.V2-level2','causeofdeath':'D76.V2-level3','113causelist':'D76.V4',
    '130causelist(infants)':'D76.V12','injuryintent':'D76.V22','injurymechanism':'D76.V23','drug/alcohol':'D76.V25','*None*':'*None*'
    }

    #print out the XML code in correct format
    b_parameters = {
    "B_1": codematch[param1], 
    "B_2": codematch[param2], 
    "B_3": codematch[param3],
    "B_4": codematch[param4], 
    "B_5": codematch[param5]
    }

    return b_parameters


#--------------------MEASURES------------------------
#------The value we're tracking for each group-------
def measures(measure1='deaths',measure2 ='pop',measure3='percentofdeaths',measure4='',measure5=''):
    #List of valid answers for the group_By function
    valid = {'deaths','pop','crude','crudestandard','crude95','agerate','ageratestandard','agerateconfidence','percentofdeaths',''
    }
    measures = {measure1,measure2,measure3,measure4,measure5}

    #if not in the valid list, throw error
    for i in measures:
        if i not in valid:
            raise ValueError("\n \n You must group by one of these: \n %r." % valid + '\n')

    #takes the function paramater and converts it to the correct code for our query
    codematch1 = {'deaths': 'M_1','pop': 'M_2','crude': 'M_3','crudestandard':'M_31',
    'crude95':'M_32','agerate':'M_4','ageratestandard':'M_41','agerateconfidence':'M_42',
    'percentofdeaths':'M_9','':''
    }

    codematch2 = {'deaths': 'D76.M1','pop': 'D76.M2','crude': 'D76.M3','crudestandard':' D76.M31',
    'crude95':' D76.M32','agerate':'D76.M4','ageratestandard':' D76.M41','agerateconfidence':' D76.M42',
    'percentofdeaths':'D76.M9','':''
    }

    #print out the XML code in correct format
    b_parameters = {}

    for i in measures:
        if i != '':
            b_parameters[codematch1[i]] = codematch2[i]

    return b_parameters

def createParameterList(parameterList):
    """Helper function to create a parameter list from a dictionary object"""
    
    parameterString = ""
    
    for key in parameterList:
        parameterString += "\n"
        parameterString += "" + key + "\n"
        
        if isinstance(parameterList[key], list):
            for value in parameterList[key]:
                parameterString += "" + value + "\n"
        else:
            parameterString += "" + parameterList[key] + "\n"
        
        parameterString += "\n"
        
    return parameterString