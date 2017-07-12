import yaml
import math
from topological_node import topological_node




class topological_map(object):

    def __init__(self, filename=None):
        if filename:
            lnodes = self._loadMap(filename)
            self.nodes= self._get_nodes(lnodes)
        else:
            self.nodes=[]
        
        
    def _get_nodes(self, lnodes):
        nodes=[]
        for i in lnodes:
            node = topological_node(i['node'])
            nodes.append(node)
        return nodes
            

    def _loadMap(self, filename):
        print "loading " + filename
        with open(filename, 'r') as f:
            return yaml.load(f)
            
    def get_dict(self):
        s=[]
        #s['node']=[]
        for i in self.nodes:
            nod={}
            nod['node']={}
            nod['node']['pointset']='NA'
            nod['node']['name'] = i.name
            
            nod['node']['pose'] = {}
            nod['node']['pose']['position'] = {'x': i.pose.position.x, 'y': i.pose.position.y, 'z': i.pose.position.z}
            nod['node']['pose']['orientation'] = {'w': i.pose.orientation.w, 'x': i.pose.orientation.x, 'y': i.pose.orientation.y, 'z': i.pose.orientation.z}
            
            nod['node']['edges']=[]
            for j in i.edges:
                dd={}
                dd['action']= j.action
                dd['edge_id']= j.edge_id
                dd['node']= j.node                    
                nod['node']['edges'].append(dd)
            
            nod['node']['verts']=[]
            for h in i.verts:
                vv={'x': h.x,'y': h.y}
                nod['node']['verts'].append(vv)
                
            s.append(nod)
        
        return s
        