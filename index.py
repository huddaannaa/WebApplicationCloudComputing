#!/usr/bin/python2.7

import os
import webapp2
import jinja2
import httplib
import boto.ec2
import urllib2
import time


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
                company    = self.request.get('com')
                investment = self.request.get('investment')
                M          = self.request.get('M')
                T          = self.request.get('T')
                R_         = self.request.get('R_')
		
		#ret
		c1 =httplib.HTTPSConnection("e644jfpqtl.execute-api.eu-west-2.amazonaws.com")
		json1= '{ "T": "'+str(T)+'","com": "'+str(company)+'"}'
		c1.request("POST", "/retadj/", json1)
        	response1 = c1.getresponse()
       		data1 = response1.read()
		data1 = data1[1:len(data1)-1]
		eid = data1.split(",")

		#adj
		#https://i2r4jpi5qf.execute-api.eu-west-2.amazonaws.com/adjh
		c2 =httplib.HTTPSConnection("i2r4jpi5qf.execute-api.eu-west-2.amazonaws.com")
		json2= '{ "T": "'+str(T)+'","com": "'+str(company)+'"}'
		c2.request("POST", "/adjh/", json2)
        	response2 = c2.getresponse()
       		data2 = response2.read()
		data2 = data2[1:len(data2)-1]

                


                conn= boto.ec2.connect_to_region("eu-west-2",aws_access_key_id="AKIAINOL5ISSNCJG5FSA" , aws_secret_access_key="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")

                reservations = conn.run_instances("ami-77d5c213",min_count=str(R_),max_count=str(R_),key_name="eulondon-hsd",instance_type="t2.micro",security_groups=["SSH"])

                adds=[]
				#get the dns of the instances
		instances = reservations.instances
		running = 0
		r = int(R_)
		while running!=r:	
			running = 0		
			for inst in instances:
				inst.update()
				print "Running instances "+str(running)+" Requested "+R_	
				if inst.state=="running":	
					running = running + 1
				else:
					#just wait
					#print inst.state,inst.id
					time.sleep(1)                
                
                for inst in instances:
                        adds.append(inst.public_dns_name)
 
                
                #company = 'amazon'
                #T = 1000
                #M = 10000
                #investment = 10000
                query = '/heat2.py?company='+str(company)+'&T='+str(T)+'&M='+str(M)+'&investment='+str(investment)
                responses = []
                #waiting for resposnse from ec2
                for add in adds:
			print 'asdasdasdasdasdasdasdasdasdasda'+str(len(adds))
			flag = True
			while flag:
				try:
				        print 'http://'+str(add)+query
					response = urllib2.urlopen('http://'+str(add)+query)
					print 'UP'
					flag = False
				except:
					print 'down'
					time.sleep(1)
                        #inst response gone through
                        response = urllib2.urlopen('http://'+str(add)+query)
		        text = response.read()
	                responses.append(text)
		tokill = []
		#terminate instances
		for inst in instances:
			tokill.append(str(inst.id))
		conn.terminate_instances(tokill)
		#print "Fuck em up"
                
                ###Now process the results
                results = [0,0,0,0,0,0]
                rest = responses
                for res in rest:
                        this = res.split(",")
                        for i in range (0,6):
                                value = this[i]
                                if ")"  in value:
                                        value=value.replace(")","")
                                       # print "sdasdas"+value+"sdsadasdasdasd"
                                if "("  in value:
                                        value=value.replace("(","")
                                results[i] = results[i]+float(value)
                resu = []
                for i in range(0,6):
                        u =results[i]/len(rest)
                        resu.append(u)
                
                
                mh95 = "Historical at 95% is : "+str(resu[0])
		mh99 = "Historical at 99% is : "+str(resu[1])
		mc95 = "Covariance at 95% is : "+str(resu[2])
		mc99 = "Covariance at 99% is : "+str(resu[3])
		mMc95 = "Monte Carlo, historical at 95% is : "+str(resu[4])
		mMc99 = "Monte Carlo, historical at 99% is : "+str(resu[5])
	        
	        doRender(self,'index.htm',{' note1': mh95, 'note2': mh99,'note3': mc95, 'note4': mc99,'note5': mMc95, 'note6': mMc99,'note8': data2[:], 'note7' :data1[:]} )        
                                
                #doRender(self,'index.htm',{'note1': results})
#app = webapp2.WSGIApplication([('/random', RandomHandler),('/.*', MainPage)], debug=True)
app = webapp2.WSGIApplication([('/random', RandomHandler),('/.*', MainPage)], debug=True)
                
