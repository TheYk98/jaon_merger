import glob,json
class json_merger:
    def merger(self):
        result = {}
        for f in glob.glob("*.json"):
            with open(f, "r") as infile:
                data=(json.loads(infile.read()))
                key=list(data.keys())
                
                    
                if len(result)==0:
                    result=data
                
                else:
                    #iterate through all the keys
                    for itr_key in key:
                        #if the key is already present
                        if itr_key in result.keys():
                            # check if the json is a array 
                            if isinstance(data[itr_key],list):
                                #append each item to the json    
                                for inner_object in data[itr_key]:
                                        result[itr_key].append(inner_object)
                            # if the key initially had only one value and in the second json it has another value,merge them as a list
                            elif isinstance(data[itr_key],str):
                                result[itr_key]=[(result[itr_key])]
                                result[itr_key].append(data[itr_key])
                                print(result[itr_key])
                                
                            #else, directly merge to the key
                            else:
                                result[itr_key].append(data[itr_key])
                        else:
                            result[itr_key]=data[itr_key]
                            
        with open('Merger.json', 'w') as outfile:
            json.dump(result, outfile)

test=json_merger()
test.merger()




            
            