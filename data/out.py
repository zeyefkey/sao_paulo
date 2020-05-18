import pandas as pd

def configure(context, require):
    require.stage("data.hts.cleaned")
    require.stage("data.census.cleaned")

def execute(context):
	
        
    df_hts_trips = context.stage("data.hts.cleaned")[1]
    df_hts_persons = context.stage("data.hts.cleaned")[0]
    df_census = context.stage("data.census.cleaned")
    
    df_hts_trips.to_csv("%s/HTS/trips.csv" %  context.config["raw_data_path"])
    df_hts_persons.to_csv("%s/HTS/persons.csv" %  context.config["raw_data_path"])
    df_census.to_csv("%s/Census/census.csv" %  context.config["raw_data_path"])