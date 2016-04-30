
def fetchPedestrian(osm_id,meta_data,refs):
    if 'highway' in meta_data:
        value = meta_data['highway']
        if(value == 'pedestrian'):
            data ={}
            data['osmId'] = osm_id
            data['nodes']=refs
            data['meta_data']=meta_data
            return data
        else:
            return None
    else:
        return None
    
def fetchPedestrian2(osm_id,meta_data,refs):
            data ={}
            data['osmId'] = osm_id
            data['nodes']=refs
            data['meta_data']={}
            for key in meta_data:
                if key.find("."):
                    key1 = key.replace(".","_")
                data['meta_data'][key1] = meta_data[key]    
            return data

def fetchNodesForWays(osm_id,meta_data,coords,waysCollection):
    edge = waysCollection.find({"nodes":{"$in":[osm_id]}})
    if edge !=None and edge.count()>0:
        data ={}
        data['osmId'] = osm_id
        data['lat']=coords[0]
        data['lng']=coords[1]
        data['meta_data']=meta_data
        return data
    else:
        return None
      
def fetchNodesForWays2(osm_id,meta_data,coords,waysCollection):
        data ={}
        data['osmId'] = osm_id
        data['lat']=coords[0]
        data['lng']=coords[1]
        data['meta_data']=meta_data
        return data