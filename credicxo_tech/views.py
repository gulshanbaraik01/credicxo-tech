from django.shortcuts import render
import pandas as pd
import json


# Create your views here.
def Search(request):
    d = {}
    query = request.GET.get('search')
    query1 = request.GET.get('searchbank')
    query2 = request.GET.get('searchcity')
    df = pd.read_csv('https://raw.githubusercontent.com/snarayanank2/indian_banks/master/bank_branches.csv')
    if query:
        val = df.loc[df['ifsc'] == query].reset_index()
        d = val.to_dict()
        d = {'val': d, 'message': '1'}
    elif query1 and query2:
        array = [query1, query2]
        vall = df.loc[(df['bank_name'].isin(array) & df['city'].isin(array))].reset_index()
        json_records = vall.reset_index().to_json(orient='records')
        data = []
        data = json.loads(json_records)
        d = {'vall': data, 'message': '2'}

    return render(request, 'home.html', d)
