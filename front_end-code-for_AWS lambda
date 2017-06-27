#!/usr/bin/python2.7

import os
import webapp2
import jinja2
import httplib

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment( loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

def doRender(handler, tname, values={}):
        temp = os.path.join(os.path.dirname(__file__),'templates/'+tname)
        if not os.path.isfile(temp):
                doRender(handler, 'index.htm')
                return
        # Make a copy of the dictionary and add the path
        newval = dict(values)
        newval['path'] = handler.request.path
        template = jinja_environment.get_template(tname)
        handler.response.out.write(template.render(newval))
        return True



class MainPage(webapp2.RequestHandler):
        def get(self):
                path = self.request.path
                doRender(self, path)


class RandomHandler(webapp2.RequestHandler):
        def post(self):
                company = self.request.get('com')
                investment = self.request.get('investment')
                M = self.request.get('M')
                T = self.request.get('T')
                R_ = self.request.get('R_')
                mm = M  #json1["key4"] 
                rr = R_ #json1["key5"]  
                #print "gulgygoguofufuf"
                Rr = int(mm)/int(rr)
                l_m = []
                for N in range(int(rr)): 
                        l_m.append(Rr)
                #l_m



		c1 =httplib.HTTPSConnection("e644jfpqtl.execute-api.eu-west-2.amazonaws.com")
		json1= '{ "T": "'+str(T)+'","com": "'+str(company)+'"}'
		c1.request("POST", "/retadj/", json1)
                response1 = c1.getresponse()
                data1 = response1.read()
		data1 = data1[1:len(data1)-1]
		eid = data1.split(",")
		
                #results = [] 
                rh95 = [ ]
		rh99 = [ ]
		rc95 = [ ]
		rc99 = [ ]
		rmc95 = [ ]
		rmc99 = [ ]
            
                for M in range(int(rr)): # l_m:
                        M = Rr
                        c = httplib.HTTPSConnection("ncr8yanvz6.execute-api.eu-west-2.amazonaws.com")
			
                        #json= '{ "key1": "1000"}'
                        json= '{ "T": "'+str(T)+'","com": "'+str(company)+'","investment": "'+str(investment)+'","M": "'+str(M)+'"}'
                        
                        c.request("POST", "/deployhud", json)
                        response = c.getresponse()
                        data = response.read()
			data = data[1:len(data)-1]
			words = data.split(",")
			
			rh95.append(words[0])
			rh99.append(words[1])
			rc95.append(words[2])
			rc99.append(words[3])
			rmc95.append(words[4])
			rmc99.append(words[5])
		
			
		#print ('ppppppppppppppppp')        
	        wh95 = [ ]
	        wh99 = [ ]
	        wc95 = [ ]
	        wc99 = [ ]
	        wmc95 = [ ]
	        wmc99 = [ ]
		#rt = 1
		#for h in
		#de = [1,2,3,4,5,6]
		for i in range(len(rh95[:])):
		#for e in resulth95:
		        a =float(rh95[i])
			b =float(rh99[i])
			c =float(rc95[i])
			d =float(rc99[i])
			e =float(rmc95[i])
			f =float(rmc99[i])
			wh95.append(a)
			wh99.append(b)
			wc95.append(c)
			wc99.append(d)
			wmc95.append(e)
			wmc99.append(f)
			
		mh95 = sum(wh95)/max(len(wh95),1)
		mh99 = sum(wh99)/max(len(wh99),1)
		mc95 = sum(wc95)/max(len(wc95),1)
		mc99 = sum(wc99)/max(len(wc99),1)
		mMc95 = sum(wmc95)/max(len(wmc95),1)
		mMc99 = sum(wmc99)/max(len(wmc99),1)
		
		mh95 = "Historical at 95% is : "+str(mh95)
		mh99 = "Historical at 99% is : "+str(mh99)
		mc95 = "Covariance at 95% is : "+str(mc95)
		mc99 = "Covariance at 99% is : "+str(mc99)
		mMc95 = "Monte Carlo, historical at 95% is : "+str(mMc95)
		mMc99 = "Monte Carlo, historical at 99% is : "+str(mMc99)

	        #doRender(self,'chart.htm',{'note':data1 } )
	        doRender(self,'index.htm',{' note1': mh95, 'note2': mh99,'note3': mc95, 'note4': mc99,'note5': mMc95, 'note6': mMc99, 'note' :data1} )        
                                
                #doRender(self,'index.htm',{'note1': results})
app = webapp2.WSGIApplication([('/random', RandomHandler),('/.*', MainPage)], debug=True)
                
