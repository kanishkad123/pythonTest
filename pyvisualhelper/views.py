#import
from django.shortcuts import render
from django.views.generic import TemplateView
# import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.offline as opy
import plotly.graph_objs as go
import numpy as np
import matplotlib.pyplot as plt, mpld3
import pymongo
from pymongo import MongoClient
import json
#create your views
try:
    client = MongoClient('localhost',27017)
    print("Mongo connection successfull")
except:
    print("Problem with mongo connection")



class HomePageView(TemplateView):
    # def get(self, request, **kwargs):
    #     return render(request, 'index.html', context=None)
    def get(self,request,**kwargs):
        db = client.kanishkatest
        collection = db.djangotest
        emp_rec1 = {
                "name":"Mr.Kanishka",
                "eid":1,
                "location":"pune"
                }
        emp_rec2 = {
                "name":"Mr.Deshpande",
                "eid":2,
                "location":"pune"
                }
        emp_rec3 = {
                "name":"Mr.Anand",
                "eid":3,
                "location":"pune"
                } 
        rec_id1 = collection.insert_one(emp_rec1)
        rec_id2 = collection.insert_one(emp_rec2)
        rec_id3 = collection.insert_one(emp_rec3)
        print("Data inserted with record ids",rec_id1," ",rec_id2,rec_id3)
        cursor = collection.find()
        arrayWithNames = ['one','two','three']
        for record in cursor:
            print(record["name"])
            arrayWithNames[1]=record["name"]
        #return json.loads(arrayWithNames)
        return render(request,"index.html",context=None)
        

class AboutPageView(TemplateView):
    template_name="about.html"

    def get_context_data(self,**kwargs):
        context = super(AboutPageView,self).get_context_data(**kwargs)
        x1 = [1,2,3]
        y1 = [2,4,1]
        plt.plot(x1, y1, label = "line 1")
        x2 = [1,2,3]
        y2 = [4,1,3]
        plt.plot(x2, y2, label = "line 2")
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Two lines on same graph!')
        plt.legend()
        plt.show()

        x = [-2,0,4,6,7]
        y = [q**2-q+3 for q in x]
        trace1 = go.Scatter(x=x, y=y, marker={'color': 'blue', 'symbol': 104, 'size': "10"},
                            mode="lines",  name='1st Trace')
        data=go.Data([trace1])
        layout=go.Layout(title="General Plot kanishka", xaxis={'title':'x1'}, yaxis={'title':'x2'})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')
        # div = opy.plot(figure,include_plotlyjs=False, output_type='div')
        context['graph'] = div
        # return div
        return context
    
class renderHtml(TemplateView):
    def get(self, request, **kwargs):
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        sizes = [15, 30, 45, 10]
        explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()
        #figure1tohtml = mpld3.fig_to_html()
        #Stacked bar chart
        N = 5
        menMeans = (20, 35, 30, 35, 27)
        womenMeans = (25, 32, 34, 20, 25)
        menStd = (2, 3, 4, 1, 2)
        womenStd = (3, 5, 2, 3, 3)
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence

        p1 = plt.bar(ind, menMeans, width, yerr=menStd)
        p2 = plt.bar(ind, womenMeans, width,
                bottom=menMeans, yerr=womenStd)

        plt.ylabel('Scores')
        plt.title('Scores by group and gender')
        plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
        plt.yticks(np.arange(0, 81, 10))
        plt.legend((p1[0], p2[0]), ('Men', 'Women'))
        plt.show()
        #mpld3.show()


        return render(request,"index.html",context=None)